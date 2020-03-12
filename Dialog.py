# -*-coding:utf-8 -*-

from lxml import etree

class Dialog:
    """Défini le choix et texte affichés à l'ecran"""
    def __init__(self):
        self.tree = etree.parse("data/dialog.xml")

    def display(self, id):
        for line in self.tree.xpath("/dialogs/"+ id +"/text"):
            print(line.text)

    def choice(self, id):
        for line in self.tree.xpath("/dialogs/"+ id +"/choice"):
            return int(input(line.text))