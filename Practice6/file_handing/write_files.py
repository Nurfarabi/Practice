with open(r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open(r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile.txt") as f:
  print(f.read())

with open(r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open(r"C:\Users\user\Desktop\pp2\git-tutorial\githowto\repositories\Practice\Practice6\file_handing\demofile.txt") as f:
  print(f.read())

k = open("myfile.txt", "x")