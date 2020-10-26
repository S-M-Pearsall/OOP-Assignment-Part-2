from abc import ABC, abstractmethod 
import random

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

        '''Takes the input and compares it. If it is a valid input it launches that gametype.
        Otherwise it tells the user that it is invalid and tells them to redo it.'''
        while gametype != "a" or gametype != "b" or gametype != "c":
            print("Error, invalid input, please retry, you can either choose A, B or C")
        
        if gametype == "a":
            MastermindTwoPlayer()

        elif gametype == "b":
            MastermindOnePlayer()

        elif gametype == "c":
            Mastermind44()

        getName()

        generateShieldCode()


'''Abstract class that contains the ability for future masterminds to spawn off of it through inheritance'''
class SuperMastermind(ABC):
    def __init__(self, rows, rounds, secretCode, winConditions, secretLength):
        self.rounds = rounds
        self.secretCode = secretCode
        self.winConditions = winConditions
        self.secretLength = secretLength

    @abstractmethod
    def getName(self):
        pass

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

    '''Abstract method to check the win conditions and whether they are true'''
    @abstractmethod
    def checkWinConditions(self):
        pass

'''Inherited class for basic one player Mastermind gametype'''
class MastermindOnePlayer(SuperMastermind):
    pass

'''Inherited class for basic two player Mastermind gametype'''
class MastermindTwoPlayer(SuperMastermind):
    def __init__(self, rounds, secretCode)
        super().__init__(rounds, secretCode)
        self.rounds = 12
        self.secretCode = secretCode

    '''Method to get the name of the current players'''
    def getName():
        player1 = input("Player 1: What is your name?")

        player2 = input("Player 2: what is your name?")

    '''Method to generate the secret shield code'''
    def generateShieldCode():

        print("Welcome ", player1, ", you need to create a code that consists of four pegs.")
        print("Each peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite or (B)lack.")
        print("Specify the colour by specifying four characters where each character indicates a colour")
        print("as above. For example, WWRG represents the code Whie-White-Red-Green. You need to enter")
        print("the code twice. No character is shown on the screen so Supermind cannot see it.")
        secretCode = input("Enter the code now:")
        confirmSecretCode = input("Enter the code again:")
        #REMEMBER TO MAKE SURE SECRET CODE CANNOT BE MADE IN A WRONG WAY
        while confirmSecretCode != secretCode:
            print("Error, please re-enter the code twice")
                secretCode = input("Enter the code now:")
                confirmSecretCode = input("Enter the code again:")

        print("The code was stored.")
        secretCodeList = list(secretCode)

    '''Method o take a players guesses and give them feedback'''
    def guessAndFeedback():
        index = 0
        attemptCounter = 1
        winCondition = False
        print("Welcome ", player2, ". You can now start to play by guessing the code.")
        print("Enter an attempt by providing four characters and press Enter")

        ''' While the index is less than 12 and the win condition is false
        Go through each letter in the guessed code, compare it to the secret code.
        if letter is same as secret code letter in same position, add B to feedback
        if letter is not in the same position, but still exists in the secret code
        W is added to feedback'''
        while index > rounds and winCondition == False:
            playerAttempt = input("Attempt #", attempt, ":")
            for x in playerAttempt:
                
                if x == secretCodeList(index):
                    feedback = feedback + "B "

                elif x != SecretCodeList(index) and x in secretCodeList:
                    feedback = feedback + "W "

                else:
                    feedback = feedback + " "

            print("Feedback on attempt #", attemptCounter, ":", feedback)

            index = index + 1
            attemptCounter = attemptCounter + 1
                
            if playerAttempt == SecretCode:
                winCondition = True
                print("Congratulations! You broke the code in ", attemptCounter, " attempts.")



'''Inherited class for Mastermind44 gametype'''
class Mastermind44(SuperMastermind):
    pass


'''Class to determine whether player is human or not'''
class Player:
    def __init__(self, ishuman):
        self.ishuman = False

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




