import hashlib as h
import base64
import os

G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    #Red

def hash():
 os.system("figlet Hash")
 print(30*"=")
 t=input("[+] Type   : ")
 s=input("[+] String : ")
 st=input("[+] Salt   : ")
 print(30*"=")
 if t=="md5":
  v=h.md5((st+s).encode()).hexdigest()
  print(f"[~] MD5 : {v}")
 elif t=="md4":
   v=h.new('md4',(s+st).encode("utf-8")).hexdigest()
   print(f"[~] md4 : {v}")
 elif t=="sha1":
  v=h.sha1((st+s).encode()).hexdigest()
  print(f"[~] SHA1 : {v}")
 elif t=="sha224":
  v=h.sha224((st+s).encode()).hexdigest()
  print(f"[~] SHA224 : {v}")
 elif t=="sha256":
  v=h.sha256((st+s).encode()).hexdigest()
  print(f"[~] Sha256 : {v}")
 elif t=="sha384":
  v=h.sha384((st+s).encode()).hexdigest()
  print(f"[~] Sha384 : {v}")
 elif t=="sha512":
  v=h.sha512((st+s).encode()).hexdigest()
  print(f"[~] Sha512 : {v}")
 elif t=="base64":
  msg_byte=s.encode("ascii")
  base_byte=base64.b64encode(msg_byte)
  base_str=base_byte.decode("ascii")
  print(f"[~] Base64 : {base_str}")
 else:
  print("[ !! ] Invalid Type")
  print('[md4] [md5] [sha1] [sha224] [sha256] [sha384] [sha512] [base64]')

def HashCrack():
 os.system("figlet HashCrack")
 print(30*"=")
 print("[1] Base64")
 print("[2] MD4")
 print("[3] MD5")
 print("[4] SHA1")
 print("[5] SHA224")
 print("[6] SHA256")
 print("[7] SHA384")
 print("[8] SHA512")
 print(30*"=")
 x=int(input("[+] Enter your choice : "))
 s=input("[+] Enter hashed word : ")
 if x==1:
  print(39*"=")
  msg_byte=s.encode("ascii")
  pq=base64.b64decode(msg_byte)
  v=pq.decode("ascii")
  print(f"{G}[~] Cracked : {v}{W}")
 else:
  st=input("[+] Enter salt : ")
  word=input("[+] Enter file name : ")
  print(30*"=")
  def md5():  ### MD5
   files=open(f"files/brute/{word}",encoding="ISO-8859-1")
   for i in files:
    i=i.strip()
    k=h.md5((st+i).encode()).hexdigest()
    if k==s:
     print(f"{G}[~] Cracked : {i}{W}")
     flag=True
     break
    else:
    	pass
  def md4(): ### MD4
   files=open(f"files/brute/{word}",encoding="ISO-8859-1")
   for i in files:
     i=i.strip()
     k=h.new('md4',i.encode("utf-8")).hexdigest()
     if k==s:
      print(f"{G}[~] Cracked : {i}{W}")
      break
   ########
  def sha1():
   files=open(f"files/brute/{word}",encoding="ISO-8859-1")
   for i in files:
    i=i.strip()
    k= h.sha1((st+i).encode()).hexdigest()
    if k==s:
      print(f"{G}[~] Cracked : {i}{W}")
      break
   #############
  def sha224():  ##224
    files=open(f"files/brute/{word}",encoding="ISO-8859-1")
    for i in files:
     i=i.strip()
     k= h.sha224((st+i).encode()).hexdigest()
     if k==s:
       print(f"{G}[~] Cracked : {i}{W}")
       break
  ####
  def sha256():
   files=open(f"files/brute/{word}",encoding="ISO-8859-1")
   for i in files:
    i=i.strip()
    k= h.sha256((st+i).encode()).hexdigest()
    if k==s:
     print(f"{G}[~] Cracked : {i}{W}")
     break
  ####
  def sha384():
    files=open(f"files/brute/{word}",encoding="ISO-8859-1")
    for i in files:
     i=i.strip()
     k= h.sha384((st+i).encode()).hexdigest()
     if k==s:
       print(f"{G}[~] Cracked : {i}{W}")
       break
  ###
  def sha512():
    files=open(f"files/brute/{word}",encoding="ISO-8859-1")
    for i in files:
     i=i.strip()
     k= h.sha512((st+i).encode()).hexdigest()
     if k==s:
       print(f"{G}[~] Cracked : {i}{W}")
       break
  ######
  if x==2:
   md4()
  elif x==3:
   md5()
  elif x==4:
    sha1()
  elif x==5:
  	sha224()
  elif x==6:
  	sha256()
  elif x==7:
   sha384()
  elif x==8:
    sha512()
  else:
   print("="*30)
   print("[ !! ] Wrong Choice")
   print("="*30)