import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from core.jarvis_engine import JarvisEngine

engine = JarvisEngine()

print("Running JARVIS engine...")
result = engine.run_once()
print(result)
