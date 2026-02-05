import logging
from pathlib import Path

# Step 1: Set up logging
def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s -%(levelname)s -%(message)s')

# Step 2: List files in folder
def list_files(folder_path):
    folder = Path(folder_path)
    if folder.exists and folder.is_dir():
        logging.info(f"Listing files in folder: {folder_path}")
        for item in folder.iterdir():
            if item.is_file():
                logging.info(f"File: {item.name}")
            elif item.is_dir():
                logging.info(f"Subdirectory: {item.name}")
    else:
        logging.error(f"The folder '{folder_path}' does not exist")


# Step 3: Main execution
def main():
    setup_logging()
    folder_path = input("Enter the folder path to list files:")
    list_files(folder_path)



if __name__ == "__main__":
    main()