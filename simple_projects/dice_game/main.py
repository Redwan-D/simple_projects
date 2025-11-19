import random

while True:

    answer = input("Roll Dice! {y/n}: ")

    if answer.lower() == "y":
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print(f"({num1},{num2})")

    elif answer == "n":
        print("Thanks for playing!")
        break

    else:
        print("Invalid Choice!")

