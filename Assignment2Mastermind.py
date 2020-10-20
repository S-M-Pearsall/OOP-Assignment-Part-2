from abc import ABC, abstractmethod

'''Abstract class that contains the ability for future masterminds to spawn off of it through inheritance'''

class SuperMastermind(ABC):

    '''Abstract method for use with setting the gametype such as which mastermind'''
    @abstractmethod
    def setGametype(self):
        pass

    '''Abstract method for setting the player mode such as singleplayer or with other people'''
    @abstractmethod
    def setPlayerMode(self):
        pass

    '''Abstract method for providing feedback of ones guesses with the code'''
    @abstractmethod
    def provideFeedback(self):
        pass

    '''Abstract method for defining the number of rows to be used'''
    @abstractmethod
    def numberofRows(self):
        pass

    '''Abstract method for defining the amount of rounds to be used'''
    @abstractmethod
    def amountOfRounds(self):
        pass

    '''Abstract method to check the win conditions and whether they are true'''
    @abstractmethod
    def checkWinConditions(self):
        pass
