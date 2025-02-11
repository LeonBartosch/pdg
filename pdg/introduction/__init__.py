from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'introduction'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.IntegerField(
        choices=[
            [1, 'Yes'],
            [0, 'No'],
        ],
        widget=widgets.RadioSelect
    )
    prolific_ID = models.StringField()


# PAGES
class gen_info_new(Page):
    pass

class info_consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def error_message(player, values):
        if values['consent'] == 0:
            return 'If you want to participate, you need to give your consent.'

class prolific_ID(Page):
    form_model = 'player'
    form_fields = ['prolific_ID']

class study_overview(Page):
    pass

page_sequence = [
    gen_info_new,
    info_consent,
    prolific_ID,
    study_overview,
]
