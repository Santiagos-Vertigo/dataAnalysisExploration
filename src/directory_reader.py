import logging
import sys
from pathlib import Path

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"

    )

def fail(message: str):
    logging.error(message)
    sys.exit(1)



def explore_directory(target: Path):
    file_count = 0

    for i in target.iterdir():
        if i.is_file():
            file_count += 1
            logging.info(f"[FILE] {i.name} ({i.stat().st_size} bytes)")
        elif i.is_dir():
            logging.info(f"[DIR] {i.name}")
        else:
            logging.warning(f"[UNKNOWN] {i.name}")

    if file_count == 0:
        logging.warning("Dierectory contains no files")


def main():
    setup_logging()

    target = Path("../data").resolve()
    logging.info(f"Entering directory: {target}")

    if not target.exists():
        fail("Target directory does not exist")

    if not target.is_dir():
        fail("Target path is not a directory")

    try:
        explore_directory(target)
    except PermissionError as e:
        fail(f"Permissiom error while accessing {e}")
    
    logging.info("Reconnaisance complete.")

if __name__ == "__main__":
    main()
