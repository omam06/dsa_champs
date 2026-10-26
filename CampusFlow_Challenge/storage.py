import json
import os

FILENAME = "tickets.json"

def load_tickets():
    if not os.path.exists(FILENAME):
        return []
    
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:   # the specific error Python throws when a JSON file is corrupted or empty
        print("Error: File is corrupt. Starting afresh.")

def save_tickets(tickets):
    try:
        with open(FILENAME, "w") as file:     #Store tickets in tickets.json using Python's json module.
            json.dump(tickets, file, indent=4)
    except Exception as e:
        print(f"Error saving tickets: {e}")
