import json
import os
import zipfile
import keyboard
import time
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from other.cls import cls
from menu.menu import menu
from other.game.errors import throw_error

console = Console()

class mloader:
    def __init__(self, mods_directory: str = "./mods"):
        self.mods_directory = mods_directory
        os.makedirs(self.mods_directory, exist_ok=True)

    def load_mod(self, mod_file: str) -> Optional[dict]:
        mod_path = os.path.join(self.mods_directory, mod_file)
        try:
            with zipfile.ZipFile(mod_path, 'r') as z:
                if "config.json" in z.namelist():
                    with z.open("config.json") as config_file:
                        mod_data = json.load(config_file)
                    return mod_data
                else:
                    throw_error("Mod Load Issue", "No config.json found in mod!")
                    return None
        except zipfile.BadZipFile:
            throw_error("Mod Load Issue", "Failed processing .zip file, it might be corrupted.")
            return None
        except Exception as e:
            throw_error("Mod Load Issue", "Failed loading mod!")
            return None

    def fetch_mods(self):
        mods = []
        for mod_file in os.listdir(self.mods_directory):
            if mod_file.endswith('.zip'):
                mod_data = self.load_mod(mod_file)
                if mod_data:
                    mods.append({
                        "mod_file": mod_file,
                        "mod_dispname": mod_data.get("display_name", "N/A"),
                        "mod_name": mod_data.get("name", "N/A"),
                        "mod_version": mod_data.get("version", "N/A"),
                        "mod_author": mod_data.get("author", "N/A"),
                        "mod_minver": mod_data.get("minGameVersionRequired", None)
                    })
        return mods

    def display_mods(self):
        cls()
        mods = self.fetch_mods()
        if not mods:
            console.print(Panel("[red]No mods found.[/red]", title="Mod Error", style="red"))
            return

        cls()
        cur_index = 0

        def render():
            cls()
            panels = []
            for i, mod in enumerate(mods):
                mod_display_name = mod["mod_dispname"]
                mod_name = mod["mod_name"]
                mod_version = mod["mod_version"]
                mod_author = mod["mod_author"]
                mod_minver = mod["mod_minver"]
                content = f"Inner name: {mod_name}\nVersion: {mod_version}\nAuthor: {mod_author}\nMinimal Game Version Required: {mod_minver}"
                style = "dim white" if i != cur_index else "bold blue"
                panels.append(Panel(content, title=f"Mod {i}: {mod_display_name}", style=style))

            console.print(*panels, sep="\n")

        render()
        console.print("To navigate use Up and Down. To select use Enter.")

        while True:
            if keyboard.is_pressed("up"):
                cur_index = (cur_index - 1) % len(mods)
                render()
                time.sleep(0.05)

            if keyboard.is_pressed("down"):
                cur_index = (cur_index + 1) % len(mods)
                render()
                time.sleep(0.05)

            if keyboard.is_pressed("enter"):
                render()
                continue

            elif keyboard.is_pressed("esc"):
                console.print("[bold red]Exiting mod selection.[/bold red]")
                time.sleep(1.25)
                self.menu.start()
                break