import random

options = ["Rock", "Paper", "Scissors"]

def compare(player, cpu):

    if player == cpu:
        print("Player: " + player + "  CPU: " + cpu)
        print("Tie!")
    elif player == "Rock" and cpu == "Scissors":
        print("Player: " + player + "  CPU: " + cpu)
        print("Player Wins!")
    elif player == "Paper" and cpu == "Rock":
        print("Player: " + player + "  CPU: " + cpu)
        print("Player Wins!")
    elif player == "Scissors" and cpu == "Paper":
        print("Player: " + player + "  CPU: " + cpu)
        print("Player Wins!")
    else:
        print("Player: " + player + "  CPU: " + cpu)
        print("CPU Wins!")


while True:

    cpu = random.choice(options)

    rps = input("Select Rock/Paper/Scissors [Q to quit]: ")

    if rps.lower() == "q":
        print("Thanks for playing!")
        break

    if rps.capitalize() not in options:
        print("Invalid Choice!")
    else:
        compare(rps.capitalize(), cpu)
