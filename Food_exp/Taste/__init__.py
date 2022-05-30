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
    # list of food items
    # should be modified only here, not later on
    lFoods = [
        'a Banana',             'Strawberries',         'Chia seeds',       'Chips',                    'Salmon',
        'a Vegetable mix',      'White Beans',          'Yogurt',           'Whole Grain Bread (vegan)','a Chickenfilet',
        'Chocolate (vegan)',    'a Croissant (vegan)',  'Pork',             'a sugarfree Mueslibar',    'Water',
        'Cheese (vegan)',       'a Boiled Egg',         'Banana chips',     'a Berrysmoothie (vegan)',  'Vanilla Ice Cream (vegan)',
        'salted Cashews',       'smoked Salmon',        'Hummus',           'sweetened Cranberries',    'sweetened Yogurt (Soja)',
        'White Bread (vegan)',  'a breaded Chicken filet','Butter (vegan)', 'Milk',                     'a Sausage (Pork)',        
        'a sweetened Mueslibar','Lemonade',             'Cheese',           'Crackers',                 'a Soja-Drink',
        'Ravioli Funghi',       'salted Popcorn'
    ]

    # prices health scores
    lNutri = [
        1,1,1,4,1,
        1,1,1,1,1,
        5,5,2,1,1,
        4,1,4,5,4,
        3,4,3,3,2,
        2,3,5,2,4,
        3,3,4,4,1,
        2, 4
    ]
    ##          A: 13 (v: 9)
    # A: 13 
    ##          BC: 11 (v: 9)
    # B: 5
    # C: 6
    ##          DE: 13 (v: 9)
    # D: 9
    # E: 4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    iFruit = models.StringField(blank=True)
    iBerries = models.StringField(blank=True)
    iSeeds = models.StringField(blank=True)
    iChips = models.StringField(blank=True)
    iFish = models.StringField(blank=True)

    iVeg = models.StringField(blank=True)
    iBeans = models.StringField(blank=True)
    iYog = models.StringField(blank=True)
    iBread = models.StringField(blank=True)
    iChicken = models.StringField(blank=True)

    iChoco = models.StringField(blank=True)
    iCroissant = models.StringField(blank=True)
    iRedmeat = models.StringField(blank=True)
    iBar = models.StringField(blank=True)
    iDrink = models.StringField(blank=True)

    iCheese_h = models.StringField(blank=True)
    iEggs = models.StringField(blank=True)
    iFruit_unh = models.StringField(blank=True)
    iBerries_unh = models.StringField(blank=True)
    iIce = models.StringField(blank=True)

    iNuts_unh = models.StringField(blank=True)
    iFish_unh = models.StringField(blank=True)
    iHummus = models.StringField(blank=True)
    iCran = models.StringField(blank=True)
    iYog_unh = models.StringField(blank=True)

    iBread_unh = models.StringField(blank=True)
    iChicken_unh = models.StringField(blank=True)
    iButter_unh = models.StringField(blank=True)
    iMilk = models.StringField(blank=True)
    iRedmeat_unh = models.StringField(blank=True)   

    iBar_unh = models.StringField(blank=True)
    iDrink_unh = models.StringField(blank=True)
    iCheese_unh = models.StringField(blank=True)
    iCracker = models.StringField(blank=True)
    iSoja = models.StringField(blank=True)

    iRavioli = models.StringField(blank=True)
    iPopcorn = models.StringField(blank=True)

    V1 = models.StringField(blank=True)
    V2 = models.StringField(blank=True)


# PAGES
class Taste(Page):
    form_model = 'player'
    form_fields = [
        'iFruit', 'iBerries', 'iSeeds', 'iChips', 'iFish', 
        'iVeg', 'iBeans', 'iYog', 'iBread', 'iChicken', 
        'iChoco', 'iCroissant', 'iRedmeat', 'iBar', 'iDrink', 
        'iCheese_h', 'iEggs', 'iFruit_unh', 'iBerries_unh', 'iIce', 
        'iNuts_unh', 'iFish_unh', 'iHummus', 'iCran', 'iYog_unh', 
        'iBread_unh', 'iChicken_unh', 'iButter_unh', 'iMilk', 'iRedmeat_unh', 
        'iBar_unh', 'iDrink_unh', 'iCheese_unh', 'iCracker', 'iSoja', 
        'iRavioli', 'iPopcorn', 'V1','V2'
    ]
    
    @staticmethod
    def before_next_page(self,timeout_happened):
        participant = self.participant
        lPrevcomb = [100]

        # initialize lists of healthy and unhealthy food items, taste ratings, prices and health scores
        lFoods      = list(C.lFoods)
        lTastes     = [
            int(self.iFruit),int(self.iBerries),int(self.iSeeds),int(self.iChips),int(self.iFish),
            int(self.iVeg),int(self.iBeans),int(self.iYog),int(self.iBread),int(self.iChicken),
            int(self.iChoco),int(self.iCroissant),int(self.iRedmeat),int(self.iBar),int(self.iDrink),
            int(self.iCheese_h),int(self.iEggs),int(self.iFruit_unh),int(self.iBerries_unh),int(self.iIce),
            int(self.iNuts_unh),int(self.iFish_unh),int(self.iHummus),int(self.iCran),int(self.iYog_unh),
            int(self.iBread_unh),int(self.iChicken_unh),int(self.iButter_unh),int(self.iMilk),int(self.iRedmeat_unh),
            int(self.iBar_unh),int(self.iDrink_unh),int(self.iCheese_unh),int(self.iCracker),int(self.iSoja),
            int(self.iRavioli),int(self.iPopcorn)
        ]
        lNutri      = list(C.lNutri)

        # delete items with rating "1" in both lists
        # note: 'for value in lTastes' does not work since it takes the original position of the item and not from modified list
        ind_counter   = 0
        taste_counter = 0
        for taste_num in range(len(lTastes)):
            value = lTastes[taste_counter]
            print('The item under investigation is ',lFoods[taste_counter],' with index ',ind_counter,' Taste ',lTastes[taste_counter],' and the Nutri-Score ',lNutri[taste_counter],'.')
            if value == 1:
                print('The item ',lFoods[taste_counter],' (Index ',ind_counter,') with the Taste ',lTastes[taste_counter],' and the Nutri-Score ',lNutri[taste_counter],' will be removed.')
                lTastes.remove(lTastes[taste_counter])
                lFoods.remove(lFoods[taste_counter])
                lNutri.remove(lNutri[taste_counter])
                print('Removing done.')
                taste_counter = taste_counter - 1
            else:
                print('Item not removed.')
            ind_counter = ind_counter+1
            taste_counter = taste_counter + 1

        # save final lists to participant fields
        participant.lTastes=lTastes
        participant.lFoods=lFoods
        participant.lNutri=lNutri
        participant.lPrevcomb=lPrevcomb
        
        # Validate Taste ratings
        valid1 = int(int(self.V1)==2)
        valid2 = int(int(self.V2)==1)
        self.participant.validTasteQ = valid1 + valid2
        

page_sequence = [Taste]
