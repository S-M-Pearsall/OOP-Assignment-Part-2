import pytest
from Assignment2Mastermind import *

#While the code seems solid, pytest gives me an error that I could not figure out how to fix.
#I know it has something to do with the inputs but I'm not sure what to do.
#In your feedback could you explain the error and how to fix it "in detail"
#So I can learn from this mistake?

'''Class to test mastermind one player'''
class test_Mastermind_One_Player:

    '''Function that tests shieldcode's length'''
    def test_shield_code(self):
        player1 = "Jesse"

        p = MastermindOnePlayer(player1)
        p.generateShieldCode()

        assert len(p.secretCodeList) == 4

    '''Function that makes sure a correct guess gives correct feedback'''
    def test_correct_guess_feedback(self):

        player1 = "Jesse"

        playerAttempt = 'rrrr'
        secretCodeList = ['r', 'r', 'r', 'r']

        indexRounds = 1
        attemptCounter = 1

        p = MastermindOnePlayer(player1)
        feedback = p.guessFeedback(playerAttempt, secretCodeList, indexRounds, attemptCounter)

        assert feedback == ['B', 'B', 'B', 'B']

'''Class to test mastermind two player'''
class test_Mastermind_Two_Player:

    '''Function to test that proper feedback is given if guess is correct'''
    def test_correct_guess_feedback(self):

        player1 = "Jesse"
        player2 = "James"
        playerAttempt = 'rrrr'
        secretCodeList = ['r', 'r', 'r', 'r']
        indexRounds = 1
        attemptCounter = 1

        p = MastermindTwoPlayer(player1, player2)

        feedback = p.guessFeedback(playerAttempt, secretCodeList, indexRounds, attemptCounter)

        assert feedback == ['B', 'B', 'B', 'B']

    '''Function to test that incorrect feedback is not given if guess is wrong'''
    def test_false_guess_feedback(self):

        player1 = "Jesse"
        player2 = "James"
        playerAttempt = 'rrrr'
        secretCodeList = ['L', 'L', 'L', 'L']
        indexRounds = 1
        attemptCounter = 1

        p = MastermindTwoPlayer(player1, player2)

        feedback = p.guessFeedback(playerAttempt, secretCodeList, indexRounds, attemptCounter)

        assert feedback != ['B', 'B', 'B', 'B']

'''Class to test mastermind44'''
class test_Mastermind44:

    '''Method to test shieldcode Length'''
    def test_shield_code(self):
        player1 = "Jesse"
        player2 = "James"
        player3 = "David"
        player4 = "Dina"

        p = Mastermind44(player1, player2, player3, player4)
        p.generateShieldCode()

        assert len(p.secretCodeList) == 5

    '''Function to test that proper feedback is given if guess is correct'''
    def test_correct_guess_feedback(self):

        player1 = "Jesse"
        player2 = "James"
        player3 = "David"
        player4 = "Dina"

        playerAttempt = 'rrrr'
        secretCodeList = ['r', 'r', 'r', 'r']

        indexRounds = 1
        attemptCounter = 1


        p = Mastermind44(player1, player2, player3, player4)

        feedback = p.guessFeedback(playerAttempt, secretCodeList, indexRounds, attemptCounter)

        assert feedback == ['B', 'B', 'B', 'B']

