import signal
from subprocess import Popen
import os
import sys


filename = "main.py "

try:
    flag = sys.argv[1]

except:
    print("Please enter a city flag [option]\nTBLISI: -t\nBATUMI: -b\nKUTAISI: -k\n")
    sys.exit(1)


while True:
    print("\nStarting " + filename)
    p = Popen("python3 " + filename + flag, shell=True, start_new_session=True)
    p.wait()

    os.system("kill -9 $(lsof -i:4715)")
    # os.system("adb -s R58W204XQPM forward --remove-all")

    try:
        os.killpg(os.getpgid(p.pid), signal.SIGTERM)

    except:
        ...
