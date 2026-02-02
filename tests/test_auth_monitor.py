import sys
import os
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from monitoring.auth_monitor import AuthFailureMonitor

monitor = AuthFailureMonitor()

print("Monitoring auth failures for 30 seconds...")
time.sleep(30)

event = monitor.check_failures()
print(event)
