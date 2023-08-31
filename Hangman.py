import random

def play():
    welcome()

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
