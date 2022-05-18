from otree.api import *


doc = """
In this app, participants will rate food items.
"""

#FUNCTIONS
#def make_ifield(label):
 #   return models.IntegerField(
  #      label = label,
   #     choices=[
    #        [1,'I do not want to or cannot eat that due to taste, diet, moral, allergy or other reasons'], 
     #       [2,'I would most likely not like to eat that'],
      #      [3,'I would sometimes like to eat that'],
       #     [4,'I would most likely like to eat that'],
        #    [5,'I would definitely like to eat that'],
         #   ]
    #)

class C(BaseConstants):
    NAME_IN_URL = 'Taste'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    lPrice_h = [0.2,0.9,1.5,1.2,2.8,0.7,0.4,1.3,0.2,1.3,0.2,0.1,0.7,0.1,0.1,0.8,0.4]
    lPrice_unh = [1.1,0.7,1,1.1,3.5,1.3,0.3,1.5,0.2,1.5,0.8,0.1,0.8,0.1,0.1,1.5,0.6]
    lNutri_h = [1,1,1,2,1,1,1,1,1,1,3,1,2,1,1,2,1]
    lNutri_unh = [4,5,3,3,4,2,3,3,2,3,5,2,4,3,3,4,3]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iFruit = models.StringField(blank=True)
    iFruit_unh = models.StringField(blank=True)
    iBerries = models.StringField(blank=True)
    iBerries_unh = models.StringField(blank=True)
    iSeeds = models.StringField(blank=True)
    iSeeds_unh = models.StringField(blank=True)
    iNuts = models.StringField(blank=True)
    iNuts_unh = models.StringField(blank=True)
    iFish = models.StringField(blank=True)
    iFish_unh = models.StringField(blank=True)
    iVeg = models.StringField(blank=True)
    iVeg_unh = models.StringField(blank=True)
    iBeans = models.StringField(blank=True)
    iBeans_unh = models.StringField(blank=True)
    iYog = models.StringField(blank=True)
    iYog_unh = models.StringField(blank=True)
    iBread = models.StringField(blank=True)
    iBread_unh = models.StringField(blank=True)
    iChicken = models.StringField(blank=True)
    iChicken_unh = models.StringField(blank=True)
    iButter_unh = models.StringField(blank=True)
    iButter = models.StringField(blank=True)
    iMilk = models.StringField(blank=True)
    iMilk_unh = models.StringField(blank=True)
    iRedmeat = models.StringField(blank=True)
    iRedmeat_unh = models.StringField(blank=True)   
    iBar_unh = models.StringField(blank=True)
    iBar = models.StringField(blank=True)
    iDrink = models.StringField(blank=True)
    iDrink_unh = models.StringField(blank=True)
    iCheese = models.StringField(blank=True)
    iCheese_unh = models.StringField(blank=True)
    iEggs = models.StringField(blank=True)
    iEggs_unh = models.StringField(blank=True)
    V1 = models.StringField(blank=True)
    V2 = models.StringField(blank=True)


# PAGES
class Taste(Page):
    form_model = 'player'
    form_fields = [
        'iFruit','iFruit_unh','iBerries','iBerries_unh','iSeeds','iSeeds_unh','iNuts','iNuts_unh','iFish','iFish_unh',
        'iVeg','iVeg_unh','iBeans','iBeans_unh','iYog','iYog_unh','iBread','iBread_unh','iChicken','iChicken_unh',
        'iButter_unh','iButter','iMilk','iMilk_unh','iRedmeat','iRedmeat_unh','iBar_unh','iBar','iDrink','iDrink_unh',
        'iCheese','iCheese_unh','iEggs','iEggs_unh','V1','V2'
    ]
    
    @staticmethod
    def before_next_page(self,timeout_happened):
        participant = self.participant
        lPrevRandelem = [100]
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
        int(self.iFruit),int(self.iBerries),int(self.iSeeds),int(self.iNuts),int(self.iFish),int(self.iVeg),
        int(self.iBeans),int(self.iYog),int(self.iBread),int(self.iChicken),int(self.iButter),int(self.iMilk),
        int(self.iRedmeat),int(self.iBar),int(self.iDrink),int(self.iCheese),int(self.iEggs)
        ]
        lTastes_unh = [
        int(self.iFruit_unh),int(self.iBerries_unh),int(self.iSeeds_unh),int(self.iNuts_unh),int(self.iFish_unh),
        int(self.iVeg_unh),int(self.iBeans_unh),int(self.iYog_unh),int(self.iBread_unh),int(self.iChicken_unh),
        int(self.iButter_unh),int(self.iMilk_unh),int(self.iRedmeat_unh),int(self.iBar_unh),int(self.iDrink_unh),
        int(self.iCheese_unh),int(self.iEggs_unh)
        ]
        lPrice_h = list(C.lPrice_h)
        lPrice_unh = list(C.lPrice_unh)
        lNutri_h = list(C.lNutri_h)
        lNutri_unh = list(C.lNutri_unh)
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
        participant.lPrevRandelem=lPrevRandelem
        # Validate Taste ratings
        valid1 = int(int(self.V1)==2)
        valid2 = int(int(self.V2)==1)
        self.participant.validTasteQ = valid1 + valid2
        

page_sequence = [Taste]
