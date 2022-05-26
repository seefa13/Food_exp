from otree.api import *


doc = """
In this app, participants will be asked follow-up questions and said 
good-bye.
"""


class C(BaseConstants):
    NAME_IN_URL = 'Outro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


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
    QT11= models.StringField()
    QT12= models.StringField()
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
    mail = models.StringField


# PAGES
class Outro_Q(Page):
    form_model = 'player'
    form_fields = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 
    'QT1', 'QT2', 'QT3', 'QT4', 'QT5', 'QT6', 'QT7','QT8', 'QT9', 'QT10', 'QT11', 'QT12','QT13', 'QT14', 
    'V1','V2']

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        # validate questionnaire
        valid1 = int(int(player.V1)==2)
        valid2 = int(int(player.V2)==1)
        participant.validQuestionnaire = valid1 + valid2
        # calculate CR, EE and PA score if nothing went wrong, save NA otherwise
        try:
            CR_score = (int(player.QT1)+int(player.QT2)+int(player.QT3)+int(player.QT4)+int(player.QT5)+int(player.QT6))/6
            EE_score = (int(player.QT7)+int(player.QT8)+int(player.QT9))/3
            PA_score = (int(player.QT10)+int(player.QT11)+int(player.QT12)+int(player.QT13))/4
        except: 
            CR_score = 'NA'
            EE_score = 'NA'
            PA_score = 'NA'
        participant.CR_score = CR_score
        participant.EE_score = EE_score
        participant.PA_score = PA_score



class Goodbye(Page):
    form_model = 'player'
    form_fields = ['mail']


page_sequence = [Outro_Q, Goodbye]
