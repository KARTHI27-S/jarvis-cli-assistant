from datetime import datetime, timedelta

class ReminderManager:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, text, minutes):
        due_time = datetime.now() + timedelta(minutes=minutes)

        self.reminders.append({
            "text": text,
            "due": due_time
        })

    def get_due_reminders(self):
        now = datetime.now()
        due = [r for r in self.reminders if r["due"] <= now]
        return due
    def clear_reminders(self):
        self.reminders = []
        self.save_reminders()
