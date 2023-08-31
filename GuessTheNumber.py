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