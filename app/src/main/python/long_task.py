# long_task.py
import time

progress = 0

def long_running_task():
    for i in range(100):
        global progress
        progress = i + 1
        time.sleep(0.1)  

def get_progress():
    return progress

