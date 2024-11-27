import game
from pyfiglet import Figlet


if __name__ == "__main__":
    intro = Figlet(font='slant')
    print(intro.renderText("RISK SIMULATOR"))
    game.run()