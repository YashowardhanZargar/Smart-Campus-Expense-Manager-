from datetime import datetime


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Value must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def get_valid_date(prompt):
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Enter date in YYYY-MM-DD format.")


def get_valid_choice(prompt, minimum, maximum):
    while True:
        try:
            choice = int(input(prompt))
            if minimum <= choice <= maximum:
                return choice
            print(f"Enter a number from {minimum} to {maximum}.")
        except ValueError:
            print("Please enter a valid integer.")
