import keyboard
import time
import json
from termcolor import colored

from other.cls import cls

from menu.scenes.about import about
from menu.scenes.play import play

from rich.console import Console
from rich.panel import Panel

console = Console()
about = about()
play = play()

class menu:
    def __init__(self):
        self.rawActions = []
        self.actions = []
        self.descriptions = []
        self.curIndex = 0

    def display(self, actions, descriptions, curIndex):
        cls()

        print(colored(r"                     __", "blue"))
        print(colored(r"                    /\ \__", "blue"))
        print(colored(r" _____    __  __    \ \ ,_\   __  __      ___     ___     ___     ___", "blue"))
        print(colored(r"/\ '__`\ /\ \/\ \    \ \ \/  /\ \/\ \    /'___\  / __`\  / __`\ /' _ `\ ", "blue"))
        print(colored(r"\ \ \L\ \\ \ \_\ \    \ \ \_ \ \ \_\ \  /\ \__/ /\ \ \ \/\ \ \ \/\ \/\ \ ", "blue"))
        print(colored(r" \ \ ,__/ \/`____ \    \ \__\ \/`____ \ \ \____\\ \____/\ \____/\ \_\ \_\ ", "blue"))
        print(colored(r"  \ \ \/   `/___/> \    \/__/  `/___/> \ \/____/ \/___/  \/___/  \/_/\/_/ ", "blue"))
        print(colored(r"   \ \_\      /\___/              /\___/ ", "blue"))
        print(colored(r"    \/_/      \/__/               \/__/ ", "blue"))
        print("")

        for i, action in enumerate(actions):
            if i == curIndex:
                print(f"> {action} - {descriptions[i]}")
            else:
                print(colored(f"  {action}", "blue"))

    def check(self):
        self.display(self.actions, self.descriptions, self.curIndex)

        while True:
            if keyboard.is_pressed("up"):
                self.curIndex = (self.curIndex - 1) % len(self.actions)
                self.display(self.actions, self.descriptions, self.curIndex)
                time.sleep(0.05)

            if keyboard.is_pressed("down"):
                self.curIndex = (self.curIndex + 1) % len(self.actions)
                self.display(self.actions, self.descriptions, self.curIndex)
                time.sleep(0.05)

            if keyboard.is_pressed("enter"):
                if self.curIndex == 0:
                    play.start()
                elif self.curIndex == 1:
                    pass
                elif self.curIndex == 2:
                    pass
                elif self.curIndex == 3:
                    about.start()
                    break
                elif self.curIndex == 4:
                    cls()
                    quit()

    def start(self):
        with open("data/actions/actions.json") as file:
            rawActions = json.load(file)

        for data in rawActions["actions_menu"]:
            self.actions.append(data["name"])
            self.descriptions.append(data["description"])

        cls()
        self.check()