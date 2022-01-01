# This is not tools file

Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
B = "\033[34m"    # Blue
C = "\033[36m"    # Cyan

def head():
 print(f'''{C}
    _____
   |  ___|_ _ ______ _      
   | |_ / _` |_  / _` |         
   |  _| (_| |/ / (_| |               v2.0
   |_|  \__,_/___\__,_|
       {B}Faza terminal
   https://github.com/Ag3ntQ{R}
  ----------------------------------------------------
[ # ] Use small letter only for commands
[ # ] Don't use space after command
----------------------------------------------------{W}''')

def scantools(): 
	print(f'''{Y}
  ───[ Enumeration Tools ]───{G}    
[ 1 ] subdo brute   [ find subdomains ]
[ 2 ] dir brute     [ find directory]
[ 3 ] nmap          [ Nmap ]
[ 4 ] nscripts      [ Nmap scripts]
[ 5 ] b grabbing    [ banner grabbing ]
[ 6 ] c flag        [ http cookie flag ]
[ 7 ] network scan  [ Network scan ]
[ 8 ] header        [ server header ]
[ 9 ] gdork         [ google dork ]
''')

def cryptography():
	print(f"{Y}  ───[ Cryptography ]───{G}")
	print("[ 1 ] hash       [ for Encryption ]")
	print("[ 2 ] hash crack [ for Decryption ]")
	print(" ")  # :)

def webaccess():
  print(f"{Y}  ───[ Web access ]───{G}")
  print("[ 1 ] anon ftp  [ check anonymouse login ]")
  print("[ 2 ] ftp brute [ brute force ftp login ]")
  print("[ 3 ] shell     [ reverse connection listener ]")
  print(" ") # :)

def webvuln():
  print(f"{Y}  ───[ Vulnerability scanners ]───{G}")
  print("[ 1 ] sqli    [ Sql injection ]")
  print("[ 2 ] clickjack     [ Clickjacking ]")
  print("[ 3 ] xss form      [ Xss through form submit ]")
  print("[ 4 ] open redirect [ URL redirection vulnerbility ]")
  print("[ 5 ] lfi scan      [ Local File Inclusion ]")
def attacks():  
   print(f"\n{Y}  ───[ Attacks ]───{G}")
   print("[ 1 ] dos       [ Dos attack ]")
   print("[ 2 ] lfi brute [ LFI path brute force]")
   
def te_cmd():  # Faza terminal default commamds
    print(f"\n{Y}  ───[ Terminal commands ]───{G}")
    print("[ 1 ] clear      [ Clear terminal ]")
    print("[ 2 ] restart    [ Restart termnal ]")
    print("[ 3 ] exit       [ Close terminal ]")
    print("[ 4 ] <cmd> --os [ for exicute linux commands]")

def de_cmd(): # some small commamds
  print(f"\n{Y}  ───[ Helpers :) ]───{G}")
  print('[ 1 ] ip("example.com")   [ find IP of domain ]')
  print('[ 2 ] ping("example.com") [ ping command ]')
  print('[ 3 ] my ip        [ find meachine ip ]')
  print('[ 4 ] view code    [ view-source ]')
  print('[ 5 ] sheets       [ Helping notes ]')

def helpfaza():
  head()
  te_cmd()
  scantools()
  cryptography()
  webaccess()
  webvuln()
  attacks()
  de_cmd()



