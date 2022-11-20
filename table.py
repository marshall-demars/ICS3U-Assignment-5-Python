#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program calculates multiplication tables for user input

import constants

def main():
    # This program calculates multiplication tables for user input
    counter = 0
    product = 1

    # Input
    input_as_string = input("\nEnter a positive number: ")

    # Process and Output
    try:
        input_as_int = int(input_as_string)
        if input_as_int < 0:
            print("\nPlease enter a positive number. ")
        else:
            while counter < constants.TABLE_END:
                counter = counter + 1
                product = input_as_int * counter
                print(
                    "\n{0} x {1} = {2}.".format(
                        input_as_string, counter, product
                    )
                )

    except Exception:
        print("\nInvalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
