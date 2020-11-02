import unittest
import random
import string
import Assignment2Mastermind

class Testing(unittest.TestCase):
    
    def test_computer_code_generation(self):
        asciiNumberCode = string.ascii_letters
        secretCodeList = []
        index = 0

        while index < 5:
            holdingShieldCode = random.choice(asciiNumberCode)
            while holdingShieldCode != "r" and holdingShieldCode != "l" and holdingShieldCode != "g" and holdingShieldCode != "y" and holdingShieldCode != "w" and holdingShieldCode != "b":
                holdingShieldCode = ""
                holdingShieldCode = random.choice(asciiNumberCode) 

            secretCodeList.append(holdingShieldCode)
            index = index + 1
            holdingShieldCode = ""
        self.assertEqual(len(secretCodeList), 4)


unittest.main()