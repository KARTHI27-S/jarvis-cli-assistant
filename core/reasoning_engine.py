from datetime import datetime

class ReasoningEngine:
    def _init_(self):
        self.rules_loaded = True

    def evaluate_event(self, event):
        event_type = event.get("type")
        details = event.get("details")

        if event_type == "auth_fail":
            return self._handle_auth_failure(details)

        return {
            "severity": "INFO",
            "decision": "LOG",
            "explanation": "Unknown event type, logged for review"
        }

    def _handle_auth_failure(self, details):
        attempts = details.get("attempts", 0)

        if attempts < 3:
            return {
                "severity": "LOW",
                "decision": "LOG",
                "explanation": "Few failed login attempts"
            }
        elif attempts < 6:
            return {
                "severity": "MEDIUM",
                "decision": "ALERT",
                "explanation": "Multiple failed login attempts detected"
            }
        else:
            return {
                "severity": "HIGH",
                "decision": "REVIEW",
                "explanation": "Possible brute-force attack"
            }
