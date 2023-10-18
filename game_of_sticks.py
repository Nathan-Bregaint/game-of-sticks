import time
import random

#########################################################################
# function name : computer
# inputs :  #### nb_stick: the number of sticks between the two players.
            #### stick_max: the maximum number that can be picked.

# output:   #### picked: the number of sticks picked by the player.
# function : returns the best pick to make
#########################################################################

  # You can propose another computer function


def computer(nb_stick, stick_max):
    picked = 0
    s = stick_max + 1
    t = (nb_stick - s) % (stick_max + 1)
    while (t != 0):
        s -= 1
        t = (nb_stick - s) % (stick_max + 1)
        picked = s - 1
    if (picked == 0):
        picked = 1
    return picked


#########################################################################
# function name : main
# function : initiate the game and organize it.
#########################################################################
def main():
    # initialization of variables:
    nb_stick_max = 3  # number of sticks that can be picked by the player
    nb_stick_left = random.randint(10, 40);  # number of sticks left
    picked = 0  # number of the sticks picked py the player
    who = random.randint(0, 1)  # who plays 0=User --- 1=PC

    print("---- Game of Sticks ----")
    print(f"Initial number of sticks : {nb_stick_left}")
    print(f"Maximum number of sticks to pick at each turn : {nb_stick_max}")
    print('Computer starts' if who == 1 else 'You start')

    while nb_stick_left > 0:
        if who == 0:
            display_sticks(nb_stick_left)
            picked = int(input(f"How many sticks do you want to pick? (1 to {nb_stick_max}): "))
            if 1 <= picked <= nb_stick_max:
                nb_stick_left -= picked
                print(f"\nYou picked {picked} sticks, {nb_stick_left} sticks left.")
                who = 1
            else:
                print(f"Please pick 1 to {nb_stick_max} sticks")

        else:  # Computer's turn
            picked = computer(nb_stick_left, nb_stick_max)
            nb_stick_left -= picked
            time.sleep(1)
            print(f"\nThe computer picked {picked} sticks, {nb_stick_left} sticks left.\n")
            who = 0

    if who == 0:
        print("You win !")
    else:
        print("The computer wins !")

def display_sticks(n):
    print("o  " * n)
    print("|  " * n)


main()

