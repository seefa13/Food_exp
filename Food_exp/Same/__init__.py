from otree.api import *
from numpy import random 
import numpy as np


doc = """
In this app, participants will choose between products from the same
food category.
"""


class C(BaseConstants):
    NAME_IN_URL = 'Same'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 9
    sImagePath          = 'global/figures/'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iHDec = models.BooleanField()
    sRowsRevealed = models.LongStringField()    
    sTimesRows = models.LongStringField()
    slast = models.StringField()
    dRT = models.IntegerField()
    iArousal = models.IntegerField(
        choices = [1,2,3,4,5]
    )
    iTreat = models.IntegerField()

#FUNCTIONS
def creating_session(subsession):
    import itertools
    health = itertools.cycle([0, 1, 2]) #0 is baseline, 1 is risk label, 2 is concrete risk
    if subsession.round_number == 1:
        for player in subsession.get_players():
            #assignment to treatment
            participant = player.participant
            participant.iRisk_treat = next(health)
            player.iTreat = participant.iRisk_treat

# PAGES
class Fixation(Page):
    pass


class Choice(Page):
    form_model = 'player'
    form_fields = ['iHDec','dRT']

    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        lFoods_h = participant.lFoods_h
        lTastes_h = participant.lTastes_h
        lPrice_h = participant.lPrice_h
        lNutri_h = participant.lNutri_h
        lFoods_unh = participant.lFoods_unh
        lTastes_unh = participant.lTastes_unh
        lPrice_unh = participant.lPrice_unh
        lNutri_unh = participant.lNutri_unh
        iRandelem = random.randint(0,len(lFoods_h))
        sItem_h = lFoods_h[iRandelem]
        sItem_unh = lFoods_unh[iRandelem]
        cp1 = lPrice_h[iRandelem]
        cp2 = lPrice_unh[iRandelem]
        ct1 = C.sImagePath+'Taste_'+str(lTastes_h[iRandelem])+'.png'
        ct2 = C.sImagePath+'Taste_'+str(lTastes_unh[iRandelem])+'.png'
        iTreat = participant.iRisk_treat
        if iTreat == 0:
            ch1 = C.sImagePath+'Nutri_'+str(lNutri_h[iRandelem])+'.png'
            ch2 = C.sImagePath+'Nutri_'+str(lNutri_unh[iRandelem])+'.png'
        else:
            ch1 = C.sImagePath+'Risk_'+str(lNutri_h[iRandelem])+'.png'
            ch2 = C.sImagePath+'Risk_'+str(lNutri_unh[iRandelem])+'.png' 
        

        return dict(
            Treatment = iTreat,
            Item_h = sItem_h,
            Item_unh = sItem_unh,
            cp1 = cp1,
            cp2 = cp2,
            ct1 = ct1,
            ct2 = ct2,
            ch1 = ch1,
            ch2 = ch2
        )

class Arousal(Page):
    form_model = 'player'
    form_fields = ['iArousal']


page_sequence = [Fixation, Choice, Arousal]
