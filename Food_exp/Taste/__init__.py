from ast import ListComp
from itertools import combinations
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

    # health scores
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

    # combinations and types of comparison
    lComparions = ['AvBC','AvDE','BCvDE']
    lTypes = ['largeal','largenal','small']


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
    V3 = models.StringField(blank=True)


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
        'iRavioli', 'iPopcorn', 'V1','V2','V3'
    ]
    
    @staticmethod
    def before_next_page(self,timeout_happened):
        participant = self.participant

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
        # note: 'for value in lTastes' does not work since it takes the original position of the item and not from 
        # modified list
        
        # go through every element (taste_num) in lTastes and remove it if the value is 1
        # taste counter tracks the counter of the updated taste list (if no item removed, taste_counter and taste_num 
        # are equal)
        taste_counter = 0
        for taste_num in range(len(lTastes)):
            value = lTastes[taste_counter]
            if value == 1:
                lTastes.remove(lTastes[taste_counter])
                lFoods.remove(lFoods[taste_counter])
                lNutri.remove(lNutri[taste_counter])
                taste_counter = taste_counter - 1
            taste_counter = taste_counter + 1
        
        # aggregating items in A, BC and DE
        lFoods_A            = []
        score_count         = 0
        for score in lNutri:
            if score == 1:
                lFoods_A.append(score_count)
            score_count     = score_count + 1
        lFoods_BC           = []
        score_count         = 0
        for itemBC in lNutri:
            if itemBC == 2 or itemBC == 3:
                lFoods_BC.append(score_count)
            score_count     = score_count + 1
        lFoods_DE           = []
        score_count         = 0
        for itemDE in lNutri:
            if itemDE == 4 or itemDE == 5:
                lFoods_DE.append(score_count)
            score_count     = score_count + 1
        
        participant.lFoods_A = lFoods_A
        participant.lFoods_BC = lFoods_BC
        participant.lFoods_DE = lFoods_DE
        
        # separate taste lists and combine with original indeces
        lTaste_A            = []
        lTaste_BC           = []
        lTaste_DE           = []
        lTaste_A_ind        = []
        lTaste_BC_ind       = []
        lTaste_DE_ind       = []
        for foodA in lFoods_A:
            lTaste_A.append(lTastes[foodA])
            lTaste_A_ind.append(foodA)
        for foodBC in lFoods_BC:
            lTaste_BC.append(lTastes[foodBC])
            lTaste_BC_ind.append(foodBC)
        for foodDE in lFoods_DE:
            lTaste_DE.append(lTastes[foodDE])
            lTaste_DE_ind.append(foodDE)
        print('Taste list A is ',lTaste_A)
        print('Taste list A indeces are ',lTaste_A_ind)
        print('Taste list BC is ',lTaste_BC)
        print('Taste list BC indeces are ',lTaste_BC_ind)
        print('Taste list DE is ',lTaste_DE)
        print('Taste list DE indeces are ',lTaste_DE_ind)

        for comp in C.lComparions:
            for iType in C.lTypes:
                if comp == 'AvBC':
                    lTaste1 = lTaste_A
                    lTaste2 = lTaste_BC
                    lTaste1_ind = lTaste_A_ind
                    lTaste2_ind = lTaste_BC_ind
                elif comp == 'AvDE':
                    lTaste1 = lTaste_A
                    lTaste2 = lTaste_DE
                    lTaste1_ind = lTaste_A_ind
                    lTaste2_ind = lTaste_DE_ind
                else:
                    lTaste1 = lTaste_BC
                    lTaste2 = lTaste_DE
                    lTaste1_ind = lTaste_BC_ind
                    lTaste2_ind = lTaste_DE_ind

                # initialize variables and counters
                lIndeces_out        = []
                index_out1          = 0
                index_out2          = 0
                difindex_count      = 0
                taste1_ind_count    = 0
                taste2_ind_count    = 0
                dif                 = 0
                lDifs               = []
                index1              = 0
                index2              = 0
                lIndeces            = []

                # find largest difference aligned and not aligned with health rating and smallest difference
                for taste1 in lTaste1:
                    taste2_ind_count=0
                    for taste2 in lTaste2:
                        dif         = taste1-taste2
                        if iType == 'small':
                            lDifs.append(abs(dif))
                        else:
                            lDifs.append(dif)
                        index1      = lTaste1_ind[taste1_ind_count]
                        index2      = lTaste2_ind[taste2_ind_count]
                        lIndeces.append([index1,index2])
                        taste2_ind_count = taste2_ind_count +1
                    taste1_ind_count = taste1_ind_count +1
                if iType == 'largeal':
                    finaldif        = max(lDifs)
                elif iType == 'largenal':
                    finaldif        = min(lDifs)
                elif iType == 'small':
                    finaldif        = min(lDifs)
                else:
                    print("You selected the wrong type.")
                print('The difference list for ',iType,' is ',lDifs)
                print('The index list is ',lIndeces)        
                print('The difference is ',finaldif)

                # find (pairs of) indeces for the differences
                for d in lDifs:
                    if iType == 'smalldif':
                        running_dif = abs(d)
                    else:
                        running_dif = d
                    if running_dif == finaldif:
                        index_out1, index_out2 = lIndeces[difindex_count]
                        if [index_out1,index_out2] not in lIndeces_out:
                            lIndeces_out.append([index_out1,index_out2])
                    difindex_count  = difindex_count + 1
                print('The final index list is ',lIndeces_out)
                
        # save final index list for every one of the 9 combinations
                if comp == 'AvBC':
                    if iType == 'small':
                        participant.lInds_AvBC_small = lIndeces_out
                    elif iType == 'largeal':
                        participant.lInds_AvBC_largeal = lIndeces_out
                    else:
                        participant.lInds_AvBC_largenal = lIndeces_out
                elif comp == 'AvDE':
                    if iType == 'small':
                        participant.lInds_AvDE_small = lIndeces_out
                    elif iType == 'largeal':
                        participant.lInds_AvDE_largeal = lIndeces_out
                    else:
                        participant.lInds_AvDE_largenal = lIndeces_out
                else:
                    if iType == 'small':
                        participant.lInds_BCvDE_small = lIndeces_out
                    elif iType == 'largeal':
                        participant.lInds_BCvDE_largeal = lIndeces_out
                    else:
                        participant.lInds_BCvDE_largenal = lIndeces_out

        # save final lists to participant fields
        participant.lTastes=lTastes
        participant.lFoods=lFoods
        participant.lNutri=lNutri
        
        # Validate Taste ratings
        valid1 = int(int(self.V1)==2)
        valid2 = int(int(self.V2)==1)
        valid3 = int(int(self.V3)==3)
        participant.validTasteQ = valid1 + valid2 + valid3
    
    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        participant = player.participant
        participant     = player.participant
        lFoods_A        = participant.lFoods_A
        lFoods_BC       = participant.lFoods_BC
        lFoods_DE       = participant.lFoods_DE

        iLenAvBC = len(lFoods_A)*len(lFoods_BC)
        iLenAvDE = len(lFoods_A)*len(lFoods_DE)
        iLenBCvDE = len(lFoods_BC)*len(lFoods_DE)

        # validate food lists and skip to last page if invalid length is true
        bInvalidlen = False
        if iLenAvBC < 9 or iLenAvDE < 9 or iLenBCvDE < 9:
            bInvalidlen = True
        else:
            print("Foodlist is valid.")
        participant.bInvalidlen = bInvalidlen
        if bInvalidlen == True:
            return upcoming_apps[-1]
        
page_sequence = [Taste]
