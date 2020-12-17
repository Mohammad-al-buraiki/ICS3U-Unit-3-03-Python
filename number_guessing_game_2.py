# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is Number Guessing Game

import random

pyguess = random.randint(1, 100)


def main():
    # this function asks the user to guess the right number

    # input
    guessing = int(input("Guess the right number between 1-100: "))
    print("")

    # process
    if guessing == pyguess:
        # a number between 1 and 100
        # output
        print("You got it right 😃, the number was {}".format(pyguess))
    else:
        print("You got it wrong 😞, the number was {}".format(pyguess))
        print("Try again ...")


if __name__ == "__main__":
    main()
