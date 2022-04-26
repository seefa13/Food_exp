from otree.api import *


doc = """
In this app, participants will choose between products from different
food categories.
"""


class C(BaseConstants):
    NAME_IN_URL = 'Same'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice_unhealthy = models.BooleanField
    time_price = models.IntegerField
    time_taste = models.IntegerField
    time_health = models.IntegerField
    last_attribute = models.StringField
    resp_time = models.IntegerField
    arousal = models.IntegerField


# PAGES
class Fixation(Page):
    pass


class Choice(Page):
    pass


class Arousal(Page):
    pass


page_sequence = [Fixation, Choice, Arousal]
