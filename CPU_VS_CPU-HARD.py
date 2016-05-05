from Game import *
from Player import *
from Neuron import *
game = Game(15)
player1 = CPUPlayer("cpu1", 'hard', 15)
player2 = CPUPlayer("cpu2", 'hard', 15)
for i in range(200) :
    game.start(player1, player2, False)
print(player1.getNbWin())
print(player2.getNbWin())
