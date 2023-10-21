
#Importing the library
import psutil

#Threshold value input
predefined_threshold=float(input("Enter the threshold for the CPU usage- "))


#using the exception handling to stop the loop on a keyboard input
try:
    #defining the infinite loop to monitor the usage
    while True:

        # checking the usage using psutil library and cpu_percent function and comparing with the threshold
        if psutil.cpu_percent(1)>predefined_threshold:
            print("Alert! CPU usage exceeds threshold:"+str(predefined_threshold))

#using the keyboard interrupt(ctrl+c) to exit the loop            
except KeyboardInterrupt:
    print('!!CPU usage Monitoring finished!!')

    
        