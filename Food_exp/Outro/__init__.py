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
    mail = models.StringField(blank = True)

    # EQ
    Dull = models.BooleanField(
        blank = True,
        label = "Dull, Bored",
        initial = 0
    )
    Happy = models.BooleanField(
        blank = True,
        label = "Happy, Satisfied",
        initial = 0
    )
    Active = models.BooleanField(
        blank = True,
        label = "Active, Alert",
        initial = 0
    )
    Unhappy = models.BooleanField(
        blank = True,
        label = "Unhappy, Dissatisfied",
        initial = 0
    )
    Energetic = models.BooleanField(
        blank = True,
        label = "Energetic, Excited",
        initial = 0
    )
    Nervous = models.BooleanField(
        blank = True,
        label = "Jittered, Nervous",
        initial = 0
    )
    Calm = models.BooleanField(
        blank = True,
        label = "Relaxed, Calm",
        initial = 0
    )
    Secure = models.BooleanField(
        blank = True,
        label = "Secure, At ease",
        initial = 0
    )
    Passive = models.BooleanField(
        blank = True,
        label = "Passive, Quiet",
        initial = 0
    )
    Blue = models.BooleanField(
        blank = True,
        label = "Blue, Uninspired",
        initial = 0
    )
    Enthusiastic = models.BooleanField(
        blank = True,
        label = "Enthusiastic, Inspired",
        initial = 0
    )
    Tense = models.BooleanField(
        blank = True,
        label = "Tense, Bothered",
        initial = 0
    )


# PAGES
class EQ(Page):
    @staticmethod
    def is_displayed(player):
        participant                 = player.participant
        bInvalidlen                 = participant.bInvalidlen

        # import low and high risk food list if length of taste array is valid
        lNutri                  = participant.lNutri
        lSel_Items              = participant.lSel_Items
        bShow                   = False
        score_count             = 0
        EQ_lowhigh              = random.choice(['low','high'])
        print('The participant sees a ',EQ_lowhigh,' risk product.')
        participant.EQ_lowhigh  = EQ_lowhigh

        # aggregate decisions in low (Nutri = 1) and high (Nutri = 4 || Nutri = 5) risk food lists
        if EQ_lowhigh == 'low':
            lLow                = []
            score_count         = 0
            for score in lNutri:
                if score == 1:
                    lLow.append(score_count)
                score_count     = score_count + 1
            participant.lLow    = lLow
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
            participant.lHigh    = lHigh
            for item in lSel_Items:
                for highitem in lHigh:
                    if item == highitem:
                            bShow   = True

        return bShow and not bInvalidlen

    form_model = 'player'
    form_fields = random.sample(C.Emotions,len(C.Emotions))

    @staticmethod
    def vars_for_template(player):
        participant         = player.participant
        lSel_Items          = participant.lSel_Items
        iTreat              = participant.iRisk_treat
        lFoods              = participant.lFoods
        lNutri              = participant.lNutri
        EQ_lowhigh          = participant.EQ_lowhigh
        
        # choose one item randomly and check whether it applies to the order condition
        if EQ_lowhigh == 'low':
            lLow                = participant.lLow
            randsel         = random.randint(0,len(lSel_Items)-1)
            randItem        = lSel_Items[randsel]
            while randItem not in lLow:
                randsel     = random.randint(0,len(lSel_Items)-1)
                randItem    = lSel_Items[randsel]
        else:
            lHigh               = participant.lHigh
            randsel         = random.randint(0,len(lSel_Items)-1)
            randItem        = lSel_Items[randsel]
            while randItem not in lHigh:
                randsel     = random.randint(0,len(lSel_Items)-1)
                randItem    = lSel_Items[randsel]            
        item1               = lFoods[randItem]
        if iTreat == 0:
            info1             = C.sImagePath+'Nutri_'+str(lNutri[randItem])+'.png'
        else:
            info1             = C.sImagePath+'Risk_'+str(lNutri[randItem])+'.png'
        return dict(
            item1           = item1,
            info1           = info1,
            Treatment       = iTreat
        )


class Outro_Q(Page):
    @staticmethod
    def is_displayed(player):
        participant = player.participant
        bInvalidlen = participant.bInvalidlen
        return not bInvalidlen

    form_model              = 'player'
    form_fields             = [
        'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8','D9',
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
    @staticmethod
    def is_displayed(player):
        participant = player.participant
        bInvalidlen = participant.bInvalidlen
        return not bInvalidlen

    form_model              = 'player'
    form_fields             = ['mail']


class Exclude(Page):
    @staticmethod
    def is_displayed(player):
        participant = player.participant
        bInvalidlen = participant.bInvalidlen
        return bInvalidlen

page_sequence = [EQ, Outro_Q, Goodbye, Exclude]