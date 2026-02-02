import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from assistant.system_status import SystemStatus

jarvis = SystemStatus()
status = jarvis.get_status()

print("\nJARVIS SYSTEM STATUS:\n")
for k, v in status.items():
    print(f"{k.upper():15}: {v}")
