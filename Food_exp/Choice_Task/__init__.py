from otree.api import *
from numpy import random


doc = """
In this app, participants will choose between products from the same
food category.
"""

class C(BaseConstants):
    NAME_IN_URL         = 'Choices'
    PLAYERS_PER_GROUP   = None
    # number of rounds
    NUM_ROUNDS          = 30
    NUM_PROUNDS         = 3
    # image path for taste and health/risk attribute
    sImagePath          = 'global/figures/'

    # make cominations
    comparisons         = ['AvBC','BCvDE','AvDE']
    pricetypes          = ['lowhigh','highlow','eq']
    prices              = [1,2,3]
    types               = ['largeal','largenal','small'] 
    combinations        = []
    for comp in comparisons:
        for pricetype in pricetypes:
            for type in types:
                combinations.append([comp,pricetype,type])
    #print('The combinations are ',combinations)


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # decision variables
    iHDec               = models.BooleanField()
    dRT                 = models.IntegerField()
    # attention variables
    sRowsRevealed       = models.LongStringField()   
    sTimesRows          = models.LongStringField()
    dTime2First         = models.FloatField(blank=True)
    ## focus Variables
    iFocusLost          = models.IntegerField(blank=True)
    dFocusLostT         = models.FloatField(blank=True)
    iFullscreenChange   = models.IntegerField(blank=True)

# PAGES
class Practice(Page):
    # show only if practice round in the beginning
    @staticmethod
    def is_displayed(player):
        return player.round_number < (C.NUM_PROUNDS+1)


class Ready(Page):
    # show only if practice round in the beginning
    @staticmethod
    def is_displayed(player):
        return player.round_number == (C.NUM_PROUNDS+1)


class Practice_FB(Page):
    # show only if practice round 
    @staticmethod
    def is_displayed(player):
        return player.round_number < (C.NUM_PROUNDS+1)
    @staticmethod
    def vars_for_template(player: Player):
        participant = player.participant
        lFoods = participant.lFoods
        practice_item = lFoods[participant.practice_item]
        practice_price = participant.practice_price
        return dict(
            practice_item = practice_item,
            practice_price = practice_price
        )


class Fixation(Page):
    def js_vars(player):
        bStartleft = int(random.choice([0,1]))
        return dict(
            Startleft = bStartleft
        )


