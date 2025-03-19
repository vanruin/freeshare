import os

def create_files():
    directory = "/sdcard/boostphere/"
    files = ["FRAACCOUNT.txt", "FRAPAGES.txt", "RPWACCOUNT.txt"]
    
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Create files if they don't exist
    for file in files:
        with open(os.path.join(directory, file), 'a') as f:
            pass  # Just ensures the file exists

if __name__ == "__main__":
    create_files()
    print("Files created successfully!")