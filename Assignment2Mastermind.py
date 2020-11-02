from abc import ABC, abstractmethod 
import random 
import string

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

            pass

        elif gametype == "c":
            #Mastermind44()
            pass

        MainMenu.continuePlaying(self)

    def continuePlaying(self):
        print("What would you like to do?")
        willYouPlay = input("(p)lay the game again\n(q)uit")
        if willYouPlay == "p":
            MainMenu.play(self)
        
            
            

'''Inherited class for basic two player Mastermind gametype'''
class MastermindTwoPlayer:
    def __init__(self, secretCode, secretCodeList):
        self.secretCode = secretCode
        self.secretCodeList = []

    '''Method to get the name of the current players'''
    def getName(self):
        self.player1 = input("Player 1: What is your name?")

        self.player2 = input("Player 2: what is your name?")

        MastermindTwoPlayer.generateShieldCode(self)


    '''Method to generate the secret shield code'''
    def generateShieldCode(self):

        print("Welcome ", self.player1, ", you need to create a code that consists of four pegs.")
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
                print("error, each peg can be of the colour (R)ed, B(L)ue, (G)reen, (Y)ellow, (W)hite or (B)lack.")
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

        MastermindTwoPlayer.guessAndFeedback(self, self.player2, secretCodeList)

    '''Method o take a players guesses and give them feedback'''
    def guessAndFeedback(self, player2, secretCodeList):
        rounds = 12
        indexRounds = 0
        indexSecretCode = 0
        attemptCounter = 1
        winCondition = False
        blackFeedback = []
        whiteFeedback = []
        print("Welcome ", player2, ". You can now start to play by guessing the code.")
        print("Enter an attempt by providing four characters and press Enter")

        ''' While the index is less than 12 and the win condition is false
        Go through each letter in the guessed code, compare it to the secret code.
        if letter is same as secret code letter in same position, add B to feedback
        if letter exists in the guess then it adds a white peg before then removing x number
        of white pegs determined by the number of black pegs'''
        while indexRounds < rounds and winCondition == False:
            playerAttempt = input("Give me Input")

            '''Checks validity of the guess length'''
            if len(playerAttempt) != 4:
                print("This attempt is incorrect. You must provide exactly four characters.")
                playerAttempt = input("Give me Input")
            
            '''Makes sure all guess characters are valid'''
            for x in playerAttempt:
                if x not in ['r', 'l', 'g', 'y', 'w', 'b']:
                    print("Characters can only be R, L, G, Y, W or B")
                    playerAttempt = input("Give me Input")

            
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

            '''Checks if win conditions are valid'''    
            if feedback == ['B','B','B','B']:
                winCondition = True
                print("Congratulations! You broke the code in ", attemptCounter, " attempts.")

            elif feedback != ['B','B','B','B'] and attemptCounter == 12:
                print("You have failed to guess the secret code correctly. The mastermind wins.")

            indexRounds = indexRounds + 1
            attemptCounter = attemptCounter + 1

        indexRounds = 0
        attemptCounter = 1
            

class MastermindOnePlayer:
    def __init__(self, secretCode, secretCodeList):
        self.secretCode = secretCode
        self.secretCodeList = []

    '''Method to get the name of the current players'''
    def getName(self):
        self.player1 = input("Player 1: What is your name?")

        MastermindOnePlayer.generateShieldCode(self)

    '''Method that uses random and ascii_letters to create a random code while making sure that the
    letters used are valid colours'''
    def generateShieldCode(self):
        asciiNumberCode = string.ascii_letters
        secretCodeList = []
        index = 0

        while index < 4:
            holdingShieldCode = random.choice(asciiNumberCode)
            while holdingShieldCode != "r" and holdingShieldCode != "l" and holdingShieldCode != "g" and holdingShieldCode != "y" and holdingShieldCode != "w" and holdingShieldCode != "b":
                holdingShieldCode = ""
                holdingShieldCode = random.choice(asciiNumberCode) 

            secretCodeList.append(holdingShieldCode)
            index = index + 1
            holdingShieldCode = ""
        
        print(secretCodeList)
        
        MastermindOnePlayer.guessAndFeedback(self, self.player1, secretCodeList)

    def guessAndFeedback(self, player1, secretCodeList):
        rounds = 12
        indexRounds = 0
        indexSecretCode = 0
        attemptCounter = 1
        winCondition = False
        blackFeedback = []
        whiteFeedback = []
        print("Welcome ", player1, ". You can now start to play by guessing the code.")
        print("Enter an attempt by providing four characters and press Enter")

        ''' While the index is less than 12 and the win condition is false
        Go through each letter in the guessed code, compare it to the secret code.
        if letter is same as secret code letter in same position, add B to feedback
        if letter exists in the guess then it adds a white peg before then removing x number
        of white pegs determined by the number of black pegs'''
        while indexRounds < rounds and winCondition == False:
            playerAttempt = input("Give me Input")

            '''Checks validity of the guess length'''
            if len(playerAttempt) != 4:
                print("This attempt is incorrect. You must provide exactly four characters.")
                playerAttempt = input("Give me Input")
            
            '''Makes sure all guess characters are valid'''
            for x in playerAttempt:
                if x not in ['r', 'l', 'g', 'y', 'w', 'b']:
                    print("Characters can only be R, L, G, Y, W or B")
                    playerAttempt = input("Give me Input")

            
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

            '''Checks if win conditions are valid'''    
            if feedback == ['B','B','B','B']:
                winCondition = True
                print("Congratulations! You broke the code in ", attemptCounter, " attempts.")

            elif feedback != ['B','B','B','B'] and attemptCounter == 12:
                print("You have failed to guess the secret code correctly. The mastermind wins.")

            indexRounds = indexRounds + 1
            attemptCounter = attemptCounter + 1

        indexRounds = 0
        attemptCounter = 1



'''Class to determine whether player is human or not'''
class Player:
    def __init__(self, ishuman):
        self.ishuman = False

'''Method for choosing the secret code that is meant to be guessed'''
class SecretCode:

    def __init__ (self, shieldCode):
        self.shieldCode = shieldCode

    '''Method for player setting shieldcode'''
    def setShieldCode(self, shieldCode):
        pass

    '''Method for AI generating shieldcode'''
    def generateShieldCode(self, shieldCode):
        asciiNumberCode = string.ascii_letters
        shieldCode = ""
        index = 0

        while index < 4:
            holdingShieldCode = random.choice(asciiNumberCode)
            while holdingShieldCode != "R" and holdingShieldCode != "L" and holdingShieldCode != "G" and holdingShieldCode != "Y" and holdingShieldCode != "W" and holdingShieldCode != "B":
                holdingShieldCode = random.choice(asciiNumberCode) 

            shieldCode = shieldCode + holdingShieldCode
            index = index + 1
            holdingShieldCode = ""

        
    def setColour(self, colour):
        pass

    def revealCode(self, shieldCode):
        pass

    def checkSecretLength(self, secretLength):
        pass


m = MainMenu()

m.play()


