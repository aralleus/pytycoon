import json
import os
import keyboard
import time
from typing import Optional

from other.cls import cls
from rich.console import Console
from rich.panel import Panel

console = Console()

class save:
    def __init__(self, save_directory: str = "data/saves"):
        self.save_directory = save_directory
        os.makedirs(self.save_directory, exist_ok=True)

    def create_save(self, slot: int, player_name: str, company_name: str, player_level: int, company_level: int, player_cash: int = 1000) -> bool:
        save_path = os.path.join(self.save_directory, f"save{slot}.json")
        save_data = {
            "save": {
                "player_name": player_name,
                "player_cash": player_cash,
                "player_level": player_level,
                "company_name": company_name,
                "company_level": company_level
            }
        }
        try:
            with open(save_path, "w") as save_file:
                json.dump(save_data, save_file, indent=4)
            return True
        except Exception as e:
            console.print(Panel(f"Error creating save: {e}", title="Creating Error", title_align="left", style="red"))
            return False

    def load_save(self, slot: int) -> Optional[dict]:
        save_path = os.path.join(self.save_directory, f"save{slot}.json")
        try:
            if os.path.exists(save_path):
                with open(save_path, "r") as save_file:
                    save_data = json.load(save_file)
                return save_data
            else:
                console.print(Panel(f"No save found in slot {slot}.", title="Load Error", style="red"))
                return None
        except Exception as e:
            console.print(Panel(f"Error loading save: {e}", title="Load Error", style="red"))
            return None

    def delete_save(self, slot: int) -> bool:
        save_path = os.path.join(self.save_directory, f"save{slot}.json")
        try:
            if os.path.exists(save_path):
                os.remove(save_path)
                return True
            else:
                console.print(Panel(f"No save found in slot {slot} to delete.", title="Deleting Error", style="red"))
                return False
        except Exception as e:
            console.print(Panel(f"Error deleting save: {e}", title="Deleting Error", style="red"))
            return False

    def fetch_save_slots(self):
        slots = []
        for slot in range(3):
            save_path = os.path.join(self.save_directory, f"save{slot}.json")
            if os.path.exists(save_path):
                try:
                    with open(save_path, "r") as save_file:
                        save_data = json.load(save_file)["save"]
                        slots.append({
                            "slot": slot,
                            "data": save_data
                        })
                except Exception:
                    slots.append({
                        "slot": slot,
                        "data": {"error": True, "message": "[yellow]Warning: Could not load slot."}
                    })
            else:
                slots.append({
                    "slot": slot,
                    "data": None
                })
        return slots

    # TODO: should i make buttons instead of selecting?
    def display_saves(self):
        from menu.menu import menu
        menu = menu()

        cls()
        slots = self.fetch_save_slots()
        cur_index = 0

        def render():
            cls()
            panels = []
            for i, slot in enumerate(slots):
                if slot["data"] is None:
                    content = "No save file found"
                    style = "dim white" if i != cur_index else "white"
                elif "error" in slot["data"]:
                    content = slot["data"]["message"]
                    style = "yellow" if i != cur_index else "bold yellow"
                else:
                    save_data = slot["data"]
                    content = (f"Player: {save_data['player_name']}\nLevel: {save_data['player_level']}\nCash: {save_data['player_cash']}\nCompany: {save_data['company_name']}\nCompany Level: {save_data['company_level']}")
                    style = "green" if i != cur_index else "white"

                panels.append(Panel(content, title=f"Slot {i}", style=style))

            console.print(*panels, sep="\n")

        render()
        console.print("To navigate use [purple]Up, Down. [white]For selecting use [purple]Enter.")

        while True:
            if keyboard.is_pressed("up"):
                cur_index = (cur_index - 1) % len(slots)
                render()
                time.sleep(0.05)

            elif keyboard.is_pressed("down"):
                cur_index = (cur_index + 1) % len(slots)
                render()
                time.sleep(0.05)

            elif keyboard.is_pressed("enter"):
                selected_slot = slots[cur_index]
                if selected_slot["data"] is None:
                    console.print("[yellow]This slot is empty.")
                elif "error" in selected_slot["data"]:
                    console.print(Panel(selected_slot["data"]["message"], title=f"Slot {cur_index}", style="red"))
                else:
                    save_data = selected_slot["data"]
                    console.print(Panel(f"Selected Slot {cur_index}:\nPlayer: {save_data['player_name']}\nLevel: {save_data['player_level']}\nCash: {save_data['player_cash']}\nCompany: {save_data['company_name']}\nCompany Level: {save_data['company_level']}",style="bold green"))
                    break
                time.sleep(0.2)

            elif keyboard.is_pressed("esc"):
                console.print("[bold red]Exiting save selection.[/bold red]")
                time.sleep(1.25)
                menu.start()