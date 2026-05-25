#!/usr/bin/env python3

"""
Module: Meal Cost Calculator

This module calculates the total meal cost including tip and tax.
It reads input values from standard input and prints the rounded total cost.

Author: Your Name
Date: 2026-05-25
"""

import sys


def solve(meal_cost: float, tip_percent: int, tax_percent: int) -> None:
    """
    Calculate and print the total meal cost.

    The total cost is computed by adding:
    - Tip: (tip_percent % of meal_cost)
    - Tax: (tax_percent % of meal_cost)

    The final result is rounded to the nearest integer.

    Args:
        meal_cost (float): The base cost of the meal.
        tip_percent (int): Tip percentage to be applied.
        tax_percent (int): Tax percentage to be applied.

    Returns:
        None: Prints the rounded total cost.
    """
    tip_amount = (meal_cost * tip_percent) / 100
    tax_amount = (meal_cost * tax_percent) / 100

    total_cost = round(meal_cost + tip_amount + tax_amount)

    print(f"Total cost: {total_cost}")


def main() -> None:
    """
    Entry point for the program.

    Reads input from standard input and calls the solve function.
    """
    meal_cost = float(input("Enter the meal cost: ").strip())
    tip_percent = int(input("Enter the tip percentage: ").strip())
    tax_percent = int(input("Enter the tax percentage: ").strip())

    solve(meal_cost, tip_percent, tax_percent)


if __name__ == "__main__":
    main()