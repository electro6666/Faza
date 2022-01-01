import os,sys
import socket
import requests as r
W = "\033[0m"     # White
R = "\033[31m"    # Red

# Ip address of a domain
def ip(site):
	try:
		i=socket.gethostbyname(site)
		print("IP address : "+i)
	except socket.gaierror:
		print("[~] Unable to Connect...")
# Clear terminal
def clear():
	os.system("clear")
# Banner grab
def BannerGrab():
  os.system("figlet B-Grabing")
  ip=input("[#] Enter IP : ")
  port=int(input("[#] Enter port number : "))
  s=socket.socket(socket.AF_INET,    socket.SOCK_STREAM)
  s.settimeout(20)
  abc = s.connect_ex((ip,port))
  if abc == 0:
    s.connect((ip,port))	
    byte = str.encode("request:\r\n")
    s.send(byte)
    ban = s.recv(1024)
    print("----Result-----")
    print(ban)
  else:
   print("Port is closed")
   print("Banner Grabing not possible now")
# view-source    
def source():
 y=input("[#] Enter url : ")
 print(r.get(y).text)
def netcat():
  os.system("figlet shell")
  print("[ !! ] Work based on Ncat")
  print("")
  p=input("[+] Enter listening port : ")
  os.system(f"nc -lvnp {p}")
# Except error msg
def error():
  print(25*"-")
  print(f"{R} Error found;Passed{W}")
  print(25*"-")
# Terminate
def stop():
 print(30*"=")
 print("[~] KeyboardInterrupt: Terminated")
 print(30*"=")

def ping(url):  # ping
  os.system(f"ping -c 3 {url}")
 
def whois(url):  # whois
  os.system(f"whois {url}")