import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
)

DATA_DIR = os.path.join(BASE_DIR, "data")
NOTES_FILE = os.path.join(DATA_DIR, "notes.txt")


class NotesManager:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)

        if not os.path.exists(NOTES_FILE):
            with open(NOTES_FILE, "w"):
                pass

    def add_note(self, note):
        with open(NOTES_FILE, "a") as f:
            f.write(note + "\n")

    def get_notes(self):
        with open(NOTES_FILE, "r") as f:
            return [line.strip() for line in f.readlines() if line.strip()]

    def clear_notes(self):
        with open(NOTES_FILE, "w"):
            pass
