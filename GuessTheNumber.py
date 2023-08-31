import random

def welcome():
    print("*********************************")
    print("Welcome to Guess the number game!")
    print("*********************************")

def play():
    welcome()
    secret_number = load_secret_number()
    total_guesses = choose_game_difficulty()

    