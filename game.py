import simulation


def run():
    play = True
    while play:
        # pass arguments to simulate() function from stdin
        # check if input is in valid format and range
        # repeat until input is valid
        # print("\n")
        while True:
            num = input("Insert no. of attacking armies (red): ")
            try:
                red_armies = int(num)
                if 100001 > red_armies > 1:
                    break
                else:
                    print("Invalid input: no. of attacking armies must be an integer "
                          "greater than 1 and not greater than 100,000.")
                    continue
            except ValueError:
                print("Invalid input: no. of attacking armies must be in the integer format.")
        # print(red_armies)

        while True:
            num = input("Insert no. of defending armies (blue): ")
            try:
                blue_armies = int(num)
                if 100001 > blue_armies > 0:
                    break
                else:
                    print("Invalid input: no. of defending armies must be an integer "
                          "greater than 0 and not greater than 100,000.")
                    continue
            except ValueError:
                print("Invalid input: no. of defending armies must be in the integer format.")
        # print(blue_armies)

        while True:
            num = input("Red attacks while at least n armies are on the ground. Insert n: ")
            try:
                red_stops_at = int(num)
                if red_armies + 1 > red_stops_at > -1:
                    break
                else:
                    print("Invalid input: n must be an integer "
                          "greater than 0 and not greater than the no. of red armies.")
                    continue
            except ValueError:
                print("Invalid input: n must be in the integer format.")
        # print(red_stops_at)

        while True:
            num = input("Insert no. of matches to simulate: ")
            try:
                n_simulation = int(num)
                if 0 < n_simulation < 1000001:
                    break
                else:
                    print("Invalid input: no. of matches to simulate must be an integer "
                          "greater than 0 and not greater than 1,000,000.")
                    continue
            except ValueError:
                print("Invalid input: no. of matches to simulate must be in the integer format.")
        # print(n)

        print("\n... computing the odds ...\n")
        red_armies = int(red_armies)  # red armies
        blue_armies = int(blue_armies)  # blue armies
        red_stops_at = int(red_stops_at)  # red stops attack at
        n_simulation = int(n_simulation)  # no. of attack simulations
        red_wins = simulation.simulate(red_armies, blue_armies, red_stops_at, n_simulation)
        red_wins_perc = round(red_wins / n_simulation * 100.000, 4)
        blue_wins = n_simulation - red_wins
        blue_wins_perc = round(100 - red_wins_perc, 4)
        print("Red's chances of winning: " + str(red_wins_perc) + "%")
        print("Blue's chances of winning: " + str(blue_wins_perc) + "%")
        print("Out of " + str(n_simulation) + " games: ")
        print("- Red wins " + str(int(red_wins)) + " games")
        print("- Blue wins " + str(int(blue_wins)) + " games")
        print("")
        key = input("Digit 'r' to repeat the simulation or digit 'q' to exit: ")
        while key != 'q' and key != 'r':
            key = input("Invalid input.\n"
                        "Digit 'r' to repeat the simulation or digit 'q' to exit: ")
        if key == 'q':
            play = False
