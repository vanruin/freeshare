import os

def main():
    # Fixed target file
    file_path = "/sdcard/boostphere/FRAACCOUNT.txt"

    # Prompt user for the data to save
    data = input("Enter (or paste) the account data to save: ").strip()

    try:
        # Make sure the parent directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Open in append mode and write the data
        with open(file_path, "a") as f:
            f.write(data + "\n")

        print(f"✅ Data saved successfully to {file_path}")

    except Exception as e:
        print(f"❌ Failed to save data: {e}")

if __name__ == "__main__":
    # On Android/Termux you may need to run `termux-setup-storage` first
    main()
