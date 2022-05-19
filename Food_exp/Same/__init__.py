from otree.api import *
from numpy import random


doc = """
In this app, participants will choose between products from the same
food category.
"""


class C(BaseConstants):
    NAME_IN_URL         = 'Same'
    PLAYERS_PER_GROUP   = None
    # number of rounds
    NUM_ROUNDS          = 10
    NUM_PROUNDS         = 1
    # image path for taste and health/risk attribute
    sImagePath          = 'global/figures/'


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # decision variables
    iHDec               = models.BooleanField()
    dRT                 = models.IntegerField()
    # attention variables
    sRowsRevealed       = models.LongStringField()   
    sTimesRows          = models.LongStringField()
    dTime2First         = models.FloatField(blank=True)
    ## focus Variables
    iFocusLost          = models.IntegerField(blank=True)
    dFocusLostT         = models.FloatField(blank=True)
    iFullscreenChange   = models.IntegerField(blank=True)
    # arousal
    iArousal            = models.IntegerField(
        choices = [1,2,3,4,5]
    )

# PAGES
class Practice(Page):
    # show only if practice round in the beginning
    @staticmethod
    def is_displayed(player):
        return player.round_number < (C.NUM_PROUNDS+1)


class Fixation(Page):
    pass


class Choice(Page):
    form_model = 'player'
    form_fields = [
        'iHDec',
        'dRT',
        'sRowsRevealed',
        'sTimesRows',
        'iFocusLost',
        'dFocusLostT',
        'iFullscreenChange',
        'dTime2First',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        participant         = player.participant
        iTreat              = participant.iRisk_treat

        # load participant data
        lFoods_h            = participant.lFoods_h 
        lTastes_h           = participant.lTastes_h
        lPrice_h            = participant.lPrice_h
        lNutri_h            = participant.lNutri_h
        lTastes_unh         = participant.lTastes_unh
        lPrice_unh          = participant.lPrice_unh
        lNutri_unh          = participant.lNutri_unh
        lPrevRandelem       = participant.lPrevRandelem
        lPrevRandelemcopy   = list(lPrevRandelem)

        # choose randomly one food product
        iRandelem           = random.randint(0,len(lFoods_h)-1)

        # if not practice round, look for food product in previous rounds
        if player.round_number > C.NUM_PROUNDS:
            while iRandelem in lPrevRandelemcopy:
                iRandelem   = random.randint(0,len(lFoods_h)-1)
        
        # increase list of previous food products by food product from this round
            lPrevRandelemcopy.append(iRandelem)
            participant.lPrevRandelem = lPrevRandelemcopy
        
        # assign cells for template
        cp1                 = lPrice_h[iRandelem]
        cp2                 = lPrice_unh[iRandelem]
        ct1                 = C.sImagePath+'Taste_'+str(lTastes_h[iRandelem])+'.png'
        ct2                 = C.sImagePath+'Taste_'+str(lTastes_unh[iRandelem])+'.png'

        # if baseline treatment, assign "Health", otherwise "Risk"
        if iTreat == 0:
            ch1             = C.sImagePath+'Nutri_'+str(lNutri_h[iRandelem])+'.png'
            ch2             = C.sImagePath+'Nutri_'+str(lNutri_unh[iRandelem])+'.png'
        else:
            ch1             = C.sImagePath+'Risk_'+str(lNutri_h[iRandelem])+'.png'
            ch2             = C.sImagePath+'Risk_'+str(lNutri_unh[iRandelem])+'.png' 

        # return everything
        return dict(
            Treatment       = iTreat,
            cp1             = cp1,
            cp2             = cp2,
            ct1             = ct1,
            ct2             = ct2,
            ch1             = ch1,
            ch2             = ch2
        )

    @staticmethod
    def js_vars(player: Player):
        session = player.session
        p = player.participant
        return {
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'iTimeOut'          : session.config['iTimeOut'],
            'dPixelRatio'       : p.dPixelRatio,
        }
        
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant                     = player.participant
        if player.round_number>C.NUM_PROUNDS:

        # add Focus variables to total if it's not practice trial
            participant.iOutFocus           = int(participant.iOutFocus) + player.iFocusLost
            participant.iFullscreenChanges  = int(participant.iFullscreenChanges) + player.iFullscreenChange
            participant.dTimeOutFocus       = float(participant.dTimeOutFocus) + player.dFocusLostT
        
        # if this is the selected trial, save it
        if (participant.SelectedTrial==player.round_number):
            CurrRandelem                    = participant.lPrevRandelem(-1)
            lFoods_h                        = participant.lFoods_h 
            lFoods_unh                      = participant.lFoods_unh
            if (player.iHDec==0):
                participant.Sel_Item        = lFoods_h[CurrRandelem]
            else:
                participant.Sel_Item        = lFoods_unh[CurrRandelem]

class Arousal(Page):
    form_model = 'player'
    form_fields = ['iArousal']


page_sequence = [Practice, Fixation, Choice, Arousal]
