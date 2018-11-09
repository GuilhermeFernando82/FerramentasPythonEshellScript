import subprocess

print"|  _ \ _ __ ___   __ _ _ __ __ _ _ __ ___    / \   _ __   __| | | | | __ _ "
print"| |_) | '__/ _ \ / _` | '__/ _` | '_ ` _ \  / _ \ | '_ \ / _` | |_| |/ _` |"
print"|  __/| | | (_) | (_| | | | (_| | | | | | |/ ___ \| | | | (_| |  _  | (_| |"
print"|_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_/_/   \_\_| |_|\__,_|_| |_|\__,_|"
print"                 |___/                         "                            
print"      _    _            _____           _     "
print"  ___| | _(_)_ __   __ |_   _|__   ___ | |___ "
print" / __| |/ / | '_ \ / _` || |/ _ \ / _ \| / __|"
print "| (__|   <| | | | | (_| || | (_) | (_) | \__ \""
print " \___|_|\_\_|_| |_|\__, ||_|\___/ \___/|_|___/"
print "                   |___/ "


print " 1- Whois "
print " 2- Backdoor"
print " 3- Snnifer"
print " 4- Snnifer de senhas"
print " 5- Servidor para Shell reversa"
print " 6- Scanner de portas"
print " 7- Pegar subdominios de um site"

opcao = input("Entre com uma ferramenta: ")
if opcao==1:
	return_code = subprocess.call("./whois.sh", shell=True)
elif opcao==2:
	return_code = subprocess.call("nano backdoor.py", shell=True)
elif opcao==3:
	return_code = subprocess.call("python snnifer.py", shell=True)
elif opcao==4:
	return_code = subprocess.call("python snnife1.py", shell=True)
elif opcao==5:
	return_code = subprocess.call("./serve.sh", shell=True)
elif opcao==6:
	return_code = subprocess.call("python scanner.py", shell=True)
elif opcao==7:
	turn_code = subprocess.call("./pegarsub.sh", shell=True)
