import random

def play():
    welcome()
    secret_number = load_secret_number()
    total_attempts = choose_game_difficulty()
    attempt = 1

    while(attempt <= total_attempts):
        print("Attempt {} of {}".format(attempt, total_attempts))

        guess = input("Input a number between 1 and 100: ")
        guess = int(guess)
        if(guess > 0 and guess < 101):
            if(guess == secret_number):
                print_winner_message(secret_number)
                break
            else:
                if(guess > secret_number):
                    print("It's not it! Try a smaller number.")
                elif(guess < secret_number):
                    print("It's not it! Try a bigger number.")
            attempt += 1
        else:
            print("You can only guess a number between 1 and 100")
    if(attempt > total_attempts):
        print_looser_message(secret_number)

def welcome():
    print("*********************************")
    print("Welcome to Guess the number game!")
    print("*********************************")
    print()

def load_secret_number():
    secret_number = random.randrange(1,101)
    return secret_number

def choose_game_difficulty():
    print("*Choose the game difficulty*")
    print("(1) Easy (2) Medium (3) Hard")
    while(True):
        difficulty = int(input("Game difficulty: "))

        if(difficulty == 1):
            total_guesses = 20
            break
        elif(difficulty == 2):
            total_guesses = 10
            break
        elif(difficulty == 3):
            total_guesses = 5
            break
        else:
            print("You can only choose 1, 2 or 3!")
            continue
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
    print("You lost!")
    print("    _______________        ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\   ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/    ")
    print(" |   XXX       XXX   |     ")
    print(" |                   |     ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |       ")
    print("   | I I I I I I I |       ")
    print("   |  I I I I I I  |       ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print("The number was ", secret_number)

if(__name__ == "__main__"):
    play()