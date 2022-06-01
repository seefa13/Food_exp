from otree.api import *
import random

doc = """
In this app, participants will be asked follow-up questions and said 
good-bye.
"""


class C(BaseConstants):
    NAME_IN_URL = 'Outro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # image path for taste and health/risk attribute
    sImagePath          = 'global/figures/'
    # Create list of shuffled emotions for form fields
    Emotions            = ['Dull','Happy','Active','Unhappy','Energetic','Nervous','Calm','Secure','Passive','Blue','Enthusiastic','Tense']
    Shuffled_Emotions   = ['E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12']
    Shuffle_List        = []
    shuffle_count       = 0
    while shuffle_count<len(Emotions):
        randindex       = random.randint(0,len(Emotions)-1)
        while randindex in Shuffle_List:
            randindex   = random.randint(0,len(Emotions)-1)
        Shuffle_List.append(randindex)
        shuffle_count   = shuffle_count + 1
    emo_count = 0
    for index in Shuffle_List:
        Shuffled_Emotions = Shuffled_Emotions[:index]+[Emotions[emo_count]]+Shuffled_Emotions[index+1:]
        emo_count       = emo_count + 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Variables for Demographics
    D1 = models.StringField()
    D2 = models.StringField()
    D3 = models.StringField()
    D4 = models.StringField()
    D5 = models.StringField()
    D6 = models.StringField(blank=True)
    D7 = models.StringField(blank=True)
    D8 = models.StringField()
    D9 = models.StringField()
    

    # variables for Questionnaire
    QT1 = models.StringField()
    QT2 = models.StringField()
    QT3 = models.StringField()
    QT4 = models.StringField()
    QT5 = models.StringField()
    QT6 = models.StringField()
    QT7 = models.StringField()
    QT8 = models.StringField()
    QT9 = models.StringField()
    QT10 = models.StringField()
    QT11 = models.StringField()
    QT12 = models.StringField()
    QT13 = models.StringField()
    QT14 = models.StringField()
    # QT15 = models.StringField()
    # QT16= models.StringField()
    # QT17= models.StringField()
    # QT18= models.StringField()
    # QT19= models.StringField()
    # QT20= models.StringField()
    # QT21= models.StringField()
    # QT22 = models.StringField()
    # QT23 = models.StringField()
    # QT24= models.StringField()
    # QT25 = models.StringField()
    # QT26 = models.StringField()
    # QT27 = models.StringField()

    # Validation Questions
    V1 = models.StringField()
    V2 = models.StringField()

    # E-Mail address
    mail = models.StringField()

    # EQ
    Dull = models.BooleanField(
        blank = True,
        label = "Dull, Bored" 
    )
    Happy = models.BooleanField(
        blank = True,
        label = "Happy, Satisfied"
    )
    Active = models.BooleanField(
        blank = True,
        label = "Active, Alert"
    )
    Unhappy = models.BooleanField(
        blank = True,
        label = "Unhappy, Dissatisfied"
    )
    Energetic = models.BooleanField(
        blank = True,
        label = "Energetic, Excited"
    )
    Nervous = models.BooleanField(
        blank = True,
        label = "Jittered, Nervous"
    )
    Calm = models.BooleanField(
        blank = True,
        label = "Relaxed, Calm"
    )
    Secure = models.BooleanField(
        blank = True,
        label = "Secure, At ease"
    )
    Passive = models.BooleanField(
        blank = True,
        label = "Passive, Quiet"
    )
    Blue = models.BooleanField(
        blank = True,
        label = "Blue, Uninspired"
    )
    Enthusiastic = models.BooleanField(
        blank = True,
        label = "Enthusiastic, Inspired"
    )
    Tense = models.BooleanField(
        blank = True,
        label = "Tense, Bothered"
    )

# PAGES
class EQ_Intro(Page):
    def is_displayed(player):
        participant = player.participant
        bInvalidlen = participant.bInvalidlen
        return not bInvalidlen

class EQ_1(Page):
    @staticmethod
    def is_displayed(player):
        participant             = player.participant
        # choose randomly whether low (0) or high (1) risk item shown first
        bInvalidlen             = participant.bInvalidlen
        # import low and high risk food list if length of taste array is valid
        if not bInvalidlen:
            lNutri                  = participant.lNutri
            lSel_Items              = participant.lSel_Items
            EQ_order                = random.choice([0,1])
            participant.EQ_order    = EQ_order
            bShow                   = False
            score_count             = 0
            if EQ_order == 0:
                lLow                = []
                score_count         = 0
                for score in lNutri:
                    if score == 1:
                        lLow.append(score_count)
                    score_count     = score_count + 1
                for item in lSel_Items:
                    for lowitem in lLow:
                        if item == lowitem:
                            bShow  = True
            else:
                lHigh = []
                score_count         = 0
                for score in lNutri:
                    if score == 4 or score == 5:
                        lHigh.append(score_count)
                    score_count     = score_count + 1
                for item in lSel_Items:
                    for highitem in lHigh:
                        if item == highitem:
                            bShow  = True
        
        return bShow

    form_model = 'player'
    form_fields = C.Shuffled_Emotions

    def vars_for_template(player):
        participant         = player.participant
        lSel_Items          = participant.lSel_Items
        iTreat              = participant.iRisk_treat
        EQ_order            = participant.EQ_order
        lFoods              = participant.lFoods
        # import low and high risk food list
        lNutri                  = participant.lNutri
        lLow                = []
        score_count         = 0
        for score in lNutri:
            if score == 1:
                lLow.append(score_count)
            score_count     = score_count + 1
        lHigh               = []
        score_count         = 0
        for score in lNutri:
            if score == 4 or score == 5:
                lHigh.append(score_count)
            score_count     = score_count + 1
        # choose one item randomly and check whether it applies to the order condition
        if EQ_order == 0:
            randsel         = random.randint(0,len(lSel_Items)-1)
            randItem        = lSel_Items[randsel]
            while randItem not in lLow:
                randsel     = random.randint(0,len(lSel_Items)-1)
                randItem    = lSel_Items[randsel]
        else:
            randsel         = random.randint(0,len(lSel_Items)-1)
            randItem        = lSel_Items[randsel]
            while randItem not in lHigh:
                randsel     = random.randint(0,len(lSel_Items)-1)
                randItem    = lSel_Items[randsel]            
        item1           = lFoods[randItem]
        if iTreat == 0:
            info1             = C.sImagePath+'Nutri_'+str(lNutri[randItem])+'.png'
        else:
            info1             = C.sImagePath+'Risk_'+str(lNutri[randItem])+'.png'
        return dict(
            item1           = item1,
            info1           = info1,
            Treatment       = iTreat
        )


