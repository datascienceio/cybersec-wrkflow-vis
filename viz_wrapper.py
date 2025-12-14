"""
Simple Kedro-Viz wrapper - runs Kedro-Viz directly on port 
import subprocess
import sys

if __name__ == "__main__":
    cmd = [
        "kedro", "viz", "run",
        "--host=0.0.0.0",
        "--port=5000",
        "--no-browser",
        "--pipeline=cybersecurity",
        "--include-hooks"
    ]
    
    try:
        subprocess.run(cmd, check=False)
    except KeyboardInterrupt:
        sys.exit(0)
