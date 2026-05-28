import sys
import platform

os_name = platform.system()
python_version = sys.version

with open('os_info.txt', 'w') as f:
    f.write(f"OS info is {os_name} Python version is {python_version}")