import sys
import os

if sys.platform.startswith('win32'):
    os.system("cd src")
    os.system("go build -o hascal.exe")
elif sys.platform.startswith('linux'):
    os.system("cd src")
    os.system("go build -o hascal")
