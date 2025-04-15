import subprocess
import time
import csv
import psutil
from datetime import datetime

# Function to get GPU power using powermetrics
def get_gpu_power():
    try:
        result = subprocess.run(
            ["sudo", "powermetrics", "-n", "1"],
            capture_output=True,
            text=True
        )
        for line in result.stdout.splitlines():
            if "GPU Power:" in line:
                return line.split(":")[1].strip().split(" ")[0]  # Gets the number (in mW)
    except Exception as e:
        print(f"Error reading GPU power: {e}")
    return "N/A"
# Main logging function
def log_performance(duration=60, interval=5, output_file="minecraft_performance.csv"):
    print("Logging performance data...")
    end_time = time.time() + duration

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "CPU_Usage (%)", "Memory_Usage (%)", "GPU_Power (mW)"])

        while time.time() < end_time:
            cpu_usage = psutil.cpu_percent()
            memory_usage = psutil.virtual_memory().percent
            gpu_power = get_gpu_power()

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([timestamp, cpu_usage, memory_usage, gpu_power])
            print(f"{timestamp} | CPU: {cpu_usage}% | RAM: {memory_usage}% | GPU Power: {gpu_power} mW")

            time.sleep(interval)

if __name__ == "__main__":
    log_performance()
