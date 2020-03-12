# -*-coding:utf-8 -*-

class Battle:
    """Système de combat.
    calcule de dégats : ATTAQUE - (ATTAQUE divisé par DEFENSE(enemis))
    """
    def __init__(self, heros, enemy):
        self.enemy = enemy
        self.heros = heros

    def BatAttack(self, attacker, defender, defense=False):
        degat = attacker.setAtk() - (attacker.setAtk() / defender.setDef())
        if defense:
            degat /= 2
        defender.lessHp(degat)
        return degat

    def defense(self, target):
        return True