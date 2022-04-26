from otree.api import *


doc = """
This app contains a gernal introduction to otree and the task.
"""


class C(BaseConstants):
    NAME_IN_URL = 'Intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    correct1 = models.BooleanField
    correct2 = models.BooleanField
    correct3 = models.BooleanField


# PAGES
class Intro_Exp(Page):
    pass


class Intro_Task(Page):
    pass


class Intro_Q(Page):
    pass

class Intro_General(Page):
    pass

class Intro_Consent(Page):
    pass

page_sequence = [Intro_General, Intro_Consent, Intro_Exp, Intro_Task, Intro_Q]
