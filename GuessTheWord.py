import random

def play():
    welcome()
    secret_word = load_secret_word()
    print(secret_word)
    defaut_list = ["_" for letter in secret_word]
    attempts = 5
    for i in range(0, attempts):
        print(defaut_list)
    print()
    attempts -= 1
    guesses_list = []
    while(attempts >= 0):
        guess = input("Guess the word: ").upper()
        if(guess.isalpha()):
            print()
            if(verify_correct(guess, secret_word)):
                word_list = []
                for letter in guess:
                    word_list.append(letter)
                guesses_list.append(word_list)
                for word in guesses_list:
                    print(word)
                for i in range(0, attempts):
                    print(defaut_list)
                print_winner_message(secret_word)
                break
            attempts -= 1
            word_list = []
            for letter in guess:
                word_list.append(letter)
            guesses_list.append(word_list)
            for word in guesses_list:
                print(word)
            if(attempts >= 0):
                print(verify_next(guess, secret_word))
            for i in range(0, attempts):
                print(defaut_list)
            if(attempts >= 0):
                print("You got correct the follow letters: ")
                print(verify_letters(guess, secret_word))
            print()
        else:
            print("You need to guess a word, only alphanumeric characters are allowed!")
    if(attempts < 0):
        print_looser_message(secret_word)
    
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

def verify_next(guess, secret_word):
    index = 0
    new_list = ["_","_","_","_","_"]
    while(index < 5):
        if (guess[index] == secret_word[index]):
            new_list[index] = guess[index]
        else:
            new_list[index] = "_"
        index += 1
    return new_list

def verify_letters(guess, secret_word):
    right_letters = []
    for letter in guess:
        for letters in secret_word:
            if(letter == letters and letter not in right_letters):
                right_letters.append(letter)
    return right_letters

def verify_correct(guess, secret_word):
    index = 0
    while(index < 5):
        if (guess[index] == secret_word[index]):
            index += 1
        else:
            return False
            break
    if(index == 5):
        return True        

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