class EQ_2(Page):
    @staticmethod
    def is_displayed(player):
        participant         = player.participant
        bInvalidlen         = participant.bInvalidlen
        # import low and high risk food list if length of taste array is valid
        if not bInvalidlen:
            lNutri                  = participant.lNutri
            lSel_Items              = participant.lSel_Items
            EQ_order            = participant.EQ_order
            bShow               = False
            score_count         = 0
            if EQ_order == 1:
                lLow                = []
                score_count         = 0
                for score in lNutri:
                    if score == 1:
                        lLow.append(score_count)
                    score_count     = score_count + 1
                for item in lSel_Items:
                    for lowitem in lLow:
                        if item == lowitem:
                            bShow  = True
            else:
                lHigh = []
                for score in lNutri:
                    if score == 4 or score == 5:
                        lHigh.append(score_count)
                    score_count     = score_count + 1
                for item in lSel_Items:
                    for highitem in lHigh:
                        if item == highitem:
                            bShow  = True

        return bShow

    form_model              = 'player'
    form_fields             = C.Shuffled_Emotions

    def vars_for_template(player):
        participant         = player.participant
        lSel_Items          = participant.lSel_Items
        EQ_order            = participant.EQ_order
        iTreat              = participant.iRisk_treat
        lFoods              = participant.lFoods
        # import low and high risk food list
        lNutri                  = participant.lNutri
        lLow                = []
        score_count         = 0
        for score in lNutri:
            if score == 1:
                lLow.append(score_count)
            score_count     = score_count + 1
        lHigh               = []
        score_count         = 0
        for score in lNutri:
            if score == 4 or score == 5:
                lHigh.append(score_count)
            score_count     = score_count + 1
        # choose one item randomly and check whether it applies to the order condition
        if EQ_order == 1:
            randsel         = random.randint(0,len(lSel_Items)-1)
            randItem        = lSel_Items[randsel]
            while randItem not in lLow:
                randsel     = random.randint(0,len(lSel_Items)-1)
                randItem    = lSel_Items[randsel]
            item2           = lFoods[randItem]
        else:
            randsel         = random.randint(0,len(lSel_Items)-1)
            randItem        = lSel_Items[randsel]
            while randItem not in lHigh:
                randsel     = random.randint(0,len(lSel_Items)-1)
                randItem    = lSel_Items[randsel]            
            item2           = lFoods[randItem]
        if iTreat == 0:
            info2           = C.sImagePath+'Nutri_'+str(lNutri[randItem])+'.png'
        else:
            info2           = C.sImagePath+'Risk_'+str(lNutri[randItem])+'.png'
        return dict(
            item2           = item2,
            info2           = info2,
            Treatment       = iTreat
        )

class Outro_Q(Page):
    def is_displayed(player):
        participant = player.participant
        bInvalidlen = participant.bInvalidlen
        return not bInvalidlen

    form_model              = 'player'
    form_fields             = [
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 
        'QT1', 'QT2', 'QT3', 'QT4', 'QT5', 'QT6', 'QT7','QT8', 'QT9', 'QT10', 'QT11', 'QT12','QT13', 'QT14', 
        'V1','V2'
        ]

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant         = player.participant
        # validate questionnaire
        valid1              = int(int(player.V1)==2)
        valid2              = int(int(player.V2)==1)
        participant.validQuestionnaire = valid1 + valid2
        # calculate CR, EE and PA score if nothing went wrong, save NA otherwise
        try:
            CR_score        = (int(player.QT1)+int(player.QT2)+int(player.QT3)+int(player.QT4)+int(player.QT5)+int(player.QT6))/6
            EE_score        = (int(player.QT7)+int(player.QT8)+int(player.QT9))/3
            PA_score        = (int(player.QT10)+int(player.QT11)+int(player.QT12)+int(player.QT13))/4
        except: 
            CR_score        = 'NA'
            EE_score        = 'NA'
            PA_score        = 'NA'
        participant.CR_score = CR_score
        participant.EE_score = EE_score
        participant.PA_score = PA_score


class Goodbye(Page):
    def is_displayed(player):
        participant = player.participant
        bInvalidlen = participant.bInvalidlen
        return not bInvalidlen

    form_model              = 'player'
    form_fields             = ['mail']


class Exclude(Page):
    def is_displayed(player):
        participant = player.participant
        bInvalidlen = participant.bInvalidlen
        return bInvalidlen

page_sequence = [EQ_Intro, EQ_1, EQ_2, Outro_Q, Goodbye, Exclude]