import pandas as pd
import webbrowser
import keyboard
import time

# Use the simplified file
file_path = 'file_csv.csv'

try:
    df = pd.read_csv(file_path)
    # Ensure we only take names that aren't empty
    users = df['screen_name'].dropna().tolist()
except FileNotFoundError:
    print(f"Error: {file_path} not found. Please ensure the file exists.")
    exit()

index = 0
total = len(users)

print(f"--- Script Ready! ({total} users loaded) ---")
print("Press 'P' to open the NEXT profile.")
print("Press 'ESC' to exit.")

while index < total:
    if keyboard.is_pressed('p'):
        user = users[index]
        url = f"https://x.com/{user}"
        
        print(f"[{index + 1}/{total}] Opening: @{user}")
        webbrowser.open(url)
        
        index += 1
        
        # Wait for the user to release the key to avoid "rapid fire" opening
        while keyboard.is_pressed('p'):
            time.sleep(0.1)
            
    if keyboard.is_pressed('esc'):
        print("Exiting...")
        break

    time.sleep(0.01) # Low CPU usage

print("End of list or script terminated.")