class Choice(Page):
    form_model = 'player'
    form_fields = [
        'iHDec',
        'dRT',
        'sRowsRevealed',
        'sTimesRows',
        'iFocusLost',
        'dFocusLostT',
        'iFullscreenChange',
        'dTime2First',
    ]

    @staticmethod
    def vars_for_template(player: Player):
        participant         = player.participant
        iTreat              = participant.iRisk_treat

        # load participant data
        lFoods              = participant.lFoods
        lTastes             = participant.lTastes
        lNutri              = participant.lNutri

        # adding aggregated taste and index lists
        lTaste_A            = participant.lTaste_A
        lTaste_A_ind        = participant.lTaste_A_ind
        lTaste_BC            = participant.lTaste_BC
        lTaste_BC_ind        = participant.lTaste_BC_ind
        lTaste_DE            = participant.lTaste_DE
        lTaste_DE_ind        = participant.lTaste_DE_ind

        # find product, price and taste combinations and add to participant field
        combinations        = list(C.combinations)
        curcomb             = []
        randcomb            = random.randint(0,len(combinations)-1)
        curcomb             = combinations[randcomb]
        lPrevcomb_copy      = list(participant.lPrevcomb)
        lPrevcomb_copy.append(curcomb)
        participant.lPrevcomb = lPrevcomb_copy

        #assign type of taste (iType) and food comparison
        health_comb = curcomb[0]
        lTaste1             = []
        lTaste2             = []
        lTaste1_ind         = []
        lTaste2_ind         = []
        if health_comb == 'AvsBC':
            lTaste1         = lTaste_A
            lTaste2         = lTaste_BC
            lTaste1_ind     = lTaste_A_ind
            lTaste2_ind     = lTaste_BC_ind
        elif health_comb == 'AvsDE':
            lTaste1         = lTaste_A
            lTaste2         = lTaste_DE
            lTaste1_ind     = lTaste_A_ind
            lTaste2_ind     = lTaste_DE_ind
        else:
            lTaste1         = lTaste_BC
            lTaste2         = lTaste_DE
            lTaste1_ind     = lTaste_BC_ind
            lTaste2_ind     = lTaste_DE_ind
        iType               = curcomb[2]
        
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
        
        # find find largest difference aligned and not aligned with health rating and smallest difference
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
        
        # find indeces for the differences
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

        # choose one product combination randomly
        if len(lIndeces_out) == 1:
            randinds        = 0
        else:
            randinds = random.randint(0,len(lIndeces_out)-1)
        Finalinds           = lIndeces_out[randinds]
        participant.Foods_sel = Finalinds
        item1 = lFoods[Finalinds[0]]
        item2 = lFoods[Finalinds[1]]
        print('The food items used are ',item1,' and ',item2)

        ## assign cells for template
        # price
        prices              = list(C.prices)
        print('The price list is',prices)
        if curcomb[1] == 'lowhigh':
            cp1             = prices[0]
            cp2             = prices[2]
        elif curcomb[1] == 'highlow':
            cp1             = prices[2]
            cp2             = prices[0]
        else: 
            cp1             = prices[1]
            cp2             = prices[1]   
        if player.round_number<=C.NUM_PROUNDS:
        # if practice trial, save for feedback
            participant.practice_price1             = cp1
            participant.practice_price2             = cp2
            print('Prices have been recorded.')    
        print('The selected prices are ',cp1,' and ',cp2,' for the combination ',curcomb[1])

        # taste
        ct1                 = C.sImagePath+'Taste_'+str(lTastes[Finalinds[0]])+'.png'
        ct2                 = C.sImagePath+'Taste_'+str(lTastes[Finalinds[1]])+'.png'

        # if baseline treatment, assign "Health", otherwise "Risk"
        if iTreat == 0:
            ch1             = C.sImagePath+'Nutri_'+str(lNutri[Finalinds[0]])+'.png'
            ch2             = C.sImagePath+'Nutri_'+str(lNutri[Finalinds[1]])+'.png'
        else:
            ch1             = C.sImagePath+'Risk_'+str(lNutri[Finalinds[0]])+'.png'
            ch2             = C.sImagePath+'Risk_'+str(lNutri[Finalinds[1]])+'.png' 

        # return everything
        return dict(
            Treatment       = iTreat,
            cp1             = cp1,
            cp2             = cp2,
            ct1             = ct1,
            ct2             = ct2,
            ch1             = ch1,
            ch2             = ch2
        )

    @staticmethod
    def js_vars(player: Player):
        session             = player.session
        p                   = player.participant
        return {
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'iTimeOut'          : session.config['iTimeOut'],
            'dPixelRatio'       : p.dPixelRatio,
        }
        
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant                     = player.participant
        Items_sel                       = participant.Foods_sel
        Price1                          = participant.practice_price1
        Price2                          = participant.practice_price2
        try: 
            lSel_Items                  = participant.lSel_Items
        except:
            lSel_Items                  = []

        if player.round_number>C.NUM_PROUNDS:

        # add Focus variables to total if it's not practice trial
            participant.iOutFocus           = int(participant.iOutFocus) + player.iFocusLost
            participant.iFullscreenChanges  = int(participant.iFullscreenChanges) + player.iFullscreenChange
            participant.dTimeOutFocus       = float(participant.dTimeOutFocus) + player.dFocusLostT
        
        # save decision
            if (player.iHDec==0):
                try:
                    lSel_Items.append(Items_sel[0])
                except:
                    lSel_Items = [Items_sel[0]]
            else:
                try:
                    lSel_Items.append(Items_sel[1])
                except:
                    lSel_Items = [Items_sel[1]]
            participant.lSel_Items = lSel_Items
            print('lSel_Items is now ',lSel_Items,'.')
        else:
            if (player.iHDec==0):
                participant.practice_item   = Items_sel[0]
                participant.practice_price  = Price1
            else:
                participant.practice_item   = Items_sel[1]
                participant.practice_price  = Price2


page_sequence = [Practice, Ready, Fixation, Choice, Practice_FB]