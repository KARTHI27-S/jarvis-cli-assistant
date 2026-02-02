from datetime import datetime
import os

NOTES_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "notes.txt")


class NotesManager:
    def add_note(self, text):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(NOTES_FILE, "a") as f:
            f.write(f"[{timestamp}] {text}\n")

    def get_notes(self):
        if not os.path.exists(NOTES_FILE):
            return []

        with open(NOTES_FILE, "r") as f:
            return f.readlines()
