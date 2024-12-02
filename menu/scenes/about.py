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

        print(colored(r"           __                          __", "blue"))
        print(colored(r"          /\ \                        /\ \__", "blue"))
        print(colored(r"   __     \ \ \____    ___    __  __  \ \ ,_\ ", "blue"))
        print(colored(r" /'__`\    \ \ '__`\  / __`\ /\ \/\ \  \ \ \/", "blue"))
        print(colored(r"/\ \ \.\_   \ \ \ \ \/\ \ \ \\ \ \_\ \  \ \ \_", "blue"))
        print(colored(r"\ \__/.\_\   \ \_,__/\ \____/ \ \____/   \ \__\ ", "blue"))
        print(colored(r" \/__/\/_/    \/___/  \/___/   \/___/     \/__/", "blue"))

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