from this import d
from otree.api import *
from numpy import random


doc = """
In this app, participants will choose between products from the same
food category.
"""


class C(BaseConstants):
    NAME_IN_URL = 'Same'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 9
    sImagePath          = 'global/figures/'
    #Treatment
    iTreat = models.IntegerField
    # Food data
    lFoods_h = models.StringField()
    lFoods_unh = models.StringField()
    lTastes_h = models.IntegerField()
    lPrice_h = models.FloatField()
    lNutri_h = models.IntegerField()
    lTastes_unh = models.IntegerField()
    lPrice_unh = models.FloatField()
    lNutri_unh = models.IntegerField()

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Decision variables
    iHDec = models.BooleanField()
    dRT = models.IntegerField()
    # Attention variables
    sRowsRevealed = models.LongStringField()   
    sTimesRows = models.LongStringField()
    dTime2First         = models.FloatField(blank=True)
    ## Focus Variables
    iFocusLost          = models.IntegerField(blank=True)
    dFocusLostT         = models.FloatField(blank=True)
    iFullscreenChange   = models.IntegerField(blank=True)
    # Arousal
    iArousal = models.IntegerField(
        choices = [1,2,3,4,5]
    )
    # Others
    iRandelem = models.IntegerField(blank=True)
    practice = models.BooleanField(initial=False)


#FUNCTIONS
# initialize Treatments
def creating_session(subsession):
    import itertools
    health = itertools.cycle([0, 1, 2]) #0 is baseline, 1 is risk label, 2 is concrete risk
    if subsession.round_number == 1:
        for player in subsession.get_players():
            #assignment to treatment
            participant = player.participant
            participant.iRisk_treat = next(health)
            C.iTreat = participant.iRisk_treat
            # load participant data
            participant = player.participant
            C.lFoods_h = participant.lFoods_h
            C.lTastes_h = participant.lTastes_h
            C.lPrice_h = participant.lPrice_h
            C.lNutri_h = participant.lNutri_h
            C.lTastes_unh = participant.lTastes_unh
            C.lPrice_unh = participant.lPrice_unh
            C.lNutri_unh = participant.lNutri_unh
    # three practice rounds
    if subsession.round_number < 4: 
        player.practice == True

# PAGES
class Ready(Page):
    @staticmethod
    def is_displayed(player):
        return player.practice<4


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
        'dTime2First'
    ]

    @staticmethod
    def vars_for_template(player: Player):
        # choose randomly one food product
        player.iRandelem = random.randint(0,len(C.lFoods_h))
        iRandelem = player.iRandelem
        cp1 = C.lPrice_h[iRandelem]
        cp2 = C.lPrice_unh[iRandelem]
        ct1 = C.sImagePath+'Taste_'+str(C.lTastes_h[iRandelem])+'.png'
        ct2 = C.sImagePath+'Taste_'+str(C.lTastes_unh[iRandelem])+'.png'
        iTreat = C.iTreat
        if iTreat == 0:
            ch1 = C.sImagePath+'Nutri_'+str(C.lNutri_h[iRandelem])+'.png'
            ch2 = C.sImagePath+'Nutri_'+str(C.lNutri_unh[iRandelem])+'.png'
        else:
            ch1 = C.sImagePath+'Risk_'+str(C.lNutri_h[iRandelem])+'.png'
            ch2 = C.sImagePath+'Risk_'+str(C.lNutri_unh[iRandelem])+'.png' 

        return dict(
            Treatment = iTreat,
            cp1 = cp1,
            cp2 = cp2,
            ct1 = ct1,
            ct2 = ct2,
            ch1 = ch1,
            ch2 = ch2
        )

    #@staticmethod
    #def js_vars(player: Player):
        #session = player.session
     #   participant = player.participant
      #  dPixelRatio = participant.dPixelRatio
       # return dict (
        #    'bRequireFS'        : session.config['bRequireFS'],
         #   'bCheckFocus'       : session.config['bCheckFocus'],
          #  'iTimeOut'          : session.config['iTimeOut'],
        #    dPixelRatio = dPixelRatio
        #)

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            iRandelem = player.iRandelem
            practice = player.practice
            participant = player.participant
            if practice==False:
            # delete food product from list, if not practice trials
                C.lFoods_h.remove(iRandelem)
                C.lPrice_h.remove(iRandelem)
                C.lPrice_unh.remove(iRandelem)
                C.lTastes_h.remove(iRandelem)
                C.lTastes_unh.remove(iRandelem)
                C.lNutri_h.remove(iRandelem)
                C.lNutri_unh.remove(iRandelem)
            # add Focus variables to total if it's not practice trial
                participant.iOutFocus = int(participant.iOutFocus) + player.iFocusLost
                participant.iFullscreenChanges = int(participant.iFullscreenChanges) + player.iFullscreenChange
                participant.dTimeOutFocus = float(participant.dTimeOutFocus) + player.dFocusLostT

class Arousal(Page):
    form_model = 'player'
    form_fields = ['iArousal']


page_sequence = [Ready, Fixation, Choice, Arousal]
