from otree.api import *


doc = """
In this app, participants rate the taste of each food item.
"""


class C(BaseConstants):
    NAME_IN_URL = 'Taste'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    taste_item1 = models.IntegerField(min=1, max=5)
    taste_item2 = models.IntegerField(min=1, max=5)
    taste_item3 = models.IntegerField(min=1, max=5)
    taste_item4 = models.IntegerField(min=1, max=5)
    taste_item5 = models.IntegerField(min=1, max=5)
    taste_item6 = models.IntegerField(min=1, max=5)
    taste_item7 = models.IntegerField(min=1, max=5)
    taste_item8 = models.IntegerField(min=1, max=5)
    


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
