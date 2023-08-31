import random

def play():
    welcome()
    secret_word = load_secret_word()
    right_letters = ["_" for letter in secret_word]
    for i in range(0, 5):
        print(right_letters)
    
def welcome():
    print("*******************************")
    print("Welcome to Guess the word game!")
    print("*******************************")
    print()

def load_secret_word():
    words_file = open("Words/Five_letters_words.txt", "r")
    words_list = []
    for line in words_file:
        line = line.strip()
        words_list.append(line)
    words_file.close()
    randomNumber = random.randrange(0, len(words_list))
    secret_word = words_list[randomNumber].upper()
    return secret_word