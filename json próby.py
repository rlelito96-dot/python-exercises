
import json
from sys import excepthook


def save_file(shopping_list, file_name = "shopping_list.json"):
    """Saving list to .json file"""
    try:
        with open(file_name, "w", encoding = "utf-8") as f:
            json.dump(shopping_list, f, indent = 4)
        print("\nFile has been saved!")
    except IOError as e:
        print(f"Error saving file: {e}")




def load_file(file_name="shopping_list.json"):
    """Loading list of strings from .json file"""
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("File is corrupted or not valid JSON.")
        return []


shopping_list = []
load = load_file()

while True: