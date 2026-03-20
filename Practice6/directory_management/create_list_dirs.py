import os

# создаем папки
os.makedirs("test_folder/subfolder1", exist_ok=True)
os.makedirs("test_folder/subfolder2", exist_ok=True)

# выводим список папок внутри test_folder
for item in os.listdir("test_folder"):
    path = os.path.join("test_folder", item)
    if os.path.isdir(path):
        print("Directory:", item)

