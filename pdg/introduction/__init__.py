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
    prolific_id = models.StringField(default=str(" "))




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

class study_overview(Page):
    form_model = 'player'

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.prolific_id = player.participant.label

    pass



class bonus_info(Page):
    pass

page_sequence = [
    gen_info_new,
    info_consent,
    study_overview,
    bonus_info,
]
