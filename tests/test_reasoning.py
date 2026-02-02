import sys
import os

# Add project root to Python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from core.reasoning_engine import ReasoningEngine


engine = ReasoningEngine()

event = {
    "type": "auth_fail",
    "details": {
        "attempts": 5
    }
}

result = engine.evaluate_event(event)
print(result)
