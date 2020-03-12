# -*-coding:utf-8 -*-



from Heros import *
from Enemy import *
from Battle import *

def intertext():
    print("-"*60)

print("""
############################################################################################################################
#       Bienvenue dans le programme console.                                                                               #
#       Ce programme est mini-jeu sous forme de choix. A chaque fois, un choix vous est proposer. Pour continuer la suite  #
#       du jeu, entrez les différentes réponses (1, 2, 3 etc...).                                                          #
#--------------------------------------------------------------------------------------------------------------------------#
#           Auteur: Anthony VIOLET                                                                                         #
#           Date de création: 09-03-2020                                                                                   #
#           Modification: 09-03-2020                                                                                       #
############################################################################################################################
""")

begin = True
while begin:
    main = True
    """Boucle principal du programme"""
    print("""Vous êtes tranquille dans votre lit. Votre mère entre subitement et vous explique qu'elle a perdu son anneau en rentrant du marché dans le village de l'autre côté de la forêt. """)
    choix_begin = int(input("""
    1 Lui dire que vous avez peur d'aller dehors...
    2 Lui dire que la veille vous avez fais la fête et que vous êtes trop fatiguer pour sortir...
    """))
    if choix_begin == 1:
        discution_mere = True
        intertext()
        while discution_mere:
            print("""La mère vous rétorque que vous êtes le seul "Homme" de la maison et que vous devez prendre votre rôle à coeur et vous repropose d'aller chercher l'anneau""")
            choix_discution_mere = int(input("""
            1 Lui dire que vous avez trop peur de nouveau
            2 Lui dire que ça vous a regonfler a bloc et vous allez y aller
            """))
            if choix_discution_mere == 2:
                intertext()
                discution_mere = False
    if choix_begin == 2:
        intertext()
        print("La mère furieuse contre vous, vous met à la porte et vous avez perdu...")
        begin = False
        main = False

    if choix_begin == 9:
        intertext()
        print("""Choix spéciale. Combat !""")
        intertext()
        print("""Monstre est en combat avec héros !""")
        monstre = Enemy(5, 5, 20)
        heros = Heros(6, 8, 20)
        battle = Battle(heros, monstre)
        heros_def = False
        monstre_def = False
        degat_heros = 0
        degat_monstre = 0

        while monstre.hp > 0:
            intertext()
            print("""
            +++ Héros +++
            HP : {0}
            Atq : {1}
            Def : {2}
            +++ Monstre +++
            HP : {3}
            Atq : {4}
            Def : {5}
            """.format(heros.setHp(), heros.setAtk(), heros.setDef(), monstre.setHp(), monstre.setAtk(), monstre.setDef()))
            choix_cbt = int(input("""
            1 attaque
            2 défense
            3 fuite
            """))
            if choix_cbt == 1:
                intertext()
                degat_heros = battle.BatAttack(heros, monstre)
                print("""Le héros attaque le monstre ! degats : {0}""".format(degat_heros))
            if choix_cbt ==2:
                heros_def = True
            if choix_cbt == 3:
                print("""Vous prenez la fuite...""")
                monstre.hp = 0

            if monstre.hp > 0:
                intertext()
                if heros_def == True:
                    degat_monstre = battle.BatAttack(monstre, heros, True)
                else:
                    degat_monstre = battle.BatAttack(monstre, heros)
                print("""Le monstre attaque le héros ! degats : {0}""".format(degat_monstre))
            else:
                intertext()
                print("""Le monstre est mort !""")

            if heros.hp < 0:
                print("""Vous êtes mort...""")
                monstre.hp = 0
                begin = False
                main = False

    while main:
        intertext()
        print("""Vous passez la porte de l'entrée et vous retrouvez dehors sur le pas de la porte.""")
        choix_main = int(input("""
        1 Aller tout droit en direction de la forêt
        2 Aller à droite en direction de la grange
        3 Vous avez trop peur, vous rentrez
        """))
        if choix_main == 1:
            intertext()
            print("""Arriver devant l'entrée de la fôret, un homme en capuche ce poste devant vous et vous regarde fixement.""")
            choix_homme = int(input("""
            1 Lui demander si il n'a pas vu un anneau dans les environs
            2 Rebrousser chemin, cet homme à l'air louche...
            """))
            if choix_homme == 1:
                intertext()
                print("""Il vous indique en effet qu'il a trouver un anneau mais qu'il vous le donnera qu'en echange de 2 réponses""")
                choix_question = int(input("""
                1 Accepter
                2 Refuser
                """))
                if choix_question == 1:
                    intertext()
                    print("""l'homme souris, et pose alors la première question.
                    je suis noir, je deviens rouge, et je finis blanc. Qui sui-je ?""")
                    question_un = int(input("""
                    1 Un feu de camp
                    2 Du charbon
                    """))
                    if question_un == 1:
                        intertext()
                        print("""Mauvaise réponse... l'homme souris et disparait dans la forêt.""")
                        main = False
                        begin= False
                    if question_un == 2:
                        intertext()
                        print("""Bonne réponse ! l'homme souris et pose une seconde question. 
                        Quel est le plus gros chiffre au monde ?""")
                        question_deux =  int(input("""
                        1 100000000000000000000000000000000000000000000000000000000000
                        2 9
                        3 Il n'existe pas puisque il n'y a pas de limite...
                        """))
                        if question_deux == 1:
                            intertext()
                            print("""Mauvaise réponse... l'homme souris et disparait dans la forêt.""")
                            main = False
                            begin = False
                        if question_deux == 2:
                            intertext()
                            print("""l'Homme surpris, vous regarde fixement. Il disparait subitement et laisse a sa place un anneau. Celui de votre mère. Vous repartez lui rendre et vous avez gagner !""")
                            main = False
                            begin = False
                        if question_deux == 3:
                            intertext()
                            print("""Mauvaise réponse... l'homme souris et disparait dans la forêt.""")
                            main = False
                            begin = False
                if choix_question == 2:
                    intertext()
                    print("""l'homme souris et disparait dans la forêt.""")
                    main = False
                    begin = False

        if choix_main == 2:
            intertext()
            print("""Vous arrivez devant la porte de la grange.""")
            choix_porte_grange = int(input("""
            1 Ouvrir la porte de la grange
            2 Faire demi-tour
            """))
            if choix_porte_grange == 1:
                intertext()
                print("""Vous entrez dans la grange. Devant vous un tas de paille avec une fourche poser dessus.""")
                choix_grange = int(input("""
                1 Inspecter le tas de paille
                2 Faire demi-tour et sortir de la grange
                """))
                if choix_grange == 1:
                    intertext()
                    print("""Après une fouille rapide, il n'y a rien d'interessent et vous décidez de partir""")

        if choix_main == 3:
            intertext()
            print("""Vous avez trop peur, vous rentrez.
            
            Le lendemain...
            """)
            main = False
            begin = True

print("""
--
Fin du jeu.
--
""")
quit()