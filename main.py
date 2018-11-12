#import requests
import socket

IP = 0
while IP == 0:
	IP_servidor = input("Digite o IP do servidor: ")
	try:
		socket.inet_aton(IP_servidor)
	except socket.error:
		print("IP Inválido")
		
usuario_servidor = input("Digite o usuario do servidor: ")
senha_servidor = input("Digite a senha do servidor: ")


print(IP_servidor, " ", usuario_servidor, " ", senha_servidor)