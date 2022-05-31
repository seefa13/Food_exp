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
    # working data
    'lFoods','lTastes','lNutri','lPrevcomb','Foods_sel','practice_item','practice_price1','practice_price2',
    'practice_price','EQ_order','lTaste_A','lTaste_BC','lTaste_DE','lTaste_A_ind','lTaste_BC_ind','lTaste_DE_ind',
    'lFoods_A','lFoods_BC','lFoods_DE','invalidlen',
    # friendly checks
    'dTimeOutFocus','iOutFocus','iFullscreenChanges','dPixelRatio','bRequireFS','bCheckFocus','startTime',
    # selected trial
    'SelectedTrial','lSel_Items',
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
