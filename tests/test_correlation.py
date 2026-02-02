import sys
import os
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from analysis.correlation_engine import CorrelationEngine

engine = CorrelationEngine(window_minutes=5)

# Simulate multiple auth failure events
events = [
    {
        "type": "auth_fail",
        "source": "system",
        "timestamp": datetime.utcnow().isoformat(),
        "details": {"attempts": 1}
    },
    {
        "type": "auth_fail",
        "source": "system",
        "timestamp": datetime.utcnow().isoformat(),
        "details": {"attempts": 2}
    }
]

for e in events:
    engine.add_event(e)

result = engine.analyze()
print(result)
