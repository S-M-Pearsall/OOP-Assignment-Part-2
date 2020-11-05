from abc import ABC, abstractmethod
import random
import string
import unittest

''' Class to run the main menu where player chooses their gamemode'''


class MainMenu:

    '''Method of MainMenu class where player chooses their gamemode'''

    def play(self):
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
        if gametype != "a" and gametype != "b" and gametype != "c":
            print("Error, invalid input, please retry, you can either choose A, B or C")
            gametype = input("*Enter A, B, or C to continue*")

        ''' These if statements check what gametype is selected and proceed
        to play out the game that has been selected'''
        if gametype == "a":

            MastermindTwoPlayer.getName(self)

        elif gametype == "b":

            MastermindOnePlayer.getName(self)


        elif gametype == "c":
            Mastermind44.getName(self)
            

        MainMenu.continuePlaying(self)

    def continuePlaying(self):
        print("What would you like to do?")
        willYouPlay = input("(p)lay the game again\n(q)uit")
        if willYouPlay == "p":
            MainMenu.play(self)


'''An abstract class for new gametypes to inherit from'''


class supermastermind(ABC):
    '''An abstract method for gametypes to inherit from so they can set names'''
    @abstractmethod
    def getName(self):
        pass
    '''An abstract method for gametypes to inherit from where they can do their guesses and feedback'''
    @abstractmethod
    def guess(self):
        pass

    @abstractmethod
    def guessFeedback(self):
        pass

'''Abstract class for gamemodes to inherit shield code generation from'''
class codeShield(ABC):

    '''Abstract method for shieldcode generation to be inherited'''
    @abstractmethod
    def generateShieldCode(self):
        pass


'''Inherited class for basic two player Mastermind gametype'''


class MastermindTwoPlayer(supermastermind, codeShield):
    def __init__(self, secretCode, secretCodeList, indexRounds):
        self.secretCode = secretCode
        self.secretCodeList = []
        self.indexRounds = indexRounds

    '''Method to get the name of the current players'''
    def getName(self):
        self.player1 = input("Player 1: What is your name?")

        self.player2 = input("Player 2: what is your name?")

        self.generateShieldCode()

    '''Method to generate the secret shield code'''
    def generateShieldCode(self):

        print("Welcome ", self.player1,", you need to create a code that consists of four pegs.")
        print("Each peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite or (B)lack.")
        print("Specify the colour by specifying four characters where each character indicates a colour")
        print("as above. For example, WWRG represents the code Whie-White-Red-Green. You need to enter")
        print("the code twice. No character is shown on the screen so Supermind cannot see it.")
        secretCode = input("Enter the code now:")
        confirmSecretCode = input("Enter the code again:")

        '''While statement to check if the two codes match'''
        while confirmSecretCode != secretCode:
            print("Error, please re-enter the code twice")
            secretCode = input("Enter the code now:")
            confirmSecretCode = input("Enter the code again:")

        '''Makes sure the secret code only contains valid characters'''
        for x in secretCode:
            if x not in ['r', 'l', 'g', 'y', 'w', 'b']:
                print(
                    "error, each peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite or (B)lack.")
                print("No other colours")
                secretCode = input("Enter the code now:")
                confirmSecretCode = input("Enter the code again:")

        '''Makes sure the length of the secret code is valid'''
        if len(secretCode) != 4:
            print("Error, secret code must be a length of 4.")
            secretCode = input("Enter the code now:")
            confirmSecretCode = input("Enter the code again:")

        print("The code was stored.")
        secretCodeList = list(secretCode)

        indexRounds = 0

        self.guess(self.player2, secretCodeList, indexRounds)

    '''Takes the players a players guess and verifies it'''
    def guess(self, player2, secretCodeList, indexRounds):
        feedback = []
        rounds = 12
        attemptCounter = 1
        print("Welcome ", player2,
              ". You can now start to play by guessing the code.")
        print("Enter an attempt by providing four characters and press Enter")

        ''' While the index is less than 12 and the win condition is false
        Go through each letter in the guessed code, compare it to the secret code.
        if letter is same as secret code letter in same position, add B to feedback
        if letter exists in the guess then it adds a white peg before then removing x number
        of white pegs determined by the number of black pegs'''
        while indexRounds < rounds:
            playerAttempt = input("Give me Input")

            '''Checks validity of the guess length'''
            if len(playerAttempt) != 4:
                print(
                    "This attempt is incorrect. You must provide exactly four characters.")
                playerAttempt = input("Give me Input")

            '''Makes sure all guess characters are valid'''
            for x in playerAttempt:
                if x not in ['r', 'l', 'g', 'y', 'w', 'b']:
                    print("Characters can only be R, L, G, Y, W or B")
                    playerAttempt = input("Give me Input")
            feedback = MastermindTwoPlayer.guessFeedback(self, playerAttempt, secretCodeList, indexRounds, attemptCounter)

            '''Checks if win conditions are valid'''
            if feedback == ['B', 'B', 'B', 'B']:
                indexRounds = 12
                print("Congratulations! You broke the code in ",
                      attemptCounter, " attempts.")

            elif feedback != ['B', 'B', 'B', 'B'] and attemptCounter == 12:
                print(
                    "You have failed to guess the secret code correctly. The mastermind wins.")

        indexRounds = indexRounds + 1
        attemptCounter = attemptCounter + 1

    '''Checks the player's guess and gives feedback'''
    def guessFeedback(self, playerAttempt, secretCodeList, indexRounds, attemptCounter):
        blackFeedback = []
        whiteFeedback = []
        indexSecretCode = 0
        '''Goes through the guess and generates feedback on whether it's correct or not'''
        playerAttemptList = list(playerAttempt)
        for x in playerAttemptList:

            if x == secretCodeList[indexSecretCode]:
                blackFeedback.append("B")
                indexSecretCode = indexSecretCode + 1

            if x in secretCodeList:
                whiteFeedback.append("W")

        indexSecretCode = 0

        for x in blackFeedback:
            whiteFeedback.pop(0)

        feedback = blackFeedback + whiteFeedback

        feedbackString = ''.join(feedback)

        if not feedback:
            print("Feedback on attempt #", attemptCounter, ":  Nothing.")

        else:
            print("Feedback on attempt #", attemptCounter, ":", feedbackString)

        blackFeedback.clear()
        whiteFeedback.clear()
        return feedback

