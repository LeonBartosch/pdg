from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(
        label='Please indicate your age in years.',
        min=18,max=99
    )
    gender = models.IntegerField(
        label='How do you describe yourself.',
        choices=[
            [0, 'Male'],
            [1, 'Female'],
            [2, 'Non-binary / third gender'],
            [3, 'Prefer not so say'],
        ],
        widget=widgets.RadioSelect
    )
    education = models.IntegerField(
        label='Please select the highest level of education you have completed.',
        choices=[
            [1, 'Elementary school '],
            [2, 'Middle school'],
            [3, 'High school '],
            [4, 'Undergrad college degree (Bachelor)'],
            [5, 'Graduate college degree or higher (Master, PhD, etc.)'],
        ],
        widget=widgets.RadioSelect
    )
    SES = models.IntegerField(
        label='',
        choices=[
            [10, '10: top of society'],
            [9, '9'],
            [8, '8'],
            [7, '7'],
            [6, '6'],
            [5, '5'],
            [4, '4'],
            [3, '3'],
            [2, '2'],
            [1, '1: Bottom of society'],
        ],
        widget=widgets.RadioSelect
    )
    pol_orient = models.IntegerField(
        label='In political matters, people talk of "the left" and "the right." How would you place your views on this scale, generally speaking?',
        choices=[
            [1, '1: Left'],
            [2, '2'],
            [3, '3'],
            [4, '4'],
            [5, '5'],
            [6, '6'],
            [7, '7'],
            [8, '8'],
            [9, '9'],
            [10, '10: Right'],
        ],
        widget=widgets.RadioSelect
    )
    local_institutional_authorities = models.IntegerField(
        label='Local institutional authorities',
        choices=[1,2,3,4,5,6,7],
        widget=widgets.RadioSelect
    )
    national_institutional_authorities = models.IntegerField(
        label='National institutional authorities',
        choices=[1,2,3,4,5,6,7],
        widget=widgets.RadioSelect
    )
    national_legal_system = models.IntegerField(
        label='The national legal system',
        choices=[1,2,3,4,5,6,7],
        widget=widgets.RadioSelect
    )
    national_political_system = models.IntegerField(
        label='The national political system',
        choices=[1,2,3,4,5,6,7],
        widget=widgets.RadioSelect
    )
    feedback = models.LongStringField(
        blank=True,
        label="Finally, if you wish, you have the opportunity to express any thoughts about this survey."
    )
    prolific_ID_copy = models.StringField(
        label="Please enter your Prolific ID."
    )


# PAGES
class demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', 'SES', 'pol_orient', 'local_institutional_authorities', 'national_institutional_authorities', 'national_legal_system', 'national_political_system', 'feedback']
    pass

class prolific_ID(Page):
    form_model = 'player'
    form_fields = ['prolific_ID_copy']

class debriefing(Page):
    pass


class redirect_prolific(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player):
        return True  # Zeige die Seite allen Teilnehmern

    @staticmethod
    def js_vars(player):
        return dict(
            completionlink=player.session.config.get('completionlink', 'https://app.prolific.com')  # Fallback-URL
        )
    pass



page_sequence = [
    demographics,
    prolific_ID,
    debriefing,
    redirect_prolific,
]
