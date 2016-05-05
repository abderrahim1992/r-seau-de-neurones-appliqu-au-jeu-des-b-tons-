from Game import *
from Player import *
from Neuron import *
JoueurH = HumanPlayer("abdou")
JoueurCPU = CPUPlayer("CPU","hard",15)
game = Game(15)
game.start(JoueurH,JoueurCPU,True)