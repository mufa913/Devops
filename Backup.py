#Import the libraries
import shutil
import os
from datetime import datetime

#fetch the current datetime.
current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

#convert it to a string
str_current_datetime = str(current_datetime)

#take the directory input
src_dir = input()
dst_dir = input()

#conditions to handle the excption of directory not found

if os.path.isdir(src_dir) and os.path.isdir(dst_dir):

    #Itreating throught the directory files
    for p in os.listdir(src_dir):
       
       #appending the timestamp
       os.listdir(src_dir).append(current_datetime)

       #copying the files from one directory to another
       shutil.copy(os.path.join(src_dir, p),dst_dir)
elif not os.path.isdir(src_dir):
    print("Source directory not found")
else:
    print("Destination directory not found")


    



		
	
		
