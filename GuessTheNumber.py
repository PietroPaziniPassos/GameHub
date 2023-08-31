import random

def play():
    welcome()
    secret_number = load_secret_number()
    total_attempts = choose_game_difficulty()
    attempt = 0

    while(attempt <= total_attempts):
        print("Attempt {} of {}".format(attempt, total_attempts))

        guess = input("Input a number between 1 and 100: ")
        guess = int(guess)

        if(guess == secret_number):
            print_winner_message(secret_number)
            break
        else:
            if(guess > secret_number):
                print("It's not it! Try a smaller number.")
            elif(guess < secret_number):
                print("It's not it! Try a bigger number.")
    if(attempt > total_attempts):
        print_looser_message(secret_number)

def welcome():
    print("*********************************")
    print("Welcome to Guess the number game!")
    print("*********************************")

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

def print_winner_message(secret_number):
    print("Congratulation, you won!  ")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("The number was ", secret_number)

def print_looser_message(secret_number):
    pass