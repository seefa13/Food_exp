from otree.api import *


doc = """
In this app, participants will deselect food categories.
"""


class C(BaseConstants):
    NAME_IN_URL = 'Foods'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Fruits = models.BooleanField(
        choices=[
            [True,'I can eat that'], 
            [False,'I cannot eat that'],
            ]
        )
    Vegetables = models.BooleanField(
        choices=[
            [True,'I can eat that'], 
            [False,'I cannot eat that'],
            ]
        )
    Grains = models.BooleanField(
        choices=[
            [True,'I can eat that'], 
            [False,'I cannot eat that'],
            ]
        )
    Beans = models.BooleanField(
        choices=[
            [True,'I can eat that'], 
            [False,'I cannot eat that'],
            ]
        )
    Fish = models.BooleanField(
        choices=[
            [True,'I can eat that'], 
            [False,'I cannot eat that'],
            ]
        )
    Meat = models.BooleanField(
        choices=[
            [True,'I can eat that'], 
            [False,'I cannot eat that'],
            ]
        )
    Poultry = models.BooleanField(
        label = 'Chicken',
        choices=[
            [True,'I can eat that'], 
            [False,'I cannot eat that'],
            ]
        )
    Dairy = models.BooleanField(
        label='Milk products',
        choices=[
            [True,'I can eat that'], 
            [False,'I cannot eat that'],
            ]
        )
    Nuts = models.BooleanField(
        choices=[
            [True,'I can eat that'], 
            [False,'I cannot eat that'],
            ]
        )
    Eggs = models.BooleanField(
        choices=[
            [True,'I can eat that'], 
            [False,'I cannot eat that'],
            ]
        )


# PAGES
class Food_Categories(Page):
    form_model = 'player'
    form_fields = ['Fruits', 'Vegetables', 'Grains', 'Fish', 'Meat', 'Dairy', 'Nuts', 'Eggs', 'Poultry', 
    'Beans']


page_sequence = [Food_Categories]
