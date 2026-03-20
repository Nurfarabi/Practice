import shutil
import os

shutil.move("source.txt", "folder/source.txt")


source_dir = "source_folder"
destination_dir = "destination_folder"

# create file destination
os.makedirs(destination_dir, exist_ok=True)

# move all files
for file in os.listdir(source_dir):
    src_path = os.path.join(source_dir, file)
    dst_path = os.path.join(destination_dir, file)

    if os.path.isfile(src_path):
        shutil.move(src_path, dst_path)
        print(f"Moved: {file}")