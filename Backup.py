import shutil
import os
from datetime import datetime

current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
str_current_datetime = str(current_datetime)
src_dir = input()
dst_dir = input()

if os.path.isdir(src_dir) and os.path.isdir(dst_dir):
    for p in os.listdir(src_dir):
       os.listdir(src_dir).append(current_datetime)
       shutil.copy(os.path.join(src_dir, p),dst_dir)
elif not os.path.isdir(src_dir):
    print("Source directory not found")
else:
    print("Destination directory not found")


    



		
	
		
