import os

def ban():    # Banner 
	print("[1] Command injection ")
	print("[2] Xss payloads")
	print("[3] TTY  :<")
def tty():    # TTY
 print("[~] python -c 'import pty; pty.spawn(\"/bin/sh\")'")
 print("[~] echo os.system('/bin/bash')")
 print("[~] /bin/sh -i")
def shell_sheets():    # cmd shell
  print('''
     _          _ _       _               _
 ___| |__   ___| | |  ___| |__   ___  ___| |_
/ __| '_ \ / _ \ | | / __| '_ \ / _ \/ _ \ __|
\__ \ | | |  __/ | | \__ \ | | |  __/  __/ |_
|___/_| |_|\___|_|_| |___/_| |_|\___|\___|\__|''')
  os.system("cat files/txt/shells.txt")

def xss_sheet():
   os.system("figlet Xss-Scheet")
   os.system("cat files/txt/xsssheet.txt")

def sheets():
  os.system("figlet Sheets")
  print("")
  ban()
  x=int(input("[~] Enter choice : "))
  if x==1:
  	shell_sheets()
  elif x==2:
  	xss_sheet()
  elif x==3:
  	tty()
  else:
  	print(" [•] wrong choice")
