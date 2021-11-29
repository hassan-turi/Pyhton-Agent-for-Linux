import subprocess
import os
import stat
from pathlib import Path


def getIp():
    
    subprocess.call(['uname','-r'])
    interface = "eth0"
    ip = subprocess.check_output("ifconfig " + interface + " | grep 'inet'| cut -d':' -f2", shell = True).strip()
    


def execute__Exploit():
 
    # giving directory name
    dirname = '/home/kali/Downloads'
    
    # giving file extension
    ext = ('.py','.c','.sh')
    
    # iterating over all files
    try:
        for files in os.listdir(dirname):
            if files.endswith(ext):
                # print(files)  # printing file name of desired extension
                if files.endswith('.c'):
                    subprocess.call(["gcc", "code.c"]) # OR gcc for c program
                    tmp = subprocess.call("./a.out")
                    # print("Code.c has output of: ",tmp)
                # elif files.endswith('.sh'):
                #     temp = os.chmod('hello.sh', 0o777)
                #     temp = subprocess.call('./hello.sh')
                    
                    

                    """
                    Different Tries
                    # temp = subprocess.call(['chmod', '0444', 'hello.sh'])  

                    # path = Path("/home/kali/Downloads")
                    # original_st_mode = path.st_mode
                    # path.chmod(original_st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                    
                    # os.popen('chmod +x hello.sh')
                    # temp = subprocess.call('./hello.sh')
                    # print("HEllo.sh file has output of: ",temp) """
            else:
                continue
    except:
        print('exploit was not succesful')


# def check_root():
#     if os.geteuid() != 0: 
#         print("\n")             # If not root user...
#         print("You are not a root user")    # Open root password window

#     if os.geteuid() == 0:   
#         print("\n")           # If you are root user...     
#         print("You are now root!") 

getIp()
execute__Exploit()
# check_root()