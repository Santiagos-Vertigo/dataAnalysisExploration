import logging
from pathlib import Path

# Step 1 Set up logging
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s - %(message)s')

# Step 2 Validate Folder
def validate_folder(folder_path):
    folder = Path(folder_path)
    if folder.exists() and folder.is_dir():
        logging.info(F"The folder '{folder_path}' exists and is valid.")
    else:
        logging.error(f"The folder '{folder_path}' does not exist or is not a directory.")

# Step 3: Main Execution
def main():
    setup_logging()
    folder_path = input("Enter the folder path to validate: ")
    validate_folder(folder_path)
    

if __name__ == "__main__":
    main()
