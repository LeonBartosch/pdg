from cProfile import label

from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'pdg'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    PDG_control1 = models.IntegerField(
        label='What is your bonus payment if you transfer 100 Talers to Person B and Person B also transfers 100 Talers to you?',
        choices=[
            [1, '0 Talers'],
            [2, '100 Talers'],
            [3, '200 Talers'],
            [4, '300 Talers'],
        ],
        widget=widgets.RadioSelect
    )
    PDG_control2 = models.IntegerField(
        label='What is your bonus payment if you transfer 0 Talers to Person B and Person B transfers 100 Talers to you?',
        choices=[
            [1, '0 Talers'],
            [2, '100 Talers'],
            [3, '200 Talers'],
            [4, '300 Talers'],
        ],
        widget=widgets.RadioSelect
    )
    PDG_control3 = models.IntegerField(
        label='What is your bonus payment if you transfer 100 Talers to Person B and Person B transfers 0 Talers to you?',
        choices=[
            [1, '0 Talers'],
            [2, '100 Talers'],
            [3, '200 Talers'],
            [4, '300 Talers'],
        ],
        widget=widgets.RadioSelect
    )
    PDG_control4 = models.IntegerField(
        label='What is your bonus payment if you transfer 0 Talers to Person B and Person B also transfers 0 Talers to you?',
        choices=[
            [1, '0 Talers'],
            [2, '100 Talers'],
            [3, '200 Talers'],
            [4, '300 Talers'],
        ],
        widget=widgets.RadioSelect
    )
    PDG_control5 = models.IntegerField(
        label='If you estimate that Person B transferred 40 Talers to you, how much would your bonus payment be if your estimation is incorrect and Person B actually transferred 30 Talers to you (given that the estimations determine your bonus payment)?',
        choices=[
            [1, '0 Talers'],
            [2, '60 Talers'],
            [3, '190 Talers'],
            [4, '400 Talers'],
        ],
        widget=widgets.RadioSelect
    )


# PAGES
class PDG_intro1(Page):
    pass

class PDG_intro2(Page):
    pass

class PDG_intro3(Page):
    pass

class PDG_intro4(Page):
    pass

class PDG_intro5(Page):
    pass

class PDG_intro6(Page):
    pass

class PDG_intro7(Page):
    pass

class PDG_intro8(Page):
    pass

class PDG_intro9(Page):
    pass

class PDG_intro10(Page):
    pass

class PDG_control1(Page):
    form_model = 'player'
    form_fields = ['PDG_control1']

    @staticmethod
    def error_message(player, values):
        if values['PDG_control1'] != 3:
            return 'Please reconsider your answer.'

class PDG_control2(Page):
    form_model = 'player'
    form_fields = ['PDG_control2']

    @staticmethod
    def error_message(player, values):
        if values['PDG_control2'] != 4:
            return 'Please reconsider your answer.'

class PDG_control3(Page):
    form_model = 'player'
    form_fields = ['PDG_control3']

    @staticmethod
    def error_message(player, values):
        if values['PDG_control3'] != 1:
            return 'Please reconsider your answer.'

class PDG_control4(Page):
    form_model = 'player'
    form_fields = ['PDG_control4']

    @staticmethod
    def error_message(player, values):
        if values['PDG_control4'] != 2:
            return 'Please reconsider your answer.'

class PDG_control5(Page):
    form_model = 'player'
    form_fields = ['PDG_control5']

    @staticmethod
    def error_message(player, values):
        if values['PDG_control5'] != 3:
            return 'Please reconsider your answer.'

class PDG_done(Page):
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        import random

        player.participant.condition = random.choice(['weighted', 'probabilistic'])
        player.participant.ingroup = random.choice(['blue', 'green'])

        if player.participant.condition == 'weighted':
            return "weighted_payoff"
        else:
            return "probabilistic_payoff"


page_sequence = [
    PDG_intro1,
    PDG_intro2,
    PDG_intro3,
    PDG_intro4,
    PDG_intro5,
    PDG_intro6,
    PDG_intro7,
    PDG_intro8,
    PDG_intro9,
    PDG_intro10,
    PDG_control1,
    PDG_control2,
    PDG_control3,
    PDG_control4,
    PDG_control5,
    PDG_done,
]
