"""
Task 5 - OS File Manager
- Copy all .txt files into backup folder
"""

import os
import shutil

def file_manager():
    while True:
        path = input("Enter a directory path: ").strip()

        # remove quotes if user enters them
        if path.startswith("'") and path.endswith("'"):
            path = path[1:-1]

        if os.path.isdir(path):
            backup_path = os.path.join(path, "backup")
            os.makedirs(backup_path, exist_ok=True)

            txt_files = [f for f in os.listdir(path) if f.endswith(".txt") and os.path.isfile(os.path.join(path, f))]

            copied_count = 0
            for file in txt_files:
                source = os.path.join(path, file)
                destination = os.path.join(backup_path, file)
                shutil.copy2(source, destination)
                copied_count += 1

            print(f"Backup folder created at: {backup_path}")
            print(f"Copied {copied_count} text file(s) into backup.")
            break
        else:
            print("Invalid directory path. Try again.")
