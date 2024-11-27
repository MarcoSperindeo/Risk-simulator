import os
import random
import sys
from pathlib import Path


def simulate(red_tanks: int, blue_tanks: int, stop_at: int, n: int) -> float:
    red_wins = 0.0
    blue_wins = 0.0
    i = 0
    while i < n:
        res = simulate_attack(red_tanks, blue_tanks, stop_at)
        red_tanks_end = res[len(res) - 1]["red_tanks"]
        blue_tanks_end = res[len(res) - 1]["blue_tanks"]

        if red_tanks_end <= 1 or red_tanks_end <= stop_at:
            blue_wins += 1
        elif blue_tanks_end == 0:
            red_wins += 1
        i += 1

        # prints the results of each attacking stage for the last simulated attack
        if i == n:
            print_simulation(res)

    return red_wins


def simulate_attack(red_tanks: int, blue_tanks: int, stop_at: int) -> list:
    stages = []
    cnt_stage = 0
    stage_dict = dict(n=cnt_stage, red_tanks=red_tanks, blue_tanks=blue_tanks, red_dice=[], blue_dice=[])
    stages.append(stage_dict)

    # print("red tanks: " + str(red_tanks))
    # print("blue tanks: " + str(blue_tanks))
    # print("stop at: " + str(stop_at))

    # red attacks while either 1\ has at least 1 tank left or 2\ has at least stop_at tanks left
    while red_tanks > 1 and blue_tanks > 0 and red_tanks > stop_at:
        # counter of attack stages
        cnt_stage += 1
        # print("\nstage no.: " + str(cnt_stage))

        # case 1: attack w/ 3, defend w/ 3
        if red_tanks >= 4 and blue_tanks >= 3:
            r, b = 3, 3

        # case 2: attack w/ 3, defend w/ 2
        if red_tanks >= 4 and blue_tanks == 2:
            r, b = 3, 2

        # case 3: attack w/ 3, defend w/ 1
        elif red_tanks >= 4 and blue_tanks == 1:
            r, b = 3, 1

        # case 4: attack w/ 2, defend w/ 3
        elif red_tanks == 3 and blue_tanks >= 3:
            r, b = 2, 3

        # case 5: attack w/ 2, defend w/ 2
        elif red_tanks == 3 and blue_tanks == 2:
            r, b = 2, 2

        # case 6: attack w/ 2, defend w/ 1
        elif red_tanks == 3 and blue_tanks == 1:
            r, b = 2, 1

        # case 7: attack w/ 1, defend w/ 3
        elif red_tanks == 2 and blue_tanks >= 3:
            r, b = 1, 3

        # case 8: attack w/ 1, defend w/ 2
        elif red_tanks == 2 and blue_tanks == 2:
            r, b = 1, 2

        # case 9: attack w/ 1, defend w/ 1
        elif red_tanks == 2 and blue_tanks == 1:
            r, b = 1, 1

        # print("no. of red dices: " + str(r))
        # print("no. of blue dices: " + str(b))

        # roll dices
        red_dice = roll_dice(r)
        blue_dice = roll_dice(b)
        # sort dices from higher to lower
        red_dice.sort(reverse=True)
        blue_dice.sort(reverse=True)
        # print("red dice: " + str(red_dice))
        # print("blue dice: " + str(blue_dice))

        # compare dices and decrement armies
        for i in range(min(r, b)):
            if blue_dice[i] >= red_dice[i]:
                red_tanks -= 1
            else:
                blue_tanks -= 1

        # print("red tanks: " + str(red_tanks) + ", blue tanks: " + str(blue_tanks))
        stage_dict = dict(n=cnt_stage, red_tanks=red_tanks, blue_tanks=blue_tanks, red_dice=red_dice,
                          blue_dice=blue_dice)
        stages.append(stage_dict)

    return stages


def roll_dice(n: int) -> list:
    res = []
    for i in range(n):
        res.insert(i, random.randint(1, 6))
    return res


def print_simulation(res):
    myfile = r"C:\Users\Utente\PycharmProjects\risk_calculator\resources\simulator.txt"
    # If file exists, delete it
    if os.path.isfile(myfile):
        os.remove(myfile)
    orig_stdout = sys.stdout
    f = open(myfile, 'w')
    sys.stdout = f
    for j in range(len(res)):
        for key, value in res[j].items():
            print(key, ' : ', value)
        print("\n")
    sys.stdout = orig_stdout
    f.close()