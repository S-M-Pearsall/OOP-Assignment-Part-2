from abc import ABC, abstractmethod

'''Abstract class that contains the ability for future masterminds to spawn off of it through inheritance'''
class SuperMastermind(ABC):
    def __init__(self, rows, rounds, secretCode, winConditions, secretLength):
        self.rows = rows
        self.rounds = rounds
        self.secretCode = secretCode
        self.winConditions = winConditions
        self.secretLength = secretLength

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

'''Class to determine whether player is human or not'''
class Player:
    def __init__(self, ishuman):
        self.ishuman = False

'''Method to place a peg in a position'''
    def placePeg(pegPosition):
        pass

'''Method to choose the colour of the peg'''
    def choosePegColour(string):
        pass

'''Method for choosing the secret code that is meant to be guessed'''
class SecretCode:

    def __init__ (self, shieldCode):
        self.shieldCode = shieldCode

    def setShieldCode(shieldCode):
        pass

    def generateShieldCode(shieldCode):
        pass

    def setColour(colour):
        pass

    def revealCode(shieldCode):
        pass

    def checkSecretLength(secretLength):
        pass

class DecodingBoard:

    def __init__(self, shield, guessHoles, feedbackHoles, shieldHoles):
        self.shield = shield
        self.guessHoles = guessHoles
        self.feedbackHoles = feedbackHoles
        self.shieldHoles = shieldHoles

    def placePeg(peg):
        pass