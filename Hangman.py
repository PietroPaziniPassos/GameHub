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