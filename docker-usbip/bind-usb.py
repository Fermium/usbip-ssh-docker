#!/usr/bin/python3
import subprocess
from subprocess import Popen, PIPE, STDOUT, DEVNULL
import re
import sys
import time
import os


# List all local bindable usb ports
result = subprocess.run(['usbip', 'list', '--parsable' , '--local'], stdout=subprocess.PIPE)

# Parse result
regex1 = r"(busid=[\d\-\.]+)"
matches = re.findall(regex1, str(result.stdout))
for i, match in enumerate(matches):
    match = match.replace("busid=","")
    matches[i] = match
    
    
uname = os.uname().release

subprocess.run(['/usr/lib/linux-tools/' + uname + "/" + 'usbipd', '-D'])

try:
    while True:
        for port in matches:
            result = subprocess.call(['/usr/lib/linux-tools/' + uname + '/' + 'usbip', 'bind', '-b' , port], stdout=DEVNULL, stderr=DEVNULL)
            del result
            time.sleep(5)
except KeyboardInterrupt:
    print("Exiting. usbip daemon could still be running")

sys.exit(0)
