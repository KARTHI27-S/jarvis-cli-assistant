import platform
import shutil
from datetime import datetime

try:
    import psutil
except ImportError:
    psutil = None


class SystemStatus:
    def get_status(self):
        status = {}

        # Time & OS
        status["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status["os"] = platform.system() + " " + platform.release()

        # CPU & Memory
        if psutil:
            status["cpu_usage"] = f"{psutil.cpu_percent()}%"
            status["ram_usage"] = f"{psutil.virtual_memory().percent}%"

            battery = psutil.sensors_battery()
            if battery:
                status["battery"] = f"{battery.percent}%"
            else:
                status["battery"] = "Not available"
        else:
            status["cpu_usage"] = "psutil not installed"
            status["ram_usage"] = "psutil not installed"
            status["battery"] = "psutil not installed"

        # Disk
        total, used, free = shutil.disk_usage("/")
        status["disk_free"] = f"{free // (1024**3)} GB free"

        return status
