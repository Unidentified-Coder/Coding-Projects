import os 
from pathlib import Path
import shutil
# Grabs the location of the current file being worked on 
# print(os.getcwd())

os.chdir('/Users/R2/Downloads')
# lists all the currents items located within the path we gave 
# print(os.listdir())

# for file in os.listdir():
#     name, ext = os.path.splitext(file)
#     splitted = name.split("-")
#     splitted = [s.strip() for s in splitted]
#     new_name = f"{splitted[2].zfill(2)}-{splitted[1]}-{splitted[0]}{ext}"
#     print(new_name)
#     os.rename(file, new_name)

# Copy file 
# Path("data").mkdir(exist_ok=True)

# for file in os.listdir():
#     if file == "data":
#         continue
#     shutil.copy2(file, "data")

# Delete Files
# os.remove("data")
# os.rmdir("data")

# Used to remove the specific file regardless of the contents held within
# shutil.rmtree("data")

os.chdir('/Users/R2/Desktop')
def remove_file(file):
    shutil.rmtree(file)

remove_file("WebApplication1")