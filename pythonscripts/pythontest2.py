import psutil
import time
import csv

# Log CPU & RAM usage
def log_performance(duration=60, interval=5, output_file="minecraft_performance.csv"):
    print("Logging performance data...")
    end_time = time.time() + duration

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "CPU_Usage", "Memory_Usage"])

        while time.time() < end_time:
            cpu_usage = psutil.cpu_percent()
            memory_usage = psutil.virtual_memory().percent
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([timestamp, cpu_usage, memory_usage])
            print(f"{timestamp} | CPU: {cpu_usage}% | RAM: {memory_usage}%")
            
            time.sleep(interval)

if __name__ == "__main__":
    log_performance()
