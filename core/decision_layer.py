class DecisionLayer:
    def present(self, correlation_result):
        severity = correlation_result.get("severity")
        reason = correlation_result.get("reason")

        decision = {
            "severity": severity,
            "summary": reason,
            "recommended_actions": [],
            "requires_approval": True
        }

        if severity == "LOW":
            decision["recommended_actions"].append(
                "Continue monitoring. No action required."
            )
            decision["requires_approval"] = False

        elif severity == "MEDIUM":
            decision["recommended_actions"].extend([
                "Notify administrator",
                "Increase monitoring frequency",
                "Review SSH access logs"
            ])

        elif severity == "HIGH":
            decision["recommended_actions"].extend([
                "Temporarily block source IP (manual)",
                "Disable SSH password login",
                "Inspect system for compromise"
            ])

        return decision
