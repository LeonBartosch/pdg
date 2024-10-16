from otree.api import *


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
    PD_tran = models.IntegerField()
    PD_exp = models.IntegerField()
    MC_tran = models.IntegerField()
    MC_exp = models.IntegerField()
    ingroup = models.StringField()
    distance = models.StringField()


# PAGES
class pdg(Page):
    pass

class manipulation_check(Page):
    pass


page_sequence = [
    pdg,
    manipulation_check
]
