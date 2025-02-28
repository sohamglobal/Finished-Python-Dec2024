import os
files_and_dirs = os.listdir()
print("Files and Directories in Current Directory:", files_and_dirs)


path = 'C:\\EthanHunt'
files_and_dirs = os.listdir(path)
print(f"Files and Directories in {path}:", files_and_dirs)
