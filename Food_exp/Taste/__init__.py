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
    t_fruit = models.IntegerField(
        label = 'Fruitmix',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_fruit_sweet = models.IntegerField(
        label = 'Fruitmix sweetened',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_walnuts = models.IntegerField(
        label = 'Walnuts',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_peanuts = models.IntegerField(
        label = 'Peanuts, salted',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_fish = models.IntegerField(
        label = 'Fish',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_fishsticks = models.IntegerField(
        label = 'Fishsticks',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_Veg = models.IntegerField(
        label = 'Some vegetables',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_Veg_bread = models.IntegerField(
        label = 'Breaded Vegetables',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_beans = models.IntegerField(
        label = 'Some beans',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_beans_baked = models.IntegerField(
        label = 'Baked Beans',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_yog = models.IntegerField(
        label = 'Yogurt',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_yog_sweet = models.IntegerField(
        label = 'Sweetened Yogurt',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_bread_whole = models.IntegerField(
        label = 'Whole Grain Bread',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_bread_white = models.IntegerField(
        label = 'White Bread',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_cheese = models.IntegerField(
        label = 'Cheese',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_cheese_bread = models.IntegerField(
        label = 'Breaded cheese',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_egg = models.IntegerField(
        label = 'Cooked Egg',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_egg_fried = models.IntegerField(
        label = 'Fried Egg',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_chicken = models.IntegerField(
        label = 'Chicken',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_nuggets = models.IntegerField(
        label = 'Chicken Nuggets',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_butter = models.IntegerField(
        label = 'Butter',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_butter_lowfat = models.IntegerField(
        label = 'Low Fat Butter',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_milk = models.IntegerField(
        label = 'Milk',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_milkshake = models.IntegerField(
        label = 'Milkshake',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_redmeat = models.IntegerField(
        label = 'Some Red Meat',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_sausage = models.IntegerField(
        label = 'Sausage',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )    
    t_mueslibar = models.IntegerField(
        label = 'Mueslibar',
        choices=[
            [1,'I would never like eat that'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
        )
    t_proteinbar = models.IntegerField(
        label = 'Proteinbar',
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
    form_fields = ['t_fruit', 't_fruit_sweet', 't_walnuts', 't_peanuts', 't_fish', 't_fishsticks',
    't_Veg', 't_Veg_bread', 't_beans', 't_beans_baked', 't_yog', 't_yog_sweet', 't_bread_whole', 
    't_bread_white', 't_cheese', 't_cheese_bread', 't_egg', 't_egg_fried', 't_chicken', 't_nuggets', 
    't_butter', 't_butter_lowfat', 't_milk', 't_milkshake', 't_redmeat', 't_sausage', 't_mueslibar', 
    't_proteinbar']

    #form_fields = ['Fruitmix', 'Fruitmix sweetened', 'Walnuts', 'Peanuts, salted', 'Fish', 'Fishsticks', 
    #'Some Vegetables', 'Breaded Vegetables', 'Some Beans', 'Baked Beans', 'Yogurt', 'Sweetened Yogurt',
    #'Whole Grain Bread', 'White Bread', 'Cheese', 'Breaded Cheese', 'Cooked Egg', 'Fried Egg', 'Chicken',
    #'Chicken Nuggets', 'Butter', 'Low Fat Butter', 'Milk', 'Milkshake', 'Some Red Meat', 'Sausage', 
    #'Mueslibar', 'Proteinbar']


page_sequence = [Taste_Q]
