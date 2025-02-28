import os

file_size = os.path.getsize('praffull.txt')
print(f"Size of 'praffull.txt': {file_size} bytes")

modification_time = os.path.getmtime('praffull.txt')
print(f"Last modification time of 'file.txt': {modification_time}")
