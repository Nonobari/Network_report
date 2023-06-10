import os
import sys


if len(sys.argv)<=1:
    print("Error : Arg missing, ip required")
else: 
    ip = sys.argv[1]
    for size in range(0,80000,8):
        os.system(f"ping -s {size} -c 1 {ip}")