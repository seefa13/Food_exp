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
    Emotions_1            = ['Dull1','Happy1','Active1','Unhappy1','Energetic1','Nervous1','Calm1','Secure1','Passive1','Blue1','Enthusiastic1','Tense1']
    Emotions_2            = ['Dull2','Happy2','Active2','Unhappy2','Energetic2','Nervous2','Calm2','Secure2','Passive2','Blue2','Enthusiastic2','Tense2']    


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

    # EQ_1
    Dull1 = models.BooleanField(
        blank = True,
        label = "Dull, Bored" 
    )
    Happy1 = models.BooleanField(
        blank = True,
        label = "Happy, Satisfied"
    )
    Active1 = models.BooleanField(
        blank = True,
        label = "Active, Alert"
    )
    Unhappy1 = models.BooleanField(
        blank = True,
        label = "Unhappy, Dissatisfied"
    )
    Energetic1 = models.BooleanField(
        blank = True,
        label = "Energetic, Excited"
    )
    Nervous1 = models.BooleanField(
        blank = True,
        label = "Jittered, Nervous"
    )
    Calm1 = models.BooleanField(
        blank = True,
        label = "Relaxed, Calm"
    )
    Secure1 = models.BooleanField(
        blank = True,
        label = "Secure, At ease"
    )
    Passive1 = models.BooleanField(
        blank = True,
        label = "Passive, Quiet"
    )
    Blue1 = models.BooleanField(
        blank = True,
        label = "Blue, Uninspired"
    )
    Enthusiastic1 = models.BooleanField(
        blank = True,
        label = "Enthusiastic, Inspired"
    )
    Tense1 = models.BooleanField(
        blank = True,
        label = "Tense, Bothered"
    )

    # EQ_2
    Dull2 = models.BooleanField(
        blank = True,
        label = "Dull, Bored" 
    )
    Happy2 = models.BooleanField(
        blank = True,
        label = "Happy, Satisfied"
    )
    Active2 = models.BooleanField(
        blank = True,
        label = "Active, Alert"
    )
    Unhappy2 = models.BooleanField(
        blank = True,
        label = "Unhappy, Dissatisfied"
    )
    Energetic2 = models.BooleanField(
        blank = True,
        label = "Energetic, Excited"
    )
    Nervous2 = models.BooleanField(
        blank = True,
        label = "Jittered, Nervous"
    )
    Calm2 = models.BooleanField(
        blank = True,
        label = "Relaxed, Calm"
    )
    Secure2 = models.BooleanField(
        blank = True,
        label = "Secure, At ease"
    )
    Passive2 = models.BooleanField(
        blank = True,
        label = "Passive, Quiet"
    )
    Blue2 = models.BooleanField(
        blank = True,
        label = "Blue, Uninspired"
    )
    Enthusiastic2 = models.BooleanField(
        blank = True,
        label = "Enthusiastic, Inspired"
    )
    Tense2 = models.BooleanField(
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
        participant                 = player.participant
        # choose randomly whether low (0) or high (1) risk item shown first
        bInvalidlen                 = participant.bInvalidlen
        # import low and high risk food list if length of taste array is valid
        if not bInvalidlen:
            lNutri                  = participant.lNutri
            lSel_Items              = participant.lSel_Items
            EQ_order                = random.choice([0,1])
            print('The order is ',EQ_order)
            participant.EQ_order    = EQ_order
            bShow                   = False
            score_count             = 0

            # aggregate decisions in low (Nutri = 1) and high (Nutri = 4 || Nutri = 5) risk food lists
            lLow                = []
            score_count         = 0
            for score in lNutri:
                if score == 1:
                    lLow.append(score_count)
                score_count     = score_count + 1
            for item in lSel_Items:
                for lowitem in lLow:
                    if item == lowitem:
                        bShow_low  = True
            participant.bShow_low = bShow_low
            participant.lLow            = lLow
            
            lHigh = []
            score_count         = 0
            for score in lNutri:
                if score == 4 or score == 5:
                    lHigh.append(score_count)
                score_count     = score_count + 1
            for item in lSel_Items:
                for highitem in lHigh:
                    if item == highitem:
                            bShow_high   = True
            participant.bShow_high      = bShow_high
            participant.lHigh           = lHigh
            if EQ_order == 0:
                bShow = bShow_low
            else:
               bShow = bShow_high
        
        return bShow

    Shuffled_Emotions_1   = random.sample(C.Emotions_1,len(C.Emotions_1))

    form_model = 'player'
    form_fields = Shuffled_Emotions_1

    def vars_for_template(player):
        participant         = player.participant
        lSel_Items          = participant.lSel_Items
        iTreat              = participant.iRisk_treat
        EQ_order            = participant.EQ_order
        lFoods              = participant.lFoods
        lLow                = participant.lLow
        lHigh               = participant.lHigh
        lNutri              = participant.lNutri
        
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
            EQ_order = participant.EQ_order
            if EQ_order == 1:
                bShow = participant.bShow_low
            else:
                bShow = participant.bShow_high

        return bShow

    Shuffled_Emotions_2   = random.sample(C.Emotions_2,len(C.Emotions_2))

    form_model              = 'player'
    form_fields             = Shuffled_Emotions_2

    def vars_for_template(player):
        participant         = player.participant
        lSel_Items          = participant.lSel_Items
        EQ_order            = participant.EQ_order
        iTreat              = participant.iRisk_treat
        lFoods              = participant.lFoods
        # import low and high risk food list
        lNutri                  = participant.lNutri
        lLow                = participant.lLow
        lHigh               = participant.lHigh

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