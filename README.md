It's a simple command line RPG.
the program algorithm is detailed in <cahierDesCharges> file. 
There are 4 class in this program : 
1: The Dialogs class. list the dialogs and display it
2 : The Heros class. create and manage hero stats
3 : The Enemy class. create and manage enemy stats
4 : The Battle class. create a fight and manage the deroulment. 

this program is very good for beginner in python. 

Algorithm of this program :
FRENCH
#############################################################################
# Cahier des charges pour un petit jeu simple. Le bu étant de récupérer un  #
# anneau pour sa mère et de lui ramené. Bien sûre, l'anneau est au bout de  #
# la map et garder par un homme masqué. Il faut pour cela repondre a 2      #
# questions Biensûre si les réponses sont fausse, il ne donne pas l'anneau. #
#############################################################################

Déroulement du programme :

- La mère vous interpelle est explique qu'elle a perdu son anneau en rentrant du marché dans le village
  de l'autre côté de la forêt.
---- 1 Lui proposer  d'aller chercher l'anneau
        |-> suite du programme
---- 2 Lui dire que vous avez peur d'aller dehors
        |-> La mère vous rétorque que vous êtes le seul "Homme" de la maison et que
        |   vous devez prendre votre rôle à coeur et vous repropose d'aller chercher
        |   l'anneau
        |-------- 1 Lui dire que vous avez trop peur de nouveau
                    |-> retour à la phrase précédente de la mère
        |-------- 2 Lui dire que ça vous a regonfler a bloc et vous allez y aller
                    |-> suite du programme
---- 3 Lui dire que vous avez trop fais la fête la veille et que vous êtes trop fatiguer... (fin du programme)
        |-> La mère furieuse contre vous, vous met à la porte et vous avez perdu...

- Vous passez la porte de l'entrée et vous retrouvez dehors sur le pas de la porte.
---- 1 Aller tout droit en direction de la forêt
        |-> Arriver devant l'entrée de la fôret, un homme en capuche ce poste devant vous et vous regarde fixement.
        |--------> 1 Lui demander si il n'a pas vu un anneau dans les environs
                    |-> Il vous indique en effet qu'il a trouver un anneau mais qu'il vous le donnera qu'en echange
                    |   de 2 reponses.
                    |--------> 1 accepter
                                |-> l'homme souris, et pose alors la première question. je suis noir, je deviens rouge,
                                    et je finis blanc. Qui sui-je ?
                                |-------- 1 Du charbon
                                            |-> Bonne réponse ! l'homme souris et pose une seconde question. Quel est le
                                            |   plus gros chiffre au monde ?
                                            |-------- 1 100000000000000000000000000000000000000000000000000000000000
                                                        |-> Mauvaise réponse... l'homme souris et disparait dans la forêt. Fin du jeu
                                            |-------- 2 9
                                                        |-> l'Homme surpris, vous regarde fixement. Il disparait subitement et laisse
                                                            a sa place un anneau. Celui de votre mère. Vous repartez lui rendre et vous
                                                            avez gagner !
                                            |-------- 3 Il n'existe pas puisque il n'y a pas de limite...
                                                        |-> Mauvaise réponse... l'homme souris et disparait dans la forêt. Fin du jeu
                                |-------- 2 Un feu de camp
                                            |-> l'homme souris et disparait dans la forêt. Fin du jeu
                    |--------> 2 refuser
                                |-> l'homme souris et disparait dans la forêt. Fin du jeu
        |--------> 3 Rebrousser chemin, cet homme à l'air louche...
                    |->retour à la phase précédente
---- 2 Aller à droite en direction de la grange
        |-> Vous arrivez devant la porte de la grange.
        |-------- 1 Ouvrir la porte et entrer
                    |-> Vous entrez dans la grange. Devant vous un tas de paille avec une fourche poser dessus.
                    |-------- 1 Inspecter le tas de paille
                                |-------- Après une fouille rapide, il n'y a rien d'interessent et vous décidez de partir
                                |-------- retour à la phase précédente
                    |-------- 2 Faire demi-tour et sortir.
                                |-> retour à la phase précédente
        |-------- 2 Revenir en arrière
                    |-> retour à la phase précédente
---- 3 Vous avez trop peur, vous rentrez


ENGLISH (comming soon...)
