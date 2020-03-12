# -*-coding:utf-8 -*-

class Heros:
    """Défini le héros et ses statistiques"""
    def __init__(self, atk, defense, hp):
        self.attack = int(atk)
        self.defense = int(defense)
        self.hp = int(hp)

    def setAtk(self):
        return self.attack

    def setDef(self):
        return self.defense

    def setHp(self):
        return self.hp

    def lessHp(self, value):
        self.hp -= value