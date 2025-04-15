import os
import shutil
from datetime import datetime, timedelta

source_directory = "/path/to/your/source_directory"

destination_directories = {
    "images": "/path/to/your/destination_directory/images",
    "documents": "/path/to/your/destination_directory/documents",
    "videos": "/path/to/your/destination_directory/videos",
    "archives": "/path/to/your/destination_directory/archives",
    "others": "/path/to/your/destination_directory/others"
}


file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".txt"],
    "videos": [".mp4", ".avi", ".mkv", ".mov"],
    "archives": [".zip", ".rar", ".tar", ".gz"]
}


days_to_keep = 30

for dir in destination_directories.values():
    if not os.path.exists(dir):
        os.makedirs(dir)

def move_file(file_path, dest_dir):
    try:
        shutil.move(file_path, dest_dir)
        print(f"Moved: {file_path} to {dest_dir}")
    except Exception as e:
        print(f"Error moving file {file_path}: {e}")

def organize_files():
    now = datetime.now()
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()
            file_age = now - datetime.fromtimestamp(os.path.getmtime(file_path))


            moved = False
            for file_type, extensions in file_types.items():
                if file_ext in extensions:
                    move_file(file_path, destination_directories[file_type])
                    moved = True
                    break
            if not moved:
                move_file(file_path, destination_directories["others"])


            if file_age > timedelta(days=days_to_keep):
                try:
                    os.remove(file_path)
                    print(f"Deleted old file: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")

if __name__ == "__main__":
    organize_files()