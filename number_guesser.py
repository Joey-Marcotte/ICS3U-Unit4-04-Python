#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program gets the user to guess a number

import random


def main():

    while True:
        # input
        number_guessed = input("pick a number between 0-9:")
        try:
            number_guessed_as_number = int(number_guessed)
            # process
            if number_guessed_as_number == (random.randint(0, 9+1)):
                # output
                print("You win, you guessed the number")
                break
            else:
                print("wrong, try again")
        except(ValueError):
            print("Not a valid number inputted")


if __name__ == "__main__":
    main()
