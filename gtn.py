#Random Librery
import random
import os

#Global Constants
equals = ("=========================================")
clear = lambda: os.system('cls')

def menu(op):
    if op == 1:
        return

    elif op == 2:
        clear()
        print(equals)
        print("|--------------INSTRUCCIONS-------------|")
        print(f"{equals}\n\n")

        print("Your goal is to guess the number generated by the computer. How? It's very simple.")
        print("The computer will generate a number between the number 1 to X number.")
        print("The number X will be a number chosen by the user to assign a limit. \n\n")

        print("Then you should try to guess the number and in each attempt the game will")
        print('give you a clue if you are near or far from the number.\n\n')

        print(equals)
        print("|---------------GOOD LUCK!--------------|")
        print(f"{equals}\n")

        input('Press any key to continue...')
        menu(1)

    elif op == 3:
        clear()
        print("\n|---- Thanks for playing :D ---|\n\n")
        quit()

def main():
    clear()
    print(equals)
    print("|-----Welcome to 'Guess the Number'-----|")
    print(f"{equals}\n")

    print("1. Play")
    print("2. Instruccions")
    print("3. Exit")

    option = int(input("\nPlease choose a option to continue: "))
    
    menu(option)

main()