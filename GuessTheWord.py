import random

def play():
    welcome()
    secret_word = load_secret_word()
    
def welcome():
    print("*******************************")
    print("Welcome to Guess the word game!")
    print("*******************************")
    print()

def load_secret_word():
    fruits_file = open("Words\Fruits.txt", "r")
    animals_file = open("Words/Animals.txt", "r")
    names_file = open("Words/names.txt", "r")
    words_list = []
    for line in fruits_file:
        line = line.strip()
        words_list.append(line)
    for line in names_file:
        line = line.strip()
        words_list.append(line)
    for line in animals_file:
        line = line.strip()
        words_list.append(line)
    fruits_file.close()
    names_file.close()
    animals_file.close()
    randomNumber = random.randrange(0, len(words_list))
    secret_word = words_list[randomNumber].upper()
    return secret_word