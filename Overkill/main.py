from time import sleep
from encrypt import encrypt
from decrypt import decrypt
from sys import platform
import os

choices = ["Encrypt", "Decrypt"]


def main():
    displayChoices(choices)
    userInput = input("> ")
    while not ["q", "quit"].__contains__(userInput.lower()):
        while not int(userInput) in range(0, len(choices)):
            print("Unknown token: " + userInput)
            userInput = input("> ")

        if userInput == "0":
            load("encrypt", encrypt)
        else:
            load("decrypt", decrypt)

        displayChoices(choices)
        userInput = input("> ")
    print("Thanks for using Overkill")


def load(choice, callback):
    clear()
    for x in range(1, 5):
        for i in ("⠻", "⠽", "⠾", "⠷", "⠯", "⠟"):
            sleep(0.1)
            if x == 4:
                clear()
                callback()
                return
            else:
                print(f'Loading {choice} ' + i, end='\r')


def displayChoices(choices):
    print("What would you like to do (q to quit): ")
    [print(f"{index} - {choice}") for index, choice in enumerate(choices)]


def clear():
    os.system("cls" if platform == "windows" else "clear")


if __name__ == '__main__':
    clear()
    main()
