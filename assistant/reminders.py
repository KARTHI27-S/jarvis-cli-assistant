from datetime import datetime, timedelta
import os

REMINDERS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "reminders.txt")


class ReminderManager:
    def add_reminder(self, minutes, message):
        trigger_time = datetime.now() + timedelta(minutes=minutes)
        with open(REMINDERS_FILE, "a") as f:
            f.write(f"{trigger_time.isoformat()}|{message}\n")

    def check_reminders(self):
        if not os.path.exists(REMINDERS_FILE):
            return []

        now = datetime.now()
        pending = []
        remaining = []

        with open(REMINDERS_FILE, "r") as f:
            for line in f:
                time_str, message = line.strip().split("|", 1)
                reminder_time = datetime.fromisoformat(time_str)

                if reminder_time <= now:
                    pending.append(message)
                else:
                    remaining.append(line)

        # Rewrite file with remaining reminders
        with open(REMINDERS_FILE, "w") as f:
            f.writelines(remaining)

        return pending
