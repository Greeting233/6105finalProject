import subprocess
import webbrowser
import time
import os

PYTHON_PATH = "/opt/anaconda3/bin/python"
APP_PATH = "/Users/greaterlofter/Desktop/finalproject/app.py"

print("Starting Streamlit App...")
print(f"Using Python: {PYTHON_PATH}")
print(f"App Path: {APP_PATH}")

process = subprocess.Popen([PYTHON_PATH, "-m", "streamlit", "run", APP_PATH])

time.sleep(2)

webbrowser.open("http://localhost:8501")

process.wait()
