import socket
import os
import requests as r

def myip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        print(f"PRIVATE IP : {IP}")
    except Exception:
        print('127.0.0.1')
    finally:
        s.close()
    try:
      pu=r.get('https://api.ipify.org').text
      print(f"PUBLIC IP  : {pu}")
    except:
    	pass
    	
def network():
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(('10.255.255.255', 1))
 ip = s.getsockname()[0]
 new=""
 c=0
 for i in ip:
  if i==".":
   c+=1
  new+=i
  if c==3:
   break
 os.system(f"nmap -sP {new}0/24")       