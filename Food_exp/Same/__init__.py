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


def creating_session(subsession):
    import itertools
    health = itertools.cycle([0, 1, 2]) #0 is baseline, 1 is risk label, 2 is concrete risk
    if subsession.round_number == 1:
        for player in subsession.get_players():
            participant = player.participant
            participant.risk_treat = next(health)
            player.sTreat = str(participant.risk_treat)

class Player(BasePlayer):
    iHDec = models.BooleanField()
    sRowsRevealed = models.LongStringField()    
    sTimesRows = models.LongStringField()
    slast = models.StringField()
    dRT = models.IntegerField()
    iArousal = models.IntegerField(
        choices = [1,2,3,4,5]
    )
    sTreat = models.StringField()


# PAGES
class Fixation(Page):
    pass


class Choice(Page):
    form_model = 'player'
    form_fields = ['iHDec','dRT']

    @staticmethod
    def vars_for_template(player: Player):
        cp1 = 'Price 1'
        cp2 = 'Price 2'
        ct1 = 'Taste 1'
        ct2 = 'Taste 2'
        ch1 = 'Health 1'
        ch2 = 'Health 2'

        return dict(
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
