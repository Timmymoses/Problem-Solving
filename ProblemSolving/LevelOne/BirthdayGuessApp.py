month = "February"
year = 2020
correct_date = 24

guess = int(input(f"Guess the birthdate (1-28) for {month}, {year}: "))
while guess != correct_date:
    print("Incorrect Guess!")
    guess = int(input(f"Guess again: "))
print("Correct Guess!")
