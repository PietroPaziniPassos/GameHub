import Hangman
import GuessTheNumber
import GuessTheWord

def welcome():
    print("*************************")
    print("***Welcome to GameHub!***")
    print("*************************")
    print()

def choose_game():
    print("(1) Hangman (2) Guess the number (3) Guess the word")

    game_number = int(input("Choose a game: "))

    if(game_number == 1):
        print("Loading Hangman...")
        Hangman.play()
    elif(game_number == 2):
        print("Loading Guess the number...")
        GuessTheNumber.play()
    elif(game_number == 3):
        print("Loading Guess the word")
        GuessTheWord.play()