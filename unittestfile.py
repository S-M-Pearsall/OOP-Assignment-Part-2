import unittest
import random
import string

from Assignment2Mastermind import MastermindOnePlayer
from Assignment2Mastermind import MastermindTwoPlayer

'''Class to test the generation of a shieldcode'''
class TestingMastermind(unittest.TestCase):

    def __init__(self):
        self.mop = MastermindOnePlayer('rgwb', ['r, g, w, b'])

unittest.main()