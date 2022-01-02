import requests
import socket as s
import os,time
B = "\033[34m"    # BlueB 
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
head={"User-Agent":user}
def subdomain():
  print(Y)
  os.system("figlet SubdoBrute")
  print(f"{Y}[ ! ] Diamin without http or https")
  target=input(f"\n{B}[#] Enter Domain : {W}")
  print(25*"=")
  files=open(f"files/brute/subdomains.txt")
  flag=False
  for line in files:
    line=line.strip()
    url=line+"."+target
    try:
     get_url="https://"+url
     res= requests.get(get_url,headers=head,timeout=5)
     if res:
      flag=True
      iip=s.gethostbyname(url)
      print(f"{G}[•] {url} [{iip}]{W}")
    except KeyboardInterrupt:
    	print("[ !! ] KeyboardInterrupt : Terminated")
    	break
    except:
    	pass
  if flag==False:
   print(f"{R}[-] Subdomain Not Found{W}")
  else:
   pass
   
  
def folder():
 print(Y)
 os.system("figlet Dir brute")
 inp=input(f"{B}[#] Enter Domain : {W}")
 file_name=input(f"{B}[#] Enter file name : {W}")
 print(25*"=")
 files=open(f"files/brute/{file_name}")
 for line in files:
   line=line.strip()
   url=inp+"/"+line
   try:
    res=requests.get(url,headers=head)
    if res:
     print(f"[ • ] {line} [{res.status_code}]{W}")
    else:
       pass
   except KeyboardInterrupt:
   	break
   	print("[ !! ] KeyboardInterrupt : Terminated")
   except:
   	pass

def open_redirect(url):
 file_name="redirect.txt"
 out_flag=False
 print(" ")
 files=open(f"files/brute/{file_name}")
 for line in files:
   line=line.strip()
   url_get=url+line
   try:
    res=requests.get(url_get,headers=head)
    if res:
     out_flag=True
     print(f"[ • ] {line} [{res.status_code}]{W}")
    else:
       pass
   except KeyboardInterrupt:
   	break
   	print("[ !! ] KeyboardInterrupt : Terminated")
   except:
   	pass
   if out_flag ==False:
    print(f"{R}[•] Not found{W}")	   	
def redirect():
  print(Y)
  os.system("figlet OpenRedirect")
  url=input(f"{B}[+] Enter Url : {W}")
  print(f"\n[~] Url Checking  : {url}")
  flag_url=False
  try:
    responce=requests.get(url,headers={"User-Agent":user})
    print(f"[~] Status code : {G}{responce.status_code}{W}")
    if responce:
     flag_url=True
  except Exception as e:
    time.sleep(2)
    print(R)
    print(f"[•] Unable to connect ...")
    pass
  if flag_url ==True:
  	open_redirect(url)  
  
 		