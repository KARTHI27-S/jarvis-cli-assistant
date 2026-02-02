import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from core.jarvis_engine import JarvisEngine

engine = JarvisEngine()

print("Running JARVIS with human-in-the-loop decision layer...")
result = engine.run_once()

print("\nCorrelation Result:")
print(result["correlation"])

print("\nDecision Presented to Human:")
for k, v in result["decision"].items():
    print(f"{k}: {v}")
