from abc import ABC, abstractmethod import string import random

''' Class to run the main menu where player chooses their gamemode'''
class MainMenu:

    '''Method of MainMenu class where player chooses their gamemode'''
    def play(self, gametype):
        print("Welcome to Mastermind!")
        print("Developed by Scott Pearsall")
        print("COMP 1046 Object Oriented Programming")

        print("Select which game you want to play:")
        print("    (A) Original Mastermind for 2 Players")
        print("    (B) Original Mastermind for 1 Player")
        print("    (C) Mastermind44 for 4 players")
        gametype = input("*Enter A, B, or C to continue*")


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

'''Inherited class for basic Mastermind gametype'''
class Mastermind(SuperMastermind):
    pass

'''Inherited class for Mastermind44 gametype'''
class Mastermind44(SuperMastermind):
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

    '''Method for player setting shieldcode'''
    def setShieldCode(shieldCode):
        pass

    '''Method for AI generating shieldcode'''
    def generateShieldCode(shieldCode):
        asciiNumberCode = string.ascii_letters
        shieldCode = ""
        index = 0

        while index < 4:
            holdingShieldCode = random.choice(asciiNumberCode)
            while holdingShieldCode != "R" and holdingShieldCode != "L" and holdingShieldCode != "G" and holdingShieldCode != "Y" and holdingShieldCode != "W" and holdingShieldCode != "B"
                holdingShieldCode = random.choice(asciiNumberCode) 

            shieldCode = shieldCode + holdingShieldCode
            index = index + 1
            holdingShieldCode = ""

        
    def setColour(colour):
        pass

    def revealCode(shieldCode):
        pass

    def checkSecretLength(secretLength):
        pass

'''Board to make guesses and give feedback'''
class DecodingBoard:

    def __init__(self, shieldCode, feedback, pegCode):
        self.shieldCode = shieldCode
        self.feedback = feedback
        self.pegCode = pegCode

    '''Method for player to make a guess on what they think the code is'''
    def playerGuess():
        pass

    '''Feedback Method to provide feedback to player'''
    def feedback(self, pegCode):
        index = 1

        for x in pegCode:
            if x == shieldcode(x):
                feedback == feedback + "B"
            elif x is in shieldCode and x != shieldCode(x):
                feedback == feedback + "W"
        print("Feedback on Attempt #", index)
        index = index + 1




