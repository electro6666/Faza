import os
import socket
import sys
W = "\033[0m"     # White
R = "\033[31m"    # Red
def nmap():
  os.system("figlet Nmap")
  print("[!] work based on Nmap")
  print("")
  print("[0] Exit")
  print("[1] Basic scan")
  print("[2] Single port")
  print("[3] scan with port range")
  print("[4] Port scan the top x ports")
  print("[5] Standard service detection")
  print("[6] Detect Os and services")
  print("[7] Remote OS detection using TCP/IP stack fingerprinting")
  print("[8] Packets trace")
  print("[9] Whois")
  print("[10] A representative scan")  
  def one():
   os.system(f"\n\nnmap {ip} -T5")
   print("")
  def two():
   port=int(input("Enter port number : "))
   os.system(f"\n\nnmap {ip} -sV -A  -p {port}")
   print("")
  def abc():
   ks=int(input("Enter starting port number :"))
   ms=int(input("Enter last port number : "))
   os.system(f"\n\nnmap {ip} -p {ks}-{ms}")
   print("")
  def four():
   os.system(f"\n\nnmap {ip} --top-ports 2000")
   print("")
  def five():
   os.system(f"\n\nnmap {ip} -sV")
   print("")
  def six():
    os.system(f"\n\nnmap {ip} -A")
    print("")
  def seven():
    os.system(f"\n\nnmap {ip} -O")
    print("")
  def trace():
   os.system(f"nmap  {ip} -T4 --packet-trace")
   print("")
  def sca():
  	os.system(f"nmap -T4 -A -v {ip}")
  	print("")	
  def nine():
   os.system(f"nmap --script whois* {ip}")
   print("")
  while True:
   print(25*"-")   
   inp=int(input("[~] Enter your choice :"))
   if inp==0:
   	break
   ip=input("[~] Enter Target IP : ")
   print(25*"-")
   if inp==1:
     one()
   elif inp==2:
      two()
   elif inp==3:
     abc()
   elif inp==4:
     four()
   elif inp==5:
   	five()
   elif inp==6:
   	six()
   elif inp==7:
   	seven()
   elif inp==8:
   	trace()
   elif inp==9:
   	nine()
   elif inp==10:
   	sca()  
   else :
   	print(f"{R}[•] wrong choise{W}")
   	
def ban():
  os.system("figlet Nscripts")
  print("[!] work based on Nmap")
  print("")
  print("[0] Exit")
  print("[1] TPlink-dir-traversal")
  print("[2] Dlink-backdoor.nse")
  print("[3] Sqli cve-2017-8917")
  print("[4] Server info")
  print("[5] Headers")
  print("[6] DOM based XSS")
  print("[7] PHP self XSS")
  print("[8] STORED XSS")
  print("[9] XSSed")
  print("[10] MYSQL info")
  print("[11] SQL-injection")
  print("[12] MySql vuln ")
  print("[13] MySql emtypassword")
  print("[14] vuln script")
  print("[15] Waf finder")
def tpl():
 x=input("[#] Target Website : ")
 os.system(f"nmap -p80 --script http-tplink-dir-traversal.nse {x}")
def dlink():
  x=input("[#] Target Website : ")
  os.system(f"nmap -sV --script http-dlink-backdoor {x}")
def vul():
  x=input("[#] Target Website : ")
  os.system(f"nmap --script=http-vuln-cve2017-8917 -p 80 {x}")
def sinfo():
 x=input("[#] Target Website : ")
 os.system(f"nmap {x} --script=afp-serverinfo.nse --script-trace")
def nmaphead():
  y=input("[#] Target Website : ")
  os.system(f"nmap -p 8009 {y} --script=ajp-headers")
def DOMXSS():
  y=input("[#] Target Website : ")
  os.system(f"nmap -p80 --script=http-dombased-xss.nse {y}")
def PHPXSS():
  y=input("[#] Target Website : ")
  os.system(f"nmap --script=http-phpself-xss -p80 {y}")
def STXSS():
  y=input("[#] Target Website : ")
  os.system(f"nmap -p80 --script=http-stored-xss.nse {y}")
def XSSED():
 y=input("[#] Target Website : ")
 os.system(f"nmap -p80 --script=http-xssed.nse {y}")
def sqlinfo():
  y=input("[#] Target Website : ")
  os.system(f"nmap {y} --script=mysql-info.nse")
def sqli():
 y=input("[#] Target Website : ")
 os.system(f"nmap -p80 --script=http-sql-injection {y}")
def sqlvuln():
 y=input("[#] Target Website : ")
 os.system(f"nmap -p3306 --script=mysql-vuln-cve2012-2122 {y}")
def empty():
 y=input("[#] Target Website : ")
 os.system(f"nmap {y} --script=mysql-empty-password.nse")
def vulnscript():
 y=input("[#] Target Website : ")
 os.system(f"nmap --script vuln {y} -A")
def wafnmap():
  y=input("[#] Target Website : ")
  os.system(f"nmap -p80 --script http-waf-detect {y}")

def Nscript():
  ban()
  while True:
    print("----------------------------------")
    c=int(input("[#] Enter your option : "))
    print("----------------------------------")
    if c==0:
      break
    if c==1:
     tpl()
    elif c==2:
      dlink()
    elif c==3:
      vul()
    elif c==4:
      sinfo()
    elif c==5:
      nmaphead()
    elif c==6:
     DOMXSS()
    elif c==7:
     PHPXSS()
    elif c==8:
    	STXSS()
    elif c==9:
      XSSED()
    elif c==10:
      sqlinfo()
    elif c==11:
      sqli()
    elif c==12:
      sqlvuln()
    elif c==13:
      empty()
    elif c==14:
      vulnscript()
    elif c==15:
    	wafnmap()
    else:
      print("--- Wrong command ---")  