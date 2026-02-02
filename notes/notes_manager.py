import os

NOTES_FILE = os.path.expanduser("~/JARVIS/data/notes.txt")

class NotesManager:
    def __init__(self):
        # Ensure file exists
        if not os.path.exists(NOTES_FILE):
            open(NOTES_FILE, "w").close()

    def add_note(self, note):
        with open(NOTES_FILE, "a") as f:
            f.write(note + "\n")

    def get_notes(self):
        with open(NOTES_FILE, "r") as f:
            notes = [line.strip() for line in f.readlines() if line.strip()]
        return notes
