from os import environ

SESSION_CONFIGS = [
    dict(
        name='Food_exp_config',
        display_name = 'Food Choice Experiment',
        app_sequence=['Intro', 'Taste', 'Choice_Task', 'Outro'],
        num_demo_participants=3,
        iTimeOut=0,
        bRequireFS=True,
        bCheckFocus=True,
    ),
        dict(
        name='Intro',
        display_name = 'Intro',
        app_sequence=['Intro'],
        num_demo_participants=3,
        iTimeOut=0,
        bRequireFS=True,
        bCheckFocus=True,
    ),
        dict(
        name='Main',
        display_name = 'Main',
        app_sequence=['Taste', 'Choice_Task'],
        num_demo_participants=3,
        iTimeOut=0,
        bRequireFS=True,
        bCheckFocus=True,
    ),
        dict(
        name='Choices',
        display_name = 'Choices',
        app_sequence=['Choice_Task'],
        num_demo_participants=3,
        iTimeOut=0,
        bRequireFS=True,
        bCheckFocus=True,
    ),
        dict(
        name='Outro',
        display_name = 'Outro',
        app_sequence=['Outro'],
        num_demo_participants=3,
        iTimeOut=0,
        bRequireFS=True,
        bCheckFocus=True,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    # treatment
    'iRisk_treat',
    # food lists
    'lFoods','lFoods_A','lFoods_BC','lFoods_DE','lFoods_B','lFoods_C','lFoods_D','lFoods_E',
    # nutri score
    'lNutri',
    # taste list
    'lTastes',
    # working data
    'randCombs','practice_item','practice_price1','practice_price2','practice_price','sEQ_lowhigh','lLowHigh',
    # indeces by comparison
    'lInds_AvBC_small','lInds_AvBC_largeal','lInds_AvBC_largenal',
    'lInds_AvDE_small','lInds_AvDE_largeal','lInds_AvDE_largenal',
    'lInds_BCvDE_small','lInds_BCvDE_largeal','lInds_BCvDE_largenal',
    'lInds_BvC_largenal','lInds_DvE_largenal',
    # content checks
    'bInvalidlen',
    # friendly checks
    'dTimeOutFocus','iOutFocus','iFullscreenChanges','dPixelRatio','bRequireFS','bCheckFocus','startTime',
    # selected food items
    'lSel_Items','lFoods_sel','lLow','lHigh',
    # validations and controls
    'validQuestionnaire','validTasteQ','CR_score','EE_score','PA_score'
    ]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1644748491042'
