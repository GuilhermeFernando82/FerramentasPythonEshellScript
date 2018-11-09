import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = raw_input("Digite o site ou ip que deseja scannear: ")
print "1 - Testar um porta especifica:"
print "2 - Teste um range de portas: "

a = input("Informe um opcao: ")

if a==1:
	porta = input("Digite uma porta: ")
	while porta != 0:
    		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    		s.settimeout(1.0)
    		conexao = s.connect_ex((host, porta))
    		if(conexao == 0):
	       		print (porta, " Porta aberta")
			porta = 0
		else:
			print "Porta fechada"
			porta = 0
elif a==2:
	r = input("Informe um range de portas que deseja scannear:")
	for port in range(0,r):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1.0)
                conexao = s.connect_ex((host, port))
                if(conexao == 0):
                	print (port, ": Porta aberta")
                else:
               		print (port, ": Porta fechada")

