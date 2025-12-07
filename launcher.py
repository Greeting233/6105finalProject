import subprocess
import webbrowser
import time
import os

# 你的 Anaconda Python
PYTHON_PATH = "/opt/anaconda3/bin/python"

# 💡 使用绝对路径 (不会随 .app 移动而失效)
APP_PATH = "/Users/greaterlofter/Desktop/finalproject/app.py"

print("Starting Streamlit App...")
print(f"Using Python: {PYTHON_PATH}")
print(f"App Path: {APP_PATH}")

# 启动 Streamlit
process = subprocess.Popen([PYTHON_PATH, "-m", "streamlit", "run", APP_PATH])

# 等待启动
time.sleep(2)

# 打开浏览器
webbrowser.open("http://localhost:8501")

process.wait()