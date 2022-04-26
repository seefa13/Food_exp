from otree.api import *


doc = """
In this app, participants will be asked follow-up questions and said 
good-bye.
"""


class C(BaseConstants):
    NAME_IN_URL = 'Outro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class Outro_Q(Page):
    pass

class Goodbye(Page):
    pass


page_sequence = [Outro_Q, Goodbye]
