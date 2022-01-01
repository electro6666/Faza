import os
import sys
import time
from tools.fazahelp import *
from tools.code import *
from tools.nmap import *
from tools.Dos import *
from tools.c_flag import *
from tools.hash import *
from tools.network_socket import *
from tools.header import *
from tools.domain import *
from tools.googledork import *
from tools.ftp import *
from tools.clickjacking import *
from tools.xss import *
from tools.bit_sheet import *
from tools.lfi import *
from tools.sqli import *

BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan


os.system("clear")
print(f'''{C}
    _____
   |  ___|_ _ ______ _ 
   | |_ / _` |_  / _` |   {R} Irfan kpm{C}
   |  _| (_| |/ / (_| |  {R}Vertion : 2.0v{C}
   |_|  \__,_/___\__,_|{W}''')
   
while True:
   print(G)
   inp=input(f"💻[Faza]~(Ag3ntQ) \n└──$ \033[0m")
  
   if "--os" in inp:
       p=len(inp)
       if inp[p-1] == "s":
          q=inp[0:p-4]
          try:
            os.system(q)
          except KeyboardInterrupt:
          	os.system("python faza.py")
       else:
       	print("[+] SpaceError Detected")
       	print(f"[+] Error : <{inp}>")	
   elif inp =="help":
       helpfaza()
   elif inp=="whoami":
   	print(f"{R}Irfankpm")
   elif inp == "my ip":
     try:
      myip()
     except:
     	pass
   elif inp=="sheets":
   	sheets()
   elif inp=="network scan":
    try:
      print(" ")
      network()
    except:
    	error()
   elif inp == "sqli":
     try:
       sqlicheck()
     except KeyboardInterrupt:
     	stop()
     except:
     	pass
   elif inp == "clickjack": 
     try:
       click_jacking()
     except:
      error()
      pass
   elif inp=="xss form":
     try:
       xss_main()
     except Exception as e:
       print(e)
       error()
       pass
   elif inp=="open redirect":
    try:
     redirect()
    except KeyboardInterrupt:
       stop()
    except Exception as e:
    	print(e)
    	error()
    	pass  
   elif inp == "nmap":
    try:
       nmap()
    except KeyboardInterrupt:
    	error()
    except Exception as e:
      print(30*"-")
      print(e)
      error()
      pass
   elif inp == "dir brute":
    try:
     folder()
    except:
     error()
     pass
   elif inp == "hash":
     try:
       hash()
     except:
       error()
       pass
   elif inp == "nscripts":
     try:
       Nscript()
     except:
     	error()
     	pass
   elif inp=="gdork":
     try:
       errordork()
     except Exception as e:
      print(e)
      error()
      pass
   elif inp == "header":
     try:
      serverfingerprint()
     except:
     	error()
     	pass
   elif "()" in inp:
   	print(f"Command <{inp}> not found ")
   elif inp == "dos":
     try:
       Dos()
     except:
       error()
       pass
   elif inp == "c flag":
     try:
      flagurl()
     except:
       error()
       pass
   elif inp == "shell":
     try:
       netcat()
     except:
      error()
      pass
   elif inp == "view code":
     try:
      source()
     except:
       print(f"{R}--- Invalid input --{W}")
   elif inp == "hash crack":
    try:
      HashCrack()
    except KeyboardInterrupt:
      stop()
    except:
      error()
      pass        
   elif inp == "subdo brute":
     try:
        subdomain()
     except KeyboardInterrupt:
       stop()
     except:
       error()
       pass
   elif inp=="lfi scan":
     try:
       lficheck()
     except KeyboardInterrupt:
        stop()
     except:
       pass
   elif inp=="lfi brute":
    try:
     lfibrute()
    except :
      error()
   elif inp=="ftp brute":
     try:
       ftpbrute()
     except KeyboardInterrupt:
      print(30*"=")
      print("[~] KeyboardInterrupt: Terminated")
      print(30*"=") 
     except:
      error()
      pass        
   elif inp=="anon ftp":
   	anonftp()
   elif inp == "b grabbing":
    try:
     BannerGrab()
    except:
      error()
   elif inp == "start":
   	os.system("python faza.py")
   elif inp=="clear":
   	clear()      
   elif inp == "exit":
    os.system("figlet Good bie")
    exit()
   else:
    try:   	 
       if "--os" not in inp:
           y=eval(inp)
           if y: input(y)
    except:
        try:
        	exec(inp)
        except Exception as e:
        	print(f"Command <{inp}> not found ")
        	print("'help' for more information")