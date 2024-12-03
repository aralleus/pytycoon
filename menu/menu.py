import json
import keyboard
import time
from termcolor import colored
from other.cls import cls
from other.center import center
from other.center_block import center_block
from menu.scenes.play import play
from menu.scenes.about import about

play = play()
about = about()

class menu:
    def __init__(self):
        self.rawActions = []
        self.actions = []
        self.descriptions = []
        self.curIndex = 0

    def display(self, actions, descriptions, curIndex):
        cls()

        logo = r"""
                             __
                            /\ \__
         _____    __  __    \ \ ,_\   __  __      ___     ___     ___     ___
        /\ '__`\ /\ \/\ \    \ \ \/  /\ \/\ \    /'___\  / __`\  / __`\ /' _ `\
        \ \ \ \ \\ \ \_\ \    \ \ \_ \ \ \_\ \  /\ \__/ /\ \ \ \/\ \ \ \/\ \/\ \
         \ \ ,__/ \/`____ \    \ \__\ \/`____ \ \ \____\\ \____/\ \____/\ \_\ \_\
          \ \ \/   `/___/> \    \/__/  `/___/> \ \/____/ \/___/  \/___/  \/_/\/_/
           \ \_\      /\___/              /\___/
            \/_/      \/__/               \/__/ 
        """
        print(colored(center_block(logo), "blue"))

        for i, action in enumerate(actions):
            if i == curIndex:
                if descriptions and descriptions[i]:
                    print(center(f"> {action} - {descriptions[i]}"))
                else:
                    print(center(f"> {action}"))
            else:
                print(center(colored(f"  {action}", "blue")))

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
        self.actions = []
        self.descriptions = []
        self.curIndex = 0

        with open("data/actions/actions.json", "r", encoding="utf-8") as file:
            rawActions = json.load(file)
        for data in rawActions["actions_menu"]:
            self.actions.append(data["name"])
            self.descriptions.append(data.get("description", None))

        cls()
        self.check()