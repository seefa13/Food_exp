from otree.api import *
import random


doc = """
In this app, participants will choose between products from the same
food category.
"""

class C(BaseConstants):
    NAME_IN_URL         = 'Choices'
    PLAYERS_PER_GROUP   = None
    Endowment = 5
    # number of rounds
    NUM_ROUNDS          = 33
    NUM_PROUNDS         = 3
    # image path for taste and health/risk attribute
    sImagePath          = 'global/figures/'

    # make cominations
    lComparisons        = ['AvBC','BCvDE','AvDE']
    lPricetypes         = ['lowhigh','highlow','eq']
    lTypes              = ['largeal','largenal','small'] 
    lPrices             = [1,2,3]
    lCombinations       = []
    lAddComps           = [
        ['BvC','lowhigh','largenal'], ['BvC','highlow','largenal'], ['BvC','eq','largenal'],
        ['DvE','lowhigh','largenal'], ['DvE','highlow','largenal'], ['DvE','eq','largenal']
    ]
    lForbidden          = [['AvBC', 'lowhigh', 'largeal'],['AvDE', 'lowhigh', 'largeal'],['BCvDE', 'lowhigh', 'largeal']]
    
    for comp in lComparisons:
        for pricetype in lPricetypes:
            for type in lTypes:
                if pricetype != 'lowhigh' or type != 'largeal':
                    lCombinations.append([comp,pricetype,type])
    for addition in lAddComps:
        lCombinations.append(addition)

    print('The combinations are ',lCombinations)

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
    # focus Variables
    iFocusLost          = models.IntegerField(blank=True)
    dFocusLostT         = models.FloatField(blank=True)
    iFullscreenChange   = models.IntegerField(blank=True)

# PAGES
class Practice(Page):
    # show only if practice round 
    @staticmethod
    def is_displayed(player):
        return player.round_number < (C.NUM_PROUNDS+1)


class Ready(Page):
    # show only if practice round 
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
        practice_payout = C.Endowment - practice_price
        return dict(
            practice_item = practice_item,
            practice_payout = practice_payout
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
        lInds_BvC_largenal  = participant.lInds_BvC_largenal
        lInds_DvE_largenal  = participant.lInds_DvE_largenal


        # find product, price and taste combinations, check whether previously used and add to participant field
        rn = player.round_number
        prn = C.NUM_PROUNDS

        # randomize
        if rn == 1:
            combinations    = list(C.lCombinations)
            if len(lInds_BvC_largenal) == 0:
                for comb in combinations:
                    if comb[0] == 'BvC':
                        combinations.remove(comb)
                randCombs       = random.sample(combinations,len(combinations))
                participant.randCombs = randCombs
            elif len(lInds_DvE_largenal) == 0:
                for comb in combinations:
                    if comb[0] == 'DvE':
                        combinations.remove(comb)
                        print('Combination',comb,'has been removed.')
                randCombs       = random.sample(combinations,len(combinations))
                participant.randCombs = randCombs
            else:
                randCombs       = random.sample(combinations,len(combinations))
                participant.randCombs = randCombs
        else:
            randCombs = participant.randCombs
        
        # take one element after the other
        if rn < prn+1:
            curcomb = random.choice(randCombs)
        else:
            curcomb             = randCombs[rn-1-prn]
        print('The chosen combination is ',curcomb)

        # import all index lists
        lInds_AvBC_small = participant.lInds_AvBC_small 
        lInds_AvBC_largeal = participant.lInds_AvBC_largeal
        lInds_AvBC_largenal = participant.lInds_AvBC_largenal

        lInds_AvDE_small = participant.lInds_AvDE_small 
        lInds_AvDE_largeal = participant.lInds_AvDE_largeal
        lInds_AvDE_largenal = participant.lInds_AvDE_largenal

        lInds_BCvDE_small = participant.lInds_BCvDE_small 
        lInds_BCvDE_largeal = participant.lInds_BCvDE_largeal
        lInds_BCvDE_largenal = participant.lInds_BCvDE_largenal

        # Choose a list for current indeces

        if curcomb[0] == 'AvBC':
            if curcomb[2] == 'small':
                lCurInds = lInds_AvBC_small 
            elif curcomb[2] == 'largeal':
                lCurInds = lInds_AvBC_largeal 
            else:
                lCurInds = lInds_AvBC_largenal
        elif curcomb[0] == 'AvDE':
            if curcomb[2] == 'small':
                lCurInds = lInds_AvDE_small 
            elif curcomb[2] == 'largeal':
                lCurInds = lInds_AvDE_largeal
            else:
                lCurInds = lInds_AvDE_largenal
        elif curcomb[0] == 'BCvDE':
            if curcomb[2] == 'small':
                lCurInds = lInds_BCvDE_small
            elif curcomb[2] == 'largeal':
                lCurInds = lInds_BCvDE_largeal
            else:
                lCurInds = lInds_BCvDE_largenal
        elif curcomb[0] == 'BvC':
            lCurInds = lInds_BvC_largenal
        else:
            lCurInds = lInds_DvE_largenal

        # choose one product combination randomly out of the final index list
        if len(lCurInds) == 1:
            randinds        = 0
        else:
            randinds = random.randint(0,len(lCurInds)-1)
        Finalinds           = lCurInds[randinds]
        participant.Foods_sel = Finalinds
        item1 = lFoods[Finalinds[0]]
        item2 = lFoods[Finalinds[1]]
        print('The food items used are ',item1,' (Nutri-Score: ',lNutri[Finalinds[0]],') and ',item2,' (Nutri-Score: ',lNutri[Finalinds[1]],')')

        ## assign cells for template
        # price
        prices              = list(C.lPrices)
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

    # friendly checks
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
        
        # save decision price and item in participant field for emotion elicitation later
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