import subprocess
import time

# Replace with your actual Minecraft path
MINECRAFT_PATH = "/Applications/Minecraft.app"

def launch_minecraft():
    print("Launching Minecraft...")
    subprocess.run(["open", MINECRAFT_PATH])
    time.sleep(10)  # Wait for Minecraft to load

if __name__ == "__main__":
    launch_minecraft()
