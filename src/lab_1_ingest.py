import sys
import logging
from pathlib import Path

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_args():
    if len(sys.argv) != 2:
        logging.error("Usage: python lab_1_ingest.py <data_folder>")
        logging.info("Example: python lab_1_ingest.py ../data")
        sys.exit(1)

def validate_file(data_folder):
    if not data_folder.exists() or not data_folder.is_dir():
        logging.error(f"Data folder '{data_folder}' does not exist or is not a directory.")
        sys.exit(1) 

def main():
    setup_logging()
    validate_args()

    input_path = Path(sys.argv[1])
    logging.info(f"Validating files in {input_path}...")
    validate_file(input_path)
if __name__ == "__main__":
    main()