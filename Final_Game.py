import pickle
from Game import *
from Player import *
from Neuron import *
import pickle
name = input(" votre nom : ")
mode = input("difficulte : easy, medium ou hard ? ")
game = Game(15)
player1 = CPUPlayer("CPU", mode, 15)
palyer2 = HumanPlayer(name)
if mode == 'hard' :
    with open('NeronNetwork.txt', 'rb') as inp : ns = pickle.load(inp)
    player1.netw = ns
game.start(player1, palyer2, True)
