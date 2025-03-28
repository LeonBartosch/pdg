from os import environ

ROOMS = [
    dict(
        name='prolific',
        display_name='Prolific Study',
        # use_secure_urls=True,  # Falls du sichere Links nutzen willst
    ),
]

SESSION_CONFIGS = [
    dict(
        name='pdg',
        app_sequence=[
            'introduction',
            'pdg',
            'probabilistic_payoff',
            'weighted_payoff',
            'prisoners_dilemma',
            'demographics'
        ],
        num_demo_participants=1,
        completionlink=
        'https://app.prolific.com/submissions/complete?cc=CCFT75WO',
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [ 'prolific_id','condition', 'color', 'order']
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

SECRET_KEY = '5111371681270'
