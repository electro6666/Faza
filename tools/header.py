import requests
import os
user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
head={"User-Agent":user}
def met(url):
 print(25*"-")
 k = ['GET', 'POST', 'PUT','OPTIONS', 'DELETE', 'TRACE',  'TEST']
 for i in k:
  req = requests.request(i,url,headers=head)
  print(f"[~] {i}       {req.status_code} ")

def serverfingerprint():
 user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
 head={"User-Agent":user}
 os.system("figlet Header ")
 inp=input("[#] Enter Url : ")
 print("")
 tar=""
 if "https://" in inp:
   k=inp.replace("https://","")
   tar+="http://"+k  
 elif "http" not in inp:
 	tar+="http://"+inp	
 else:
     tar+=inp
 req = requests.get(tar,headers=head)
 headers = ['Host','Server','Date','Via','Content-Length','X-Powered-By','Content-Type','X-Country-Code','X-Frame-Options','X-XSS-Protection','Connection','ETag',"allow","Accept-Ranges","pragma"]
 for head in headers:
   try:
     result = req.headers[head]
     print(f'{head} : {result}')
   except:
    pass
 met(inp)