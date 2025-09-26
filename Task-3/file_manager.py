# 5) OS File Manager
#    - Ask user for a directory path.
#    - Automatically:
#         - Create a folder "backup" inside it if not exists.
#         - Copy all .txt files into "backup".
#         - Print summary: how many files copied.
#    - If directory invalid, retry until correct.

import os 
import shutil

def file_managing():

    while True:
        try:

            dir_path = input("enter directory path: ").strip()

            os.makedirs(dir_path)

            backup_path = os.path.join(dir_path,"backup")

            os.makedirs(backup_path, exist_ok=True)

            txt_files_path = "E:/ITI_materials/python/Task-3"

            txt_files = [f for f in os.listdir(txt_files_path) if f.endswith(".txt")]

            for file in txt_files:
                src = os.path.join(txt_files_path, file)
                des = os.path.join(backup_path, file)

                shutil.copy2(src,des)
            
            print(f"{len(txt_files)} txt files copied to")

            break
        
        except Exception as e:
            print(f"error : {e}")

# file_managing()
