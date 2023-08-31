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
        print_win_message(secret_word)
    else:
        print_looser_message(secret_word)


def welcome():
    print("******************************")
    print("***Welcome to hangman game!***")
    print("******************************")
    print()

def load_secret_word():
    fruits_file = open("Words/Fruits.txt", "r")
    names_file = open("Words/Names.txt", "r")
    animals_file = open("Words/Animals.txt", "r")
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
        print("É uma fruta!")
    elif (randomNumber in range(len(fruits_list), len(fruits_list) + len(names_list)+1)):
        print("É o nome de uma pessoa!")
    elif (randomNumber in range(len(fruits_list) + len(names_list), len(fruits_list) + len(names_list) + len(animals_list)+2)):
        print("É um animal!")
    return secret_word

def right_guess(guess, right_letters, secret_word):
    pass

def draw_hangman(wrong_guesses, wrong_letters):
    pass

def print_win_message(secret_word):
    pass

def print_looser_message(secret_word):
    pass