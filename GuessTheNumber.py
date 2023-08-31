import random

def welcome():
    print("*********************************")
    print("Welcome to Guess the number game!")
    print("*********************************")

def play():
    welcome()
    secret_number = load_secret_number()
    total_guesses = choose_game_difficulty()

def load_secret_number():
    secret_number = random.randrange(1,101)
    return secret_number

def choose_game_difficulty():
    print("*Choose the game difficulty*")
    print("(1) Easy (2) Medium (3) Hard")

    difficulty = int(input("Game difficulty: "))
    
    if(difficulty == 1):
        total_guesses = 20
    elif(difficulty == 2):
        total_guesses = 10
    else:
        total_guesses = 5
    return total_guesses