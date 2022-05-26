from otree.api import *
from numpy import random


doc = """
In this app, participants will choose between products from the same
food category.
"""

class C(BaseConstants):
    NAME_IN_URL         = 'Same'
    PLAYERS_PER_GROUP   = None
    # number of rounds
    NUM_ROUNDS          = 10
    NUM_PROUNDS         = 1
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


class Fixation(Page):
    pass


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
        if health_comb == 'AvsBC':
            lFoods1         = lFoods_A
            lFoods2         = lFoods_BC
        elif health_comb == 'AvsDE':
            lFoods1         = lFoods_A
            lFoods2         = lFoods_DE
        else:
            lFoods1         = lFoods_BC
            lFoods2         = lFoods_DE
        iType               = curcomb[2]

        # separate taste lists and combine with original indeces
        lTaste1             = []
        lTaste2             = []
        lTaste1_ind         = []
        lTaste2_ind         = []
        for food1 in lFoods1:
            lTaste1.append(lTastes[food1])
            lTaste1_ind.append(food1)
        for food2 in lFoods2:
            lTaste2.append(lTastes[food2])
            lTaste2_ind.append(food2)
        print('Taste list 1 is ',lTaste1)
        print('Taste list 1 indeces are ',lTaste1_ind)
        print('Taste list 2 is ',lTaste2)
        print('Taste list 2 indeces are ',lTaste2_ind)
        
        # initialize variables and counters
        lIndeces_out        = []
        index_out1          = 0
        index_out2          = 0
        difindex_count      = 0
        taste1_ind_count    = 0
        taste2_ind_count    = 0
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
        session         = player.session
        p               = player.participant
        return {
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'iTimeOut'          : session.config['iTimeOut'],
            'dPixelRatio'       : p.dPixelRatio,
        }
        
    @staticmethod
    def before_next_page(player, timeout_happened):
        participant     = player.participant
        if player.round_number>C.NUM_PROUNDS:

        # add Focus variables to total if it's not practice trial
            participant.iOutFocus           = int(participant.iOutFocus) + player.iFocusLost
            participant.iFullscreenChanges  = int(participant.iFullscreenChanges) + player.iFullscreenChange
            participant.dTimeOutFocus       = float(participant.dTimeOutFocus) + player.dFocusLostT
        
        # save decision
            Items_sel                       = participant.Foods_sel
            if (player.iHDec==0):
                participant.lSel_Items      = Items_sel[0]
            else:
                participant.lSel_Items      = Items_sel[1]


page_sequence = [Practice, Fixation, Choice]
