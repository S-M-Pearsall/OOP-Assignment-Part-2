from Assignment2Mastermind import MastermindOnePlayer as mop
#from Assignment2Mastermind import MastermindTwoPlayer
import unittest
class TestMastermind(unittest.TestCase):

    def test_MastermindPlayerOne(self):
        firstPerson = "Jesse"
        testcode = ['r, g, w, b']

        self.assertEqual(firstPerson.getName, "Jesse")
        self.assertEqual(testcode, ['r, g, w, b'])







unittest.main()