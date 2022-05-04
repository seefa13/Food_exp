from os import environ

SESSION_CONFIGS = [
    dict(
    name='Food_exp',
    display_name = 'Food Choice Experiment',
    app_sequence=['Intro', 'Foods', 'Taste', 'Same', 'Different', 'Outro'],
    num_demo_participants=3,
    ),
    dict(
    name='Intro',
    display_name = 'Intro',
    app_sequence=['Intro'],
    num_demo_participants=3,
    ),
    dict(
    name='Main',
    display_name = 'Main',
    app_sequence=['Foods', 'Taste', 'Same', 'Different'],
    num_demo_participants=3,
    ),
    dict(
    name='Choices',
    display_name = 'Choices',
    app_sequence=['Same', 'Different'],
    num_demo_participants=3,
    ),
    dict(
    name='Outro',
    display_name = 'Outro',
    app_sequence=['Outro'],
    num_demo_participants=3,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['risk_treat']
SESSION_FIELDS = []

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