'''Inherited class for singleplayer original Mastermind against computer'''
class MastermindOnePlayer(supermastermind, codeShield):
    def __init__(self, secretCode, secretCodeList, indexRounds):
        self.secretCode = secretCode
        self.secretCodeList = []
        self.indexRounds = indexRounds

    '''Method to get the name of the current players'''

    def getName(self):
        self.player1 = input("Player 1: What is your name?")

        self.generateShieldCode()

    '''Method that uses random and ascii_letters to create a random code while making sure that the
    letters used are valid colours'''

    def generateShieldCode(self):
        asciiNumberCode = string.ascii_letters
        index = 0

        while index < 4:
            holdingShieldCode = random.choice(asciiNumberCode)
            while holdingShieldCode != "r" and holdingShieldCode != "l" and holdingShieldCode != "g" and holdingShieldCode != "y" and holdingShieldCode != "w" and holdingShieldCode != "b":
                holdingShieldCode = ""
                holdingShieldCode = random.choice(asciiNumberCode)

            self.secretCodeList.append(holdingShieldCode)
            index = index + 1
            holdingShieldCode = ""
        indexRounds = 0
        self.guess(self.player1, self.secretCodeList, indexRounds)

    '''Method o take a players guesses and give them feedback'''
    def guess(self, player1, secretCodeList, indexRounds):
        feedback = []
        rounds = 12
        attemptCounter = 1
        print("Welcome ", player1,". You can now start to play by guessing the code.")
        print("Enter an attempt by providing four characters and press Enter")

        ''' While the index is less than 12 and the win condition is false
        Go through each letter in the guessed code, compare it to the secret code.
        if letter is same as secret code letter in same position, add B to feedback
        if letter exists in the guess then it adds a white peg before then removing x number
        of white pegs determined by the number of black pegs'''
        while indexRounds < rounds:
            playerAttempt = input("Give me Input")

            '''Checks validity of the guess length'''
            if len(playerAttempt) != 4:
                print(
                    "This attempt is incorrect. You must provide exactly four characters.")
                playerAttempt = input("Give me Input")

            '''Makes sure all guess characters are valid'''
            for x in playerAttempt:
                if x not in ['r', 'l', 'g', 'y', 'w', 'b']:
                    print("Characters can only be R, L, G, Y, W or B")
                    playerAttempt = input("Give me Input")
            feedback = self.guessFeedback(playerAttempt, secretCodeList, indexRounds, attemptCounter)

            '''Checks if win conditions are valid'''
            if feedback == ['B', 'B', 'B', 'B']:
                indexRounds = 12
                print("Congratulations! You broke the code in ",
                      attemptCounter, " attempts.")

            elif feedback != ['B', 'B', 'B', 'B'] and attemptCounter == 12:
                print(
                    "You have failed to guess the secret code correctly. The mastermind wins.")

        indexRounds = indexRounds + 1
        attemptCounter = attemptCounter + 1

    def guessFeedback(self, playerAttempt, secretCodeList, indexRounds, attemptCounter):
        blackFeedback = []
        whiteFeedback = []
        indexSecretCode = 0
        '''Goes through the guess and generates feedback on whether it's correct or not'''
        playerAttemptList = list(playerAttempt)
        for x in playerAttemptList:

            if x == secretCodeList[indexSecretCode]:
                blackFeedback.append("B")
                indexSecretCode = indexSecretCode + 1

            if x in secretCodeList:
                whiteFeedback.append("W")

        indexSecretCode = 0

        for x in blackFeedback:
            whiteFeedback.pop(0)

        feedback = blackFeedback + whiteFeedback

        feedbackString = ''.join(feedback)

        if not feedback:
            print("Feedback on attempt #", attemptCounter, ":  Nothing.")

        else:
            print("Feedback on attempt #", attemptCounter, ":", feedbackString)

        blackFeedback.clear()
        whiteFeedback.clear()
        return feedback

