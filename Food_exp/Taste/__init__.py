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
    taste_item1 = models.IntegerField(
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    taste_item2 = models.IntegerField(
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    taste_item3 = models.IntegerField(
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    taste_item4 = models.IntegerField(
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    taste_item5 = models.IntegerField(
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    taste_item6 = models.IntegerField(
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    taste_item7 = models.IntegerField(
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    taste_item8 = models.IntegerField(
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    


# PAGES
class Taste_Q(Page):
    form_model = 'player'
    form_fields = ['taste_item1', 'taste_item2', 'taste_item3', 'taste_item4', 'taste_item5', 'taste_item6', 
    'taste_item7', 'taste_item8']


page_sequence = [Taste_Q]
