import logging
import sys
from pathlib import Path

MAX_SIZE_BYTES = 5 * 1024 * 1024 # 5 MB

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

def fail(message: str):
    logging.error(message)
    sys.exit(1)

def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent

def validate_data_dir(data_dir: Path):
    if not data_dir.exists():
        fail(f"Missing data directory: {data_dir}")
    if not data_dir.is_dir():
        fail(f"Data path is not a directory: {data_dir}")

def classify_file(path: Path):
    """
    Return classification string based on extention
    """
    ext = path.suffix.lower()

    if ext in {".csv", ".json", ".parquet", ".arrow", ".tsv", ".xml"}:
        return "data"
    if ext in {".png", ".jpg", ".jpeg"}:
        return "binary"
    return "unknown"

def analyze_file(path: Path, stats: dict):
    stats["total"] += 1

    size = path.stat().st_size
    file_type = classify_file(path)

    # Count by type
    stats["type_counts"][file_type] += 1

    if size == 0:
        logging.warning(f"Empty file detected: {path.name}")
        stats["warnings"] += 1

    if size > MAX_SIZE_BYTES:
        logging.warning(
            f"Large file (>5MB): {path.name} ({size} bytes)"
        )
        stats["warnings"] += 1
        stats["large_files"] += 1

    if file_type == "unknown":
        logging.warning(f"Unknown file type: {path.name}")
        stats["warnings"] += 1
        stats["unknown_types"] += 1

    elif file_type == "binary":
        logging.info(f"Binary asset detected: {path.name}")

    else:
        logging.info(f"Data file detected: {path.name}")

def main():
    setup_logging()

    root = get_project_root()
    data_dir = root / "data"

    logging.info(f"Validating data directory: {data_dir}")
    validate_data_dir(data_dir)

    stats = {
        "total" : 0,
        "warnings" : 0,
        "large_files" : 0,
        "unknown_types" : 0,
        "type_counts": {
        "data": 0,
        "binary": 0,
        "unknown": 0
        }
    }

    for i in data_dir.iterdir():
        if i.is_file():
            analyze_file(i, stats)
    
    


    logging.info("File type distribution:")
    for file_type in ("data", "binary", "unknown"):
        logging.info(f"  {file_type}: {stats['type_counts'][file_type]}")


if __name__ == "__main__":
    main()
