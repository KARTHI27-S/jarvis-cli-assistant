from core.reasoning_engine import ReasoningEngine
from monitoring.auth_monitor import AuthFailureMonitor
from analysis.correlation_engine import CorrelationEngine
from core.decision_layer import DecisionLayer


class JarvisEngine:
    def __init__(self):
        self.monitor = AuthFailureMonitor()
        self.brain = ReasoningEngine()
        self.correlator = CorrelationEngine(window_minutes=5)
        self.decision_layer = DecisionLayer()

    def run_once(self):
        event = self.monitor.check_failures()

        if event:
            self.correlator.add_event(event)

        correlation = self.correlator.analyze()
        decision = self.decision_layer.present(correlation)

        return {
            "correlation": correlation,
            "decision": decision
        }
