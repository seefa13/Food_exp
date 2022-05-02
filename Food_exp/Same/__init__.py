from otree.api import *


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

class Player(BasePlayer):
    choice_unhealthy = models.BooleanField
    time_price = models.IntegerField
    time_taste = models.IntegerField
    time_health = models.IntegerField
    last_attribute = models.StringField
    resp_time = models.IntegerField
    arousal = models.IntegerField(
        choices = [1,2,3,4,5]
    )


# PAGES
class Fixation(Page):
    pass


class Choice(Page):
    pass


class Arousal(Page):
    form_model = 'player'
    form_fields = ['arousal']


page_sequence = [Fixation, Choice, Arousal]
