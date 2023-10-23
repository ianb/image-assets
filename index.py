#!/usr/bin/env python3

import os
import json

def generate_index_json(root_directory):
    # Walk through each directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_directory):
        # If there are no files in the directory, skip
        if not filenames:
            continue

        files_info = []

        # For each file, collect its name and size
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if not filepath.endswith(".jpg"):
                continue
            size = os.path.getsize(filepath)
            files_info.append({"filename": filename, "size": size})

        # Write the collected information to an "index.json" file in the current subdirectory
        if dirpath == ".":
            continue
        with open(os.path.join(dirpath, "index.json"), "w") as json_file:
            json.dump({"files": files_info}, json_file, indent=4)

if __name__ == "__main__":
    root_directory = "."  # Current directory
    generate_index_json(root_directory)
