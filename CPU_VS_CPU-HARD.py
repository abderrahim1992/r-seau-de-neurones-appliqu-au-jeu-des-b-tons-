from Game import *
from Player import *
from Neuron import *
jeu = Game(15)
joueur1 = CPUPlayer("Albert1", 'hard', 15)
joueur2 = CPUPlayer("Albert2", 'hard', 15)
for i in range(100) :
    jeu.start(joueur1, joueur2, False)
print(joueur1.getNbWin())
print(joueur2.getNbWin())
