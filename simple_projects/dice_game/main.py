import random

player_wins = 0
cpu_wins = 0

while True:



    answer = input("Roll Dice! {y/n}: ")

    if answer.lower() == "y":

        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print(f"Player: ({num1},{num2})")

        cpu1 = random.randint(1, 6)
        cpu2 = random.randint(1, 6)
        print(f"CPU: ({cpu1},{cpu2})")

        player_num = num1 + num2
        cpu_num = cpu1 + cpu2

        if player_num > cpu_num:
            print("Player Won!")
            player_wins += 1
        else:
            print("CPU Won!")
            cpu_wins += 1

    elif answer == "n":
        print(f"Player Wins: {player_wins}")
        print(f"CPU Wins: {cpu_wins}")
        print("Thanks for playing!")
        break

    else:
        print("Invalid Choice!")

