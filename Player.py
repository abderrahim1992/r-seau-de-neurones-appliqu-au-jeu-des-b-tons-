import random
from Neuron import *

class Player:
    def __init__(self,name):
        self.name = name
        self.nbWin = 0
    def getName(self):
        return self.name
    def getNbWin(self):
        return self.nbWin
    def addWin(self):
        self.nbWin+=1
    def addLoss(self):
        pass

class HumanPlayer(Player):
    def play(self,sticks):
        if sticks==1: return 1 # 1 bâton restant
        else:
            correct = False
            while not correct:
                nb = input('Sticks?\n') # Récupère le choix de l'utilisateur
                try:
                    nb=int(nb) # Convertit le choix en entier
                    if nb>=1 and nb<=3 and sticks-nb>=0:
                        correct=True # Nombre valide
                except: pass
            return nb

class CPUPlayer(Player):
    def __init__(self,name,mode,nbSticks):
        super().__init__(name)
        self.mode = mode # Mode facile, moyen ou dificile
        self.netw = NeuronNetwork(3,nbSticks) # Réseau de neurone
        self.previousNeuron = None 
    def play(self,sticks):
        if self.mode=='easy': return self.playEasy(sticks)
        elif self.mode=='hard': return self.playHard(sticks)
        else: return self.playMedium(sticks)
    def playMedium(self,sticks):
        # TODO compléter ici avec les quelques conditions pour éviter de faire une grosse erreur aux derniers tours
        if sticks <= 4 :
            return sticks-1
        return self.playRandom(sticks)
    def playEasy(self,sticks):
        return self.playRandom(sticks)
    def playRandom(self,sticks):
        if sticks < 4 : return random.randint(1, sticks)
        else : return random.randint (1, 3)
    def playHard(self,sticks):
        # TODO utiliser le réseau neuronal pour choisir le nombre de bâtons à jouer
        # utiliser l'attribut self.previousNeuron pour avoir le neuron précédemment sollicité dans la partie
        # calculer un 'shift' qui correspond à la différence entre la valeur du précédent neurone et le nombre de bâtons encore en jeu
        # utiliser la méthode 'chooseConnectedNeuron' du self.previousNeuron puis retourner le nombre de bâtons à jouer
        # bien activer le réseau de neurones avec la méthode 'activateNeuronPath' après avoir choisi un neurone cible
        # attention à gérer les cas particuliers (premier tour ou sticks==1)
        if sticks == 1 :
            return 1
        if self.previousNeuron == None :
            self.previousNeuron = self.netw.getNeuron(sticks)
            shift = 0
        else : 
            shift = self.previousNeuron.index - sticks
        choosenNeuron = self.previousNeuron.chooseConnectedNeuron(shift)
        nb = sticks - choosenNeuron.index
        self.netw.activateNeuronPath(self.previousNeuron, choosenNeuron)
        self.previousNeuron = choosenNeuron
        return nb
    def getNeuronNetwork(self): return self.netw
    def addWin(self):
        super().addWin()
        self.netw.recompenseConnections()
        self.previousNeuron=None
    def addLoss(self):
        super().addLoss()
        self.previousNeuron=None




        


