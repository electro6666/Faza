from googlesearch import search
import requests as r
import time
import os
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
B = "\033[34m"    # Blue
def dork():
  os.system("figlet G Dork")
  print("")
  url=input(f"{B}[~] Enter Target : {W}")
  print("")
  def sub_dork(query):
    flag=False
    for j in search(query):
      print(f"{G} [•] {j}{W}")
      flag=True
    if flag==False:
      print(f"{R}[•] Not found anything{W}")
    time.sleep(10)
  print(f"{Y}  >>> Login page{W}")  ###
  query="inurl:login site:" +url
  sub_dork(query)	
  print(f"{Y}  >>> Login/Signup{W}") ###
  query="site:"+url+" inurl:signup | inurl:register | intitle:Signup"
  sub_dork(query)
  print(f"{Y}  >>> php{W}") ###
  query="site:"+url+" inurl:php"
  sub_dork(query)
  print(f"{Y} >>> html-doc-pdf {W}")  ####
  query="site:"+url+" ext:html | ext:doc | ext:pdf"
  sub_dork(query)
  print(f"{Y}  >>> Wordpress Entries{W}")
  query="site:" + url + " inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download"
  sub_dork(query)
  print(f"{Y}  >>> = parameter {W}") ###
  query="site:"+url+" inurl:id= | inurl:page= | inurl:news= | inurl:article= | inurl:file="
  sub_dork(query)

def errordork():
  try:
    dork()
  except:
  	print(25*"-")
  	print("[•] ERROR found;Passed")
  	print(25*"-")
  	pass
	 