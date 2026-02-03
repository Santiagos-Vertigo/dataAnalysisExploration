from pathlib import Path

data_dir = Path('../data')
for file in data_dir.glob('*.csv'):
    print(file.name)


print("\n**** All JSON files ****\n")


for file in data_dir.glob('*.json'):
    print(file.name)