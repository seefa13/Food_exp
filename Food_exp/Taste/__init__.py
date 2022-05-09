from otree.api import *


doc = """
In this app, participants will rate food items.
"""

#FUNCTIONS
def make_ifield(label):
    return models.IntegerField(
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
    iFruit = make_ifield('Banana') 
    iFruit_unh = make_ifield('Banana chips')
    iBerries = make_ifield('Strawberries')
    iBerries_unh = make_ifield('Strawberries, Smoothie')
    iSeeds = make_ifield('Chia seeds')
    iSeeds_unh = make_ifield('Sunflower seeds')
    iNuts = make_ifield('Cashews')
    iNuts_unh = make_ifield('Cashews, salted')
    iFish = make_ifield('Salmon')
    iFish_unh = make_ifield('Salmon, smoked')
    iVeg = make_ifield('Vegetable mix')
    iVeg_unh = make_ifield('Vegetables, breaded')
    iBeans = make_ifield('White Beans')
    iBeans_unh = make_ifield('Baked Beans')
    iYog = make_ifield('Yogurt, natural')
    iYog_unh = make_ifield('Yogurt, sweetened')
    iBread = make_ifield('Whole Grain Bread')
    iBread_unh = make_ifield('White Bread')
    iChicken = make_ifield('Chicken, filet')
    iChicken_unh = make_ifield('Chicken, breaded filet')
    iButter_unh = make_ifield('Butter')
    iButter = make_ifield('Butter, plant-based')
    iMilk = make_ifield('Milk, low fat')
    iMilk_unh = make_ifield('Milk, whole fat')
    iRedmeat = make_ifield('Pork')
    iRedmeat_unh = make_ifield('Pork, sausage')    
    iBar_unh = make_ifield('Mueslibar, no sugar added')
    iBar = make_ifield('Mueslibar, sweetened')
    iDrink = make_ifield('Water')
    iDrink_unh = make_ifield('Lemonade')
    iCheese = make_ifield('Cottage Cheese')
    iCheese_unh = make_ifield('Cheese')
    iEggs = make_ifield('Boiled Egg')
    iEggs_unh = make_ifield('Egg, salad')


# PAGES
class Taste(Page):
    form_model = 'player'
    form_fields = [
        'iFruit','iFruit_unh','iBerries','iBerries_unh','iSeeds','iSeeds_unh','iNuts','iNuts_unh','iFish','iFish_unh',
        'iVeg','iVeg_unh','iBeans','iBeans_unh','iYog','iYog_unh','iBread','iBread_unh','iChicken','iChicken_unh',
        'iButter_unh','iButter','iMilk','iMilk_unh','iRedmeat','iRedmeat_unh','iBar_unh','iBar','iDrink','iDrink_unh',
        'iCheese','iCheese_unh','iEggs','iEggs_unh'
    ]
    
    @staticmethod
    def before_next_page(self,timeout_happened):
        participant = self.participant
        lFoods_h = [
        'Banana','Strawberries','Chia seeds','Cashews','Salmon','Vegetable mix','White Beans','Yogurt',
        'Whole Grain Bread','Chicken, filet','Butter, plant-based','Milk, low fat','Pork','Mueslibar, no sugar added',
        'Water','Cottage Cheese','Boiled Egg'
        ]
        lFoods_unh = [
        'Banana chips','Strawberries, Smoothie','Sunflower seeds','Cashews, salted','Salmon, smoked',
        'Vegetables, breaded','Baked Beans','Yogurt, sweetened','White Bread','Chicken, breaded filet','Butter',
        'Milk, whole fat','Pork, sausage','Mueslibar, sweetened','Lemonade','Cheese','Egg, salad'
        ]
        lTastes_h = [
        self.iFruit,self.iBerries,self.iSeeds,self.iNuts,self.iFish,self.iVeg,self.iBeans,self.iYog,self.iBread,
        self.iChicken,self.iButter,self.iMilk,self.iRedmeat,self.iBar,self.iDrink,self.iCheese,self.iEggs
        ]
        lTastes_unh = [
        self.iFruit_unh,self.iBerries_unh,self.iSeeds_unh,self.iNuts_unh,self.iFish_unh,self.iVeg_unh,self.iBeans_unh,self.iYog_unh,
        self.iBread_unh,self.iChicken_unh,self.iButter_unh,self.iMilk_unh,
        self.iRedmeat_unh,self.iBar_unh,self.iDrink_unh,self.iCheese_unh,self.iEggs_unh
        ]
        lPrice_h = [0.2,0.9,1.5,1.2,2.8,0.7,0.4,1.3,0.2,1.3,0.2,0.1,0.7,0.1,0.1,0.8,0.4]
        lPrice_unh = [1.1,0.7,1,1.1,3.5,1.3,0.3,1.5,0.2,1.5,0.8,0.1,0.8,0.1,0.1,1.5,0.6]
        lNutri_h = [1,1,1,2,1,1,1,1,1,1,3,1,2,1,1,2,1]
        lNutri_unh = [4,5,3,3,4,2,3,3,2,3,5,2,4,3,3,4,3]
        counter = 0
        for value in lTastes_h:
            if value == 1:
                lTastes_h.remove(value)
                lFoods_h.pop(counter)
                lTastes_unh.pop(counter)
                lFoods_unh.pop(counter)
                lPrice_h.pop(counter)
                lPrice_unh.pop(counter)
                lNutri_h.pop(counter)
                lNutri_unh.pop(counter)
            counter=counter+1
        counter = 0
        for value in lTastes_unh:
            if value == 1:
                lTastes_unh.remove(value)
                lFoods_unh.pop(counter)
                lTastes_h.pop(counter)
                lFoods_h.pop(counter)
                lPrice_h.pop(counter)
                lPrice_unh.pop(counter)
                lNutri_h.pop(counter)
                lNutri_unh.pop(counter)
            counter=counter+1
        participant.lTastes_h=lTastes_h
        participant.lFoods_h=lFoods_h
        participant.lTastes_unh=lTastes_unh
        participant.lFoods_unh=lFoods_unh
        participant.lPrice_h=lPrice_h
        participant.lPrice_unh=lPrice_unh
        participant.lNutri_h=lNutri_h
        participant.lNutri_unh=lNutri_unh

page_sequence = [Taste]
