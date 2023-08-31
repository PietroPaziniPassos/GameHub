import random

def play():
    welcome()
    secret_word = load_secret_word()
    right_letters = ["_" for letter in secret_word]
    wrong_letters = []
    wrong_guesses = 0
    print(right_letters)

    while(wrong_guesses <= 7 and "_" in right_letters):
        guess = input("Guess a letter").strip().upper()
        if (guess in secret_word):
            right_guess(guess, right_letters, secret_word)
        else:
            wrong_letters.append(guess)
            wrong_guesses += 1
            draw_hangman(wrong_guesses, wrong_letters)
        print(right_letters)
    if ("_" not in right_letters):
        print_winner_message(secret_word)
    else:
        print_looser_message(secret_word)

def welcome():
    print("******************************")
    print("***Welcome to hangman game!***")
    print("******************************")
    print()

def load_secret_word():
    fruits_file = open(r"c:\Users\ppppa\OneDrive\Documents\VSCodes\Python\Python_GameHub\Words\Fruits.txt", "r")
    names_file = open(r"c:\Users\ppppa\OneDrive\Documents\VSCodes\Python\Python_GameHub\Words\Names.txt", "r")
    animals_file = open(r"c:\Users\ppppa\OneDrive\Documents\VSCodes\Python\Python_GameHub\Words\Animals.txt", "r")
    fruits_list = []
    names_list = []
    animals_list = []
    all_words_list = []
    for line in fruits_file:
        line = line.strip()
        fruits_list.append(line)
        all_words_list.append(line)
    for line in names_file:
        line = line.strip()
        names_list.append(line)
        all_words_list.append(line)
    for line in animals_file:
        line = line.strip()
        animals_list.append(line)
        all_words_list.append(line)
    fruits_file.close()
    names_file.close()
    animals_file.close()
    randomNumber = random.randrange(0, len(all_words_list))
    secret_word = all_words_list[randomNumber].upper()
    if (randomNumber in range(0, len(fruits_list))):
        print("It's a fruit name!")
    elif (randomNumber in range(len(fruits_list), len(fruits_list) + len(names_list)+1)):
        print("It's a personal name!")
    elif (randomNumber in range(len(fruits_list) + len(names_list), len(fruits_list) + len(names_list) + len(animals_list)+2)):
        print("It's an animal name!")
    return secret_word

def right_guess(guess, right_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (guess == letter):
            right_letters[index] = letter
        index += 1

def draw_hangman(wrong_guesses, wrong_letters):
    print("  _______     ")
    print(" |/      |    ")

    if(wrong_guesses == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(wrong_guesses == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(wrong_guesses == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(wrong_guesses == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(wrong_guesses == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(wrong_guesses == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (wrong_guesses == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    print("Wrong letters: ", wrong_letters)
    print()

def print_winner_message(secret_word):
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
    print("The word was ", secret_word)

def print_looser_message(secret_word):
    print("You lost!")
    print("The word was ", secret_word)
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

if(__name__ == "__main__"):
    play()