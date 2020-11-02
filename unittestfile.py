import unittest
import random
import string

from Assignment2Mastermind import MastermindOnePlayer
from Assignment2Mastermind import MastermindTwoPlayer

class Testing(unittest.TestCase):
    
    def test_computer_code_generation(self):
        self.assertEqual(len(secretCodeList), 4)


unittest.main()