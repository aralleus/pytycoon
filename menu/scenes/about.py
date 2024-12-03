from termcolor import colored
import keyboard
import time

from other.center import center
from other.center_block import center_block
from other.cls import cls
from rich.console import Console
console = Console()

class about:
    def start(self):
        from menu.menu import menu
        menu = menu()
        cls()

        logo = r"""
                   __                          __
                  /\ \                        /\ \__
           __     \ \ \____    ___    __  __  \ \ ,_\
         /'__`\    \ \ '__`\  / __`\ /\ \/\ \  \ \ \/
        /\ \ \.\_   \ \ \ \ \/\ \ \ \\ \ \_\ \  \ \ \_
        \ \__/.\_\   \ \_,__/\ \____/ \ \____/   \ \__\
         \/__/\/_/    \/___/  \/___/   \/___/     \/__/
        """

        print(colored(center_block(logo), "blue"))
        print("")
        print(center("Made using Python 3.10"))
        print(center("By aralleus."))
        print(center("Use Escape to return to menu"))

        while True:
            if keyboard.is_pressed("esc"):
                cls()
                menu.start()
                return
        time.sleep(0.1)