#!/usr/bin/env python3

# ---
# Library imports

import random
from turtle import title

# ---
# Main Code

def show_menu():
    print (r""" 
   _____  __________ ______  _  __  ____      __   ___   ___  ___  _______ 
  / _ \ \/ /_  __/ // / __ \/ |/ / / __/___  / /  / _ | / _ \/ _ \/ __/ _ \
 / ___/\  / / / / _  / /_/ /    /  > _/_ _/ / /__/ __ |/ // / // / _// , _/
/_/    /_/ /_/ /_//_/\____/_/|_/  |_____/  /____/_/ |_/____/____/___/_/|_| 

1. Start
2. Rules
3. Exit  
    """)

def main_game():
    print("Welcome to the game!")

    # Add game logic here

def board():
    print("This is the game board.")


# ---
# Main Progam

def main():
    show_menu()

    while True:
        
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            main_game()
        elif choice == '2':
            print("Game rules: ...")  # Add actual rules here
        elif choice == '3':
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please try again.")
