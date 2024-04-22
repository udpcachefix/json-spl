import json
import sys
import os

def split_json(file_path, output_dir, lines_per_file):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for i in range(0, len(lines), lines_per_file):
        part = lines[i:i + lines_per_file]
        part_file_path = os.path.join(output_dir, f'part{i // lines_per_file + 1}.json')

        with open(part_file_path, 'w') as f:
            f.writelines(part)

if __name__ == '__main__':
    json_file = sys.argv[1]
    output_folder = sys.argv[2]
    split_json(json_file, output_folder, 500)
