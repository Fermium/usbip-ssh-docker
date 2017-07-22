#!/usr/bin/python3
import subprocess
import re

# List all local bindable usb ports
result = subprocess.run(['usbip', 'list', '--parsable' , '--local'], stdout=subprocess.PIPE)

# Parse result
regex1 = r"(busid=[\d\-\.]+)"
matches = re.findall(regex1, str(result.stdout))
for i, match in enumerate(matches):
    match = match.replace("busid=","")
    matches[i] = match
    
    
import os
uname = os.uname().release

subprocess.run(['/usr/lib/linux-tools/' + uname + "/" + 'usbipd', '-D'])

import time

while 1:
    for port in matches:
        result = subprocess.run(['/usr/lib/linux-tools/' + uname + '/' + 'usbip', 'bind', '-b' , port])
        del result
    time.sleep(5)
    
