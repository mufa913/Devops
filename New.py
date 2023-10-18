import psutil

predefined_threshold=float(input("enter the threshold for the cpu usage-"))
while True:
    print(psutil.cpu_percent())
    if float(psutil.cpu_percent())>predefined_threshold:
        print("Alert!! The CPU has reached its threshold")
        