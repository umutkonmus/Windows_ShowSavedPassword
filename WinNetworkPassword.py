import subprocess
import time
 
TargetNetwork = str(subprocess.check_output(["netsh","wlan","show","profiles"]),"cp437").split("\n")
 
def FindNetwork():
    for i in TargetNetwork:
        if "All User Profile" in i:
            i = i.split(":")
            yield i[-1].strip()
 
Networks = list(FindNetwork())
print(Networks)
 
SelectNetwork = input("Please type target network name :").strip()
if SelectNetwork in Networks:
    TargetInfo = str(subprocess.check_output(["netsh","wlan","show","profiles",SelectNetwork,"key=clear"]),"cp437").split("\n")
    for p in TargetInfo:
        if "Key Content" in p:
            p = p.strip().split(":")
            print("\nPassword :",p[-1].strip())
            break
else:
    print("Couldn't find the network!")
    time.sleep(3)