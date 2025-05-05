import keyboard
from datetime import datetime
import csv

# Prompt user for metadata
user = input("Enter User Name: ")
lamp_version = input("Enter Lamp Version: ")
stone_version = input("Enter Stone Version: ")

# Generate dynamic CSV filename
csv_filename = f"user_breath_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Write metadata to the CSV file
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["User", user])
    writer.writerow(["Lamp Version", lamp_version])
    writer.writerow(["Stone Version", stone_version])
    writer.writerow([])  # Blank line for separation
    writer.writerow(["Timestamp", "Time Since Last Press (ms)"])  # Header row

# Initialize the last press time
last_press_time = None

def on_spacebar_press(event):
    global last_press_time
    timestamp = datetime.now()
    time_since_last_press = (
        (timestamp - last_press_time).total_seconds() * 1000 if last_press_time else None
    )
    last_press_time = timestamp

    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            f"{time_since_last_press:.2f}" if time_since_last_press is not None else "N/A"
        ])

def main():
    keyboard.on_press_key('space', on_spacebar_press)
    print("Spacebar logger is running. Press ESC to stop.")
    keyboard.wait('esc')

if __name__ == "__main__":
    main()