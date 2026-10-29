#!/usr/bin/env python3
import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")
    dice_value = roll_dice()
    print(f"You rolled a {dice_value}!")
    break
