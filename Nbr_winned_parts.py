from Game import *
from Player import *
from Neuron import *
import pickle
game = Game(15)
player1 = CPUPlayer("player1", 'hard', 15)
player2 = CPUPlayer("player2", 'hard', 15)
for i in range(20000) :
    game.start(player1, player2, False)
print(player1.getNbWin())
print(player2.getNbWin())
player1.getNeuronNetwork().printAllConnections()
player2.getNeuronNetwork().printAllConnections()
with open('NeronNetwork.txt', 'wb') as output : pickle.dump(player1.getNeuronNetwork(), output, pickle.HIGHEST_PROTOCOL)