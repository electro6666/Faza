import requests as r
import os
import time
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan

user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

def flagcookie(req):  # Main
 jar=req
 try:
    for cookie in jar:
      print('[+] Name:', cookie.name)
      print('[+] Value:', cookie.value)
      if not cookie.secure:
       cookie.secure = '\x1b[31mFalse\x1b[39;49m'
       print('[+] Secure:', cookie.secure)
      if 'httponly' in cookie._rest.keys():
        cookie.httponly = 'True'
      else:
       cookie.httponly='\x1b[31mFalse\x1b[39;49m'
       print('[+] HTTPOnly:', cookie.httponly)
      if cookie.domain_initial_dot:
       cookie.domain_initial_dot =    '\x1b[31mTrue\x1b[39;49m'
       print('[+] Loosly defined domain:', cookie.domain_initial_dot, '\n')
      else:
       print("\n")
 except:
   pass

def flagurl():   # Url checking
  os.system("figlet C flag")
  url=input(f"{B}[+] Enter Url : {W}")
  print(f"\n[~] Url Checking  : {url}")
  flag_url=False
  try:
    responce=r.get(url,headers={"User-Agent":user})
    print(f"[~] Status code : {G}{responce.status_code}{W}")
    print("")  # : )
    flag_url=True
  except Exception as e:
    print(e)
    time.sleep(2)
    print(R)
    print(f"[•] Unable to connect ...")
    pass
  if flag_url ==True:
  	jar(url)

def jar(url):  # cookiejar
  req=r.get(url,headers={"User-Agent":user}).cookies
  if len(req) != 0:
  	flagcookie(req)
  else:
  	print("\n"+25*"-")
  	print(f"{R}[•] Empty Jar{W}")
  	print(25*"-")
  	


  	