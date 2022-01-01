import requests as r
import os
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
Y = "\033[33m"    # Yellow
      ### ClickJacking 
def click_Poc(url):
  html=f"""<html>
   <head><title>Faza ClickJack</title></head>
   <body>
     <h2>Website is vulnerable to clickjacking!</h2>
     <iframe src="{url}" width="500" height="500"></iframe>
     <h3>It's me Ag3ntQ</h3>
   </body>
</html>"""
  if "https://" in url:
   name=url.replace("https://","")
  elif "http://" in url:
  	name=url.replace("http://","")
  with open("clickjacking"+name+".html","w") as file:
   file.write(html)
   file.close
   print(f"{Y} >>> PoC file clickjacking{name}.html Saved{W}")
   os.system(f"mv clickjacking{name}.html files/PoC")
def click_jacking():
  os.system("figlet ClickJack")
  inp=(input("[~] Enter Domain : "))
  print("")
  k=r.get(inp).headers
  if "X-Frame-Options" not in k:
    print(f"{G}[•] Website is vulnerable{W}")
    click_Poc(inp)
  else:
    print(f"{R}[•] Website is not Vulnerable{W}")          