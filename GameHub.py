import Hangman
import GuessTheNumber
import GuessTheWord

def welcome():
    print("*************************")
    print("***Welcome to GameHub!***")
    print("*************************")
    print()

def choose_game():
    welcome()
    print("(1) Hangman (2) Guess the number (3) Guess the word")

    while(True):
        game_number = int(input("Choose a game: "))

        if(game_number == 1):
            print("Loading Hangman...")
            Hangman.play()
            break
        elif(game_number == 2):
            print("Loading Guess the number...")
            GuessTheNumber.play()
            break
        elif(game_number == 3):
            print("Loading Guess the word")
            GuessTheWord.play()
            break
        else:
            print("You have to choose a number between 1 and 3!")
            continue

if(__name__ == "__main__"):
    choose_game()