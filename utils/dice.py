"""
Util that rolls dice for you
Author: Yisrael Hessler

Example
from utils import d4
hp = d4(4) + 10
"""
import random


def roll_dice(d: int, amount: int) -> int:
    # TODO: add roll summary printing, example: "Rolled 4d8, (5+2+1+5)=12"

    sumRoll = 0
    for i in range(amount):
        roll = random.randint(1, d)
        sumRoll += roll
    return sumRoll


def d4(amount: int = 1):
    """D4 dice roll"""
    return roll_dice(4, amount)


def d6(amount: int = 1):
    """D6 dice roll"""
    return roll_dice(6, amount)


def d8(amount: int = 1):
    """D8 dice roll"""
    return roll_dice(8, amount)


def d10(amount: int = 1):
    """D10 dice roll"""
    return roll_dice(10, amount)


def d12(amount: int = 1):
    """D12 dice roll"""
    return roll_dice(12, amount)


def d20(amount: int = 1):
    """D20 dice roll"""
    return roll_dice(20, amount)


def d100(amount: int = 1):
    """D100 dice roll"""
    return roll_dice(100, amount)
