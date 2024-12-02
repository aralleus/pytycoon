import keyboard
import time
from termcolor import colored
import json
from other.cls import cls
from other.game.data.save import save

save = save()
class play:
    def __init__(self):
        self.actions = []
        self.rawActions = []
        self.descriptions = []
        self.curIndex = 0

    def display(self, actions, descriptions, curIndex):
        cls()
        for i, action in enumerate(actions):
            if i == curIndex:
                print(f"> {action} - {descriptions[i]}")
            else:
                print(colored(f"  {action}", "blue"))
    def check(self):
        from menu.menu import menu
        menu = menu()

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
                    pass
                elif self.curIndex == 1:
                    save.display_saves()
                elif self.curIndex == 2:
                    menu.start()

    def start(self):
        cls()

        with open("data/actions/actions.json") as file:
            rawActions = json.load(file)

        for data in rawActions["actions_play"]:
            self.actions.append(data["name"])
            self.descriptions.append(data["description"])

        self.check()