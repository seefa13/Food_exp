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
    Fruits = models.BooleanField
    Vegetables = models.BooleanField
    Grains = models.BooleanField
    Fish = models.BooleanField
    Meat = models.BooleanField
    Dairy = models.BooleanField
    Nuts = models.BooleanField
    Eggs = models.BooleanField


# PAGES
class Food_Categories(Page):
    pass


page_sequence = [Food_Categories]
