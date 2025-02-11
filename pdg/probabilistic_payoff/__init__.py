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
    pass


# PAGES
class general_instruction(Page):
    pass

class instruction_probabilistic(Page):
    pass



page_sequence = [
    general_instruction,
    instruction_probabilistic
]
