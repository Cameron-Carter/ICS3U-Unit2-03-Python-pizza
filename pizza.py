#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on April 2021
# This program calculates the total price of a pizza based on diameter

import constants


def main():
    # This function calculates total pizza cost

    # Input
    diameter = int(input("Enter the diameter of your pizza (inches): "))

    # Process
    subtotal = (
        diameter * constants.COST_PER_INCH + constants.LABOR + constants.RENT
    )
    total = subtotal * constants.HST + subtotal

    # Output
    print("A {0} inch pizza costs ${1:,.2f}.".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
