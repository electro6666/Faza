import os
import time
from shutil import which

os.system("rm -r faza.jpg")
os.system("rm -r toolimg.jpg")

B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan

print(25*"-")
print(f"{Y}[ !! ] This tool only for Education purpose{W}")
time.sleep(2)
print(f"{R}[ !! ]  Faza terminal configuration started{W}")
time.sleep(3)
print(f"{R}[ ! ] Download rockyou.txt and put in [ files/brute ]{W}")
print(25*"-")
time.sleep(2)
#----
os.system("chmod +x faza")
print("{G}[ + ] permission granted for 'faza'")
time.sleep(2)
print(f"{C}[ + ] Move 'faza' {R}(Not faza.py ){C} to bin for run 'faza terminal' from any directory{W}")
time.sleep(3)
#----
def install(name):
	os.system(f"pkg install {name}")
	time.sleep(1)
	os.system("clear")

fi= which("figlet")
if fi==None:
  install("figlet")

map=which("nmap")
if map==None:
  install("nmap")

cat=which("ncat")
if cat==None:
	install("ncat")
#-----
def pip(name):
	os.system(f"pip install {name}")
	time.sleep(1)
	os.system("clear")	

try:
 import requests
except:
 pip("requests")

try:
 from bs4 import BeautifulSoup
except:
 pip("beautifulsoup4")

try:
  from googlesearch import search
except:
 pip("googlesearch-python")

print(25*"-")
print(f"{G}=======> Completed ")
print(f"{G}[ !! ] type 'faza' for run faza from any directory{W}")
print(25*"-")

#---


 



 

