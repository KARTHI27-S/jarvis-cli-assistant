import os

NOTES_FILE = os.path.expanduser("~/JARVIS/data/notes.txt")

class NotesManager:
    def _init_(self, file_path=None):
        os.makedirs(os.path.dirname(NOTES_FILE), exist_ok=True)
        if not os.path.exists(NOTES_FILE):
            open(NOTES_FILE, "w").close()

    def add_note(self, note):
        with open(NOTES_FILE, "a") as f:
            f.write(note + "\n")

    def get_notes(self):
        with open(NOTES_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]

    def clear_notes(self):
        open(NOTES_FILE, "w").close()
