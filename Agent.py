import subprocess
import os
import re
import sys
from pathlib import Path

# class Agent():
  
Linux_kernel = ['4.19.13', '4.19.0', '4.19.28', '5.4.0', '5.5.0', '5.7.0', '5.9.0']


p = subprocess.Popen(['uname', '-r'], stdout=subprocess.PIPE).communicate()[0]
kernel_name = p.decode('utf-8')
print(type(kernel_name))
# kernel_name1 , err = p.communicate()

kernel_name1 = kernel_name.join(re.findall(r"[0-9]+\.[0-9]+\.[0-9]+",kernel_name))

if kernel_name1 == "5.9.0":
    print("hello")
    args = ["./PwnKit"]
    child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    child_process_output = child_proccess.communicate(b"id > output.txt")[0]
    print(child_process_output)

elif kernel_name1 == "4.19.0":
    args = ["./pwn"]
    child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    child_process_output = child_proccess.communicate(b"id > output.txt")[0]
    print(child_process_output)

    # def linux(self):
    #     print('there')
    #     if '5.9.0'.__contains__(self.kernel_name):
    #         print("hello")
    #         args = ["./PwnKit"]
    #         child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    #         child_process_output = child_proccess.communicate(b"id > output.txt")[0]
    #         print(child_process_output)
    # if kernel_name == '4.19.0':
    #     args = ["./pwn"]
    #     child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    #     child_process_output = child_proccess.communicate(b"id > output.txt")[0]
    #     print(child_process_output)
    
# obj = Agent()
# obj.check()
# obj.linux()