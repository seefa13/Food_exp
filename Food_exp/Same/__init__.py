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
        lFoods_unh = participant.lFoods_unh
        lTastes_unh = participant.lTastes_unh
        iRandelem=random.randint(0,len(lFoods_h))
        sItem_h = lFoods_h[iRandelem]
        sItem_unh = lFoods_unh[iRandelem]
        cp1 = 'Price 1'
        cp2 = 'Price 2'
        ct1 = lTastes_h[iRandelem]
        ct2 = lTastes_unh[iRandelem]
        ch1 = 'Health 1'
        ch2 = 'Health 2'
        iTreat = participant.iRisk_treat

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