'''Class for playing Mastermind44'''
class Mastermind44(supermastermind, codeShield):
    '''Takes player names as input and assigns to variable'''
    def getName(self):
        self.player1 = input("Player 1: What is your name?")
        self.player2 = input("Player 2: What is your name?")
        self.player3 = input("Player 3: What is your name?")
        self.player4 = input("Player 4: What is your name?")

    '''Generates a random code and assigns one position and element to each mastermind'''
    def generateShieldCode(self):
        asciiNumberCode = string.ascii_letters
        self.secretCodeList = []
        index = 0
        choosingMastermind = 0
        mastermindPosition = []
        takenposition = []

        while index < 5:
            holdingShieldCode = random.choice(asciiNumberCode)
            while holdingShieldCode != "r" and holdingShieldCode != "l" and holdingShieldCode != "g" and holdingShieldCode != "y" and holdingShieldCode != "w" and holdingShieldCode != "b":
                holdingShieldCode = ""
                holdingShieldCode = random.choice(asciiNumberCode)

            self.secretCodeList.append(holdingShieldCode)
            index = index + 1
            holdingShieldCode = ""

        indexRounds = 0

    def playerCodeAssign(self):
        takenposition = []

        print("Welcome to Mastermind44! The computer will create the secret code and reveal")
        print("four of the five positions one-by-one individually to each player. During")
        print("revealing each position only the requested player should look at the screen.")
        print("(R)ed, b(L)ue, (G)reen, (Y)ellow, (W)hite, or (B)lack")
        positionHoldingVariable = random.randint(0, 4)
        takenposition.append(positionHoldingVariable)
        self.player1Code = self.secretCodeList[positionHoldingVariable]
        positionHoldingVariable = positionHoldingVariable + 1
        self.player1Position = positionHoldingVariable
        print("Player ", self.player1, ": When you are ready for one position of the code to be revealed")
        print("on the screen press <enter>")
        randomEnterVariable = input("")
        print("Position: ", self.player1Position, "Colour: ", self.player1Code)

        positionHoldingVariable = random.randint(0, 4)
        while positionHoldingVariable in takenposition:
            positionHoldingVariable = random.randint(0, 4)
        self.player2Code = self.secretCodeList[positionHoldingVariable]
        positionHoldingVariable = positionHoldingVariable + 1
        self.player2Position = positionHoldingVariable
        print("Player ", self.player2, ": When you are ready for one position of the code to be revealed")
        print("on the screen press <enter>")
        randomEnterVariable = input("")
        print("Position: ", self.player2Position, "Colour: ", self.player2Code)

        positionHoldingVariable = random.randint(0, 4)
        while positionHoldingVariable in takenposition:
            positionHoldingVariable = random.randint(0, 4)
        self.player3Code = self.secretCodeList[positionHoldingVariable]
        positionHoldingVariable = positionHoldingVariable + 1
        self.player3Position = positionHoldingVariable
        print("Player ", self.player3, ": When you are ready for one position of the code to be revealed")
        print("on the screen press <enter>")
        randomEnterVariable = input("")
        print("Position: ", self.player3Position, "Colour: ", self.player3Code)

        positionHoldingVariable = random.randint(0, 4)
        while positionHoldingVariable in takenposition:
            positionHoldingVariable = random.randint(0, 4)
        self.player4Code = self.secretCodeList[positionHoldingVariable]
        positionHoldingVariable = positionHoldingVariable + 1
        self.player4Position = positionHoldingVariable
        print("Player ", self.player4, ": When you are ready for one position of the code to be revealed")
        print("on the screen press <enter>")
        randomEnterVariable = input("")
        print("Position: ", self.player4Position, "Colour: ", self.player4Code)

    def guess(self):
        print("Each player can now start to guess the code.")
        while index > rounds:
            pass


m = MainMenu()

m.play()
