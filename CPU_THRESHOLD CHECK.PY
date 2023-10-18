import psutil

predefined_threshold=float(input("enter the threshold for the cpu usage-"))
while True:
    print(psutil.cpu_percent(interval=1))
    current_cpustat=psutil.cpu_percent(interval=1)
    if float(current_cpustat)>predefined_threshold:
        print("Alert! CPU usage exceeds threshold:"+str(predefined_threshold))
    
        