import os

# Ask for user input
data = input("Enter the account data to save: ")

# Target file path
file_path = "/sdcard/boostphere/FRAACCOUNT.txt"

try:
    # Ensure the folder exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write (append) to the file
    with open(file_path, "a") as f:
        f.write(data + "\n")

    print("✅ Data saved successfully.")

except Exception as e:
    print(f"❌ Failed to save data: {e}")
