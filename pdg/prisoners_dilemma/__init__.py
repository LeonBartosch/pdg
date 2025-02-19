from cProfile import label

from otree.api import *
from otree.forms.widgets import RadioSelectHorizontal, RadioSelect

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'prisoners_dilemma'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    PD_tran = models.IntegerField(
        label="How many Talers would you like to transfer to this person?",
        choices=[0, 1, 2, 3, 4, 5],
        widget=RadioSelectHorizontal
    )
    PD_exp = models.IntegerField(
        label="How many Talers do you think this person will transfer to you?",
        choices=[0, 1, 2, 3, 4, 5],
        widget=RadioSelectHorizontal
    )
    MC_main = models.IntegerField(
        label="How strongly do you feel that your outcomes depend on the choices of the other person?",
        choices=[
            [1, '1 - Not at all'],
            [2, '2 - Slightly'],
            [3, '3 - Somewhat'],
            [4, '4 - Very much'],
            [5, '5 - Completely']
        ],
        widget=RadioSelect
    )
    MC_expl = models.IntegerField(
        label="How socially close do you feel to the other person in the context of this study?",
        choices=[
            [1, '1 - Not at all'],
            [2, '2 - Slightly'],
            [3, '3 - Somewhat'],
            [4, '4 - Very much'],
            [5, '5 - Completely']
        ],
        widget=RadioSelect
    )
    ingroup = models.StringField()
    distance = models.StringField()


# PAGES
class pdg(Page):
    form_model = 'player'
    form_fields = ['PD_tran', 'PD_exp']

    @staticmethod
    def vars_for_template(player):
        ingroup = ['ingroup', 'ingroup', 'outgroup', 'outgroup']
        distance = ['close', 'distant', 'close', 'distant']
        player.ingroup = ingroup[player.participant.order[player.round_number-1]]
        player.distance = distance[player.participant.order[player.round_number-1]]

        if player.ingroup == "ingroup":
            other_color = player.participant.color
        else:
            if player.participant.color == "blue":
                other_color = "orange"
            else:
                other_color = "blue"

        image_path = "PD_" + player.participant.color + "_" + player.distance + "_" + other_color + ".png"

        return dict(
            other_color = other_color,
            image_path = image_path
        )

class manipulation_check(Page):
    form_model = 'player'
    form_fields = ['MC_main', 'MC_expl']


page_sequence = [
    pdg,
    manipulation_check
]
