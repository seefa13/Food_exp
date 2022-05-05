from otree.api import *


doc = """
In this app, participants will rate food items.
"""

#FUNCTIONS
def make_ifield(label):
    return models.FloatField(
        label = label,
        choices=[
            [1,'I do not want to or cannot eat that due to taste, diet, moral, allergy or other reasons'], 
            [2,'I would most likely not like to eat that'],
            [3,'I would sometimes like to eat that'],
            [4,'I would most likely like to eat that'],
            [5,'I would definitely like to eat that'],
            ]
    )

class C(BaseConstants):
    NAME_IN_URL = 'Taste'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iFruit = make_ifield('Fruitmix') 
    iFruit_unh = make_ifield('Fruitmix sweetened')
    iNuts = make_ifield('Walnuts')
    iNuts_unh = make_ifield('Peanuts, salted')
    iFish = make_ifield('Fish')
    iFish_unh = make_ifield('Fishsticks')
    iVeg = make_ifield('Some vegetables')
    iVeg_unh = make_ifield('Breaded Vegetables')
    iBeans = make_ifield('Some beans')
    iBeans_unh = make_ifield('Baked Beans')
    iYog = make_ifield('Yogurt')
    iYog_unh = make_ifield('Sweetened Yogurt')
    iBread = make_ifield('Whole Grain Bread')
    iBread_unh = make_ifield('White Bread')
    iCheese = make_ifield('Cheese')
    iCheese_unh = make_ifield('Breaded cheese')
    iEggs = make_ifield('Cooked Egg')
    iEggs_unh = make_ifield('Fried Egg')
    iChicken = make_ifield('Chicken')
    iChicken_unh = make_ifield('Chicken Nuggets')
    iButter_unh = make_ifield('Butter')
    iButter = make_ifield('Low Fat Butter')
    iMilk = make_ifield('Milk')
    iMilk_unh = make_ifield('Milkshake')
    iRedmeat = make_ifield('Some Red Meat')
    iRedmeat_unh = make_ifield('Sausage')    
    iBar_unh = make_ifield('Mueslibar')
    iBar = make_ifield('Proteinbar')
    iDrink = make_ifield('Water')
    iDrink_unh = make_ifield('Lemonade')


# PAGES
class Taste(Page):
    form_model = 'player'
    form_fields = ['iFruit','iFruit_unh','iNuts','iNuts_unh','iFish','iFish_unh','iVeg','iVeg_unh','iBeans',
    'iBeans_unh','iYog','iYog_unh','iBread','iBread_unh','iCheese','iCheese_unh','iEggs','iEggs_unh','iChicken',
    'iChicken_unh','iButter_unh','iButter','iMilk','iMilk_unh','iRedmeat','iRedmeat_unh','iBar_unh','iBar',
    'iDrink','iDrink_unh']

page_sequence = [Taste]
