import subprocess
from datetime import datetime

class AuthFailureMonitor:
    def check_failures(self):
        try:
            result = subprocess.run(
                ["journalctl", "-u", "ssh", "--since", "1 minute ago", "--no-pager"],
                capture_output=True,
                text=True,
                check=True
            )

            fail_count = 0
            for line in result.stdout.splitlines():
                if "Failed password" in line:
                    fail_count += 1

            if fail_count > 0:
                return {
                    "type": "auth_fail",
                    "source": "system",
                    "timestamp": datetime.utcnow().isoformat(),
                    "details": {
                        "attempts": fail_count
                    }
                }

            return None

        except Exception as e:
            return {
                "type": "monitor_error",
                "source": "system",
                "timestamp": datetime.utcnow().isoformat(),
                "details": {
                    "error": str(e)
                }
            }
