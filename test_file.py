from Assignment2Mastermind import MastermindOnePlayer
#from Assignment2Mastermind import MastermindTwoPlayer
import pytest

def test_shield_code():
    m = MastermindOnePlayer()
    m.generateShieldCode()
    assert len(m.secretCodeList) == 4