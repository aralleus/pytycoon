from termcolor import colored
import keyboard
import time
from other.cls import cls

class about:
    def start(self):
        from menu.menu import menu
        menu = menu()
        cls()

        version = "build1"

        print(colored("    ___       / __        ___                __  ___", "green"))
        print(colored("  //   ) )   //   ) )   //   ) )   //   / /   / /", "green"))
        print(colored(" //   / /   //   / /   //   / /   //   / /   / /", "green"))
        print(colored("((___( (   ((___/ /   ((___/ /   ((___( (   / /", "green"))

        print(f"Version: {version}")
        print("----------")
        print("Made in " + colored("Pyt", "yellow") + colored("hon", "blue"))

        time.sleep(0.4)
        print(" ")
        print("Press Escape to go back.")

        while True:
            if keyboard.is_pressed("esc"):
                cls()
                menu.start()
                return
        time.sleep(0.1)