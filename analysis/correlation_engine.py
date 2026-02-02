from datetime import datetime,timedelta

class CorrelationEngine:
    def __init__(self, window_minutes=5):
        self.window = timedelta(minutes=window_minutes)
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        self._cleanup_old_events()

    def _cleanup_old_events(self):
        now = datetime.utcnow()
        self.events = [
            e for e in self.events
            if now - datetime.fromisoformat(e["timestamp"]) <= self.window
        ]

    def analyze(self):
        auth_failures = [
            e for e in self.events if e["type"] == "auth_fail"
        ]

        total_attempts = sum(
            e["details"].get("attempts", 0) for e in auth_failures
        )

        if total_attempts >= 5:
            return {
                "pattern": "AUTH_BRUTE_FORCE_SUSPECTED",
                "severity": "HIGH",
                "reason": f"{total_attempts} failed login attempts within time window"
            }

        if total_attempts >= 3:
            return {
                "pattern": "MULTIPLE_AUTH_FAILURES",
                "severity": "MEDIUM",
                "reason": f"{total_attempts} failed login attempts detected"
            }

        return {
            "pattern": "NORMAL",
            "severity": "LOW",
            "reason": "No suspicious patterns detected"
        }
