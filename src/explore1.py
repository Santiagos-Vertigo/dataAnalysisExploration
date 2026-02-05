from pathlib import Path

# Create a path object for the data dirctory
data_dir = Path("../data")
print(f"\nPath to directory: {data_dir}")

# Get the directory of the current script
script_dir = Path(__file__).parent
print(f"\nCurrent script directory: {script_dir}")

# Check if the data directory exists
print(f"\nDoes the data directory exist? {data_dir.exists()}")

# Check if data directory is a directory
print(f"\nIs data_dir a directory? {data_dir.is_dir()}")

# Check if specific file exists
example_file = data_dir /  "airports.csv"
print(f"\nIs airports.csv a file? {example_file.is_file()}")

# Create a new directory
output_dir = script_dir /   "output"
output_dir.mkdir(parents=True, exist_ok=True)
print(f"\nOutput directory created: {output_dir}")

# List all items in data directory
print("\nItems in data directory:\n")
for item in data_dir.iterdir():
    print(f"{item} (File: {item.is_file()}, Directory: {item.is_dir()})")

# List all files and directories
print("\nAll items in data directory:\n")
for item in data_dir.glob("*"):
    print(item)

# List only CSV files
print("\nCSV files in data directory:\n")
for csv_file in data_dir.glob("*.csv"):
    print(csv_file)

# Join paths using "/"
joined_path = script_dir / ".." / "data" / "airports.csv"
print(f"\nJoined path: {joined_path.resolve()}\n")