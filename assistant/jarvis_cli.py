import sys
import os
import datetime
from notes.notes_manager import NotesManager
from reminders.reminder_manager import ReminderManager
reminders = ReminderManager()
from core.jarvis_engine import JarvisEngine

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from assistant.system_status import SystemStatus

def show_menu():
    print("\n=== JARVIS COMMAND INTERFACE ===")
    print("1. Show system status")
    print("2. Show time & date")
    print("3. Add a note")
    print("4. Show notes")
    print("5. Add a reminder")
    print("6. SOC Analyst Dashboard")
    print("7. Exit")
    print("8. Clear all notes")

def handle_choice(choice):
    global notes, reminders
    if choice == "1":
        jarvis = SystemStatus()
        status = jarvis.get_status()

        print("\nJARVIS SYSTEM STATUS")
        print("--------------------")
        for key, value in status.items():
            print(f"{key:<12}: {value}")

    elif choice == "2":
        now = datetime.datetime.now()
        print(f"\nJARVIS: Current time is {now.strftime('%Y-%m-%d %H:%M:%S')}")

    elif choice == "3":
        note = input("\nJARVIS: What should I remember? ")
        notes = NotesManager()
        notes.add_note(note)
        print("JARVIS: Noted successfully.")

    elif choice == "4":
        notes = NotesManager()
        all_notes = notes.get_notes()

        if not all_notes:
            print("\nJARVIS: No notes found.")
        else:
            print("\nJARVIS NOTES")
            print("------------")
            for line in all_notes:
                print(line.strip())
    elif choice == "5":
        try:
            minutes = int(input("Enter reminder time (in minutes): "))
            text = input("Enter reminder text: ")

            reminders.add_reminder(text, minutes)

            print(f"JARVIS: Reminder set for {minutes} minutes from now.")

        except ValueError:
            print("JARVIS: Please enter a valid number of minutes.")
    elif choice == "6":
        print("\nJARVIS SOC ANALYST DASHBOARD")
        print("----------------------------")

        engine = JarvisEngine()
        result = engine.run_once()

        correlation = result.get("correlation", {})
        decision = result.get("decision", {})

        print(f"Overall Risk     : {correlation.get('severity')}")
        print(f"Analysis         : {correlation.get('reason')}")
        print(f"Pattern Detected : {correlation.get('pattern')}")

        print("\nRecommendation:")
        actions = decision.get("recommended_actions", [])
        if actions:
            for act in actions:
                print(f"- {act}")
        else:
            print("- No action required")

        approval = decision.get("requires_approval", False)
        print(f"\nHuman Approval Required : {'YES' if approval else 'NO'}")

    elif choice == "7":
        print("\nJARVIS: Shutting down. Have a productive day.")
        sys.exit(0)
    elif choice == "8":
        notes.clear_notes()
        print("JARVIS: All notes cleared successfully.")
    else:
        print("\nJARVIS: Invalid command. Please try again.")


def main():
    print("JARVIS online.")
    print("Awaiting your command, Karthi.")


    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()
        handle_choice(choice)
        # ✅ Check reminders every cycle
        due = reminders.get_due_reminders() or []

        if not due:
            print("No reminders yet.")
        else:
            for reminder in due:
               print(f"- {reminder['text']} (due: {reminder['due']})")
if __name__ == "__main__":
    main()
