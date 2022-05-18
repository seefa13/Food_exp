from otree.api import *
import time
import random


doc = """
This app contains a gernal introduction to otree and the task.
"""

#FUNCTIONS
# initialize treatments and counter variables
def creating_session(subsession):
    iHealth = [0, 1, 2] # 0 is baseline, 1 is risk label, 2 is concrete risk
    if subsession.round_number == 1:
        for player in subsession.get_players():

            # assign treatments
            participant                     = player.participant
            participant.iRisk_treat         = random.choice(iHealth)



class C(BaseConstants):
    NAME_IN_URL         = 'Intro'
    PLAYERS_PER_GROUP   = None
    NUM_ROUNDS          = 1
    UvA_logo            = 'global/figures/UvA_logo.png'
    thumb_symbol        = 'global/figures/thumb_symbol.png'
    health_symbol       = 'global/figures/health_symbol.png'
    risk_symbol         = 'global/figures/risk_symbol.png'
    intro_choose        = 'global/figures/intro_choose.png'
    AvgDur              = "10-15"
    PaidParts           = "20"
    Endowment           = "5€"
    NumTrials           = "6"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Q1          = models.IntegerField(
        label   = "Will every of your decision be paid out?",
        choices = [
            [1, 'Yes, I will receive every food decision of every round.'],
            [2, 'Yes, I will receive one food item from one randomly selected trial for sure.'],
            [3, 'No, I will receive one food item from one randomly selected trial if I am one of the randomly selected participants for payout.'],
            [4, 'Yes, I will receive every food decision of every round if I am one of the randomly selected participants for payout.']
    ]
)

    Q2          = models.IntegerField(
        label   = "If selected for payout, how large would your payout be?",
        choices = [
            [1, '5€'],
            [2, '5€ - the price of the food item + the food item.'],
            [3, '5€ + the food item.']
    ]
)

    Q3_health   = models.IntegerField(
        label   = "Please select the food item with the best health score (=healthiest food item).",
        choices = [
            [1, 'B'],
            [2, 'A'],
            [3, 'E'],
            [4, 'D'],
            [5, 'C'],
    ]
)

    Q3_risk     = models.IntegerField(
        label   = "Please select the food item with the best risk score (=healthiest food item).",
        choices = [
            [1, '1 out of 5'],
            [2, '3 out of 5'],
            [3, '4 out of 5'],
            [4, '2 out of 5'],
            [5, '5 out of 5'],
    ]
    )
    dPixelRatio = models.FloatField()

# PAGES
class Intro_Exp(Page):
    form_model          = "player"
    form_fields         = ["Q1","Q2","Q3_health","Q3_risk"]

    @staticmethod
    def vars_for_template(player: Player):
        participant     = player.participant
        return dict(
            Treatment   = participant.iRisk_treat,
            OutFocus = participant.iOutFocus
        )
    
    #@staticmethod
    def get_form_fields(player):
        participant     = player.participant
        if participant.iRisk_treat == 0:
            return ["Q1","Q2","Q3_health"]
        else:
            return ["Q1","Q2","Q3_risk"]
        
    @staticmethod
    def error_message(player, values):
        participant         = player.participant
        if participant.iRisk_treat == 0:
            solutions       = dict(
                Q1          = 3,
                Q2          = 2,
                Q3_health   = 2
            )
        else:
            solutions   = dict(
                Q1      = 3,
                Q2      = 2,
                Q3_risk = 1
            )

        error_messages  = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Wrong answer'

        return error_messages
    
    @staticmethod
    def js_vars(player: Player):
        session = player.session
        p = player.participant
        return {
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'dPixelRatio'       : p.dPixelRatio,
        }


class Intro_Task(Page):
    @staticmethod
    def js_vars(player: Player):
        session = player.session
        p = player.participant
        return {
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'dPixelRatio'       : p.dPixelRatio,
        }

class Intro_Choose(Page):
    @staticmethod
    def js_vars(player: Player):
        session = player.session
        p = player.participant
        return {
            'bRequireFS'        : session.config['bRequireFS'],
            'bCheckFocus'       : session.config['bCheckFocus'],
            'dPixelRatio'       : p.dPixelRatio,
        }


class Intro_General(Page):
    @staticmethod
    def vars_for_template(player):

        return dict(
            UvA_logo = C.UvA_logo
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        part = player.participant
        # Initialize Focus variables        
        part.startTime          = time.time()
        part.iOutFocus          = 0
        part.iFullscreenChanges = 0
        part.dTimeOutFocus      = 0
        
class Intro_Consent(Page):
    pass

class Calibration(Page):
    form_model              = 'player'
    form_fields             = [ 'dPixelRatio' ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        part                = player.participant
        part.dPixelRatio    = player.dPixelRatio


page_sequence = [Intro_General, Intro_Consent, Calibration, Intro_Exp, Intro_Task, Intro_Choose]