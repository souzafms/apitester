#import requests
import ipaddress

##### O proximo bloco solicita ao usuário o IP do servidor e verifica se é um IP válido
##### I
IP = 0
while IP == 0:
	IP_servidor = input("Digite o IP do servidor (ex 192.168.0.1): ")
	IP = 1
	try:
		valida_ip = ipaddress.ip_address(IP_servidor)
	except:
		print("IP Inválido")
		IP = 0
usuario_servidor = input("Digite o usuario do servidor: ")
senha_servidor = input("Digite a senha do servidor: ")


print(IP_servidor, " ", usuario_servidor, " ", senha_servidor)