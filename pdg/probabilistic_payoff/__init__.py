from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'probabilistic_payoff'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    comprehension_check_1 = models.BooleanField(blank=True, label="Socially close others have a higher probability of being selected for the final bonus payment.")
    comprehension_check_2 = models.BooleanField(blank=True, label="Socially distant others have a higher probability of being selected for the final bonus payment.")
    comprehension_check_3 = models.BooleanField(blank=True, label="Members from the same group have a higher probability of being selected for the final bonus payment.")
    comprehension_check_4 = models.BooleanField(blank=True, label="Members from a different group have a higher probability of being selected for the final bonus payment.")
    comprehension_check_5 = models.BooleanField(blank=True, label="The calculation of the bonus is reciprocal, meaning the same rules for your bonus payment also apply to the bonus payment of the other person.")
    comprehension_check_6 = models.BooleanField(blank=True, label="The calculation of the bonus is not reciprocal, meaning the same rules for your bonus payment do not apply to the bonus payment of the other person.")
    comprehension_check_counter = models.IntegerField(initial=0)

# PAGES
class general_instruction(Page):
    @staticmethod
    def vars_for_template(player):
        if player.participant.color == "blue":
            other_color = "orange"
        else:
            other_color = "blue"
        return dict(
            other_color=other_color,
            image_path='gen_intro_{}.png'.format(player.participant.color)
        )

class instruction_probabilistic(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            image_path='prob_intro_{}.png'.format(player.participant.color)
        )

class comprehension_check(Page):
    form_model = 'player'
    form_fields = ['comprehension_check_1', 'comprehension_check_2', 'comprehension_check_3', 'comprehension_check_4', 'comprehension_check_5', 'comprehension_check_6']

    @staticmethod
    def error_message(player, values):
        if not (values['comprehension_check_1'] and not values['comprehension_check_2'] and not values['comprehension_check_3'] and not values['comprehension_check_4'] and values['comprehension_check_5'] and not values['comprehension_check_6']):
            player.comprehension_check_counter = player.comprehension_check_counter + 1
            return 'Please reconsider your answer. Remember that <br> - Socially close others impact your bonus payment more. <br> - Group membership does not matter. <br> - Rules apply for the other person as well.'

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        return "prisoners_dilemma"



page_sequence = [
    general_instruction,
    instruction_probabilistic,
    comprehension_check
]
