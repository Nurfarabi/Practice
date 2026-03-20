import os
os.remove(r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile.txt")

if os.path.exists(r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile.txt"):
  os.remove(r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile.txt")
else:
  print("The file does not exist")

os.rmdir("myfolder") #only empty folder

import shutil

shutil.copy(
    r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile.txt"
    r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile2.txt"
)

shutil.copy2(
    r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile.txt"
    r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile2.txt"
)