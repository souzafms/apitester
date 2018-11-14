import requests
import ipaddress
import comandosApi

##### O proximo bloco solicita ao usuário o IP do servidor e verifica se é um IP válido
IP = 0
while IP == 0:
	IP_servidor = "192.168.5.5" #input("Digite o IP do servidor (ex 192.168.0.1): ")
	IP = 1
	try:
		valida_ip = ipaddress.ip_address(IP_servidor)
	except:
		print("IP Inválido")
		IP = 0

##### Solicitamos usuário e senha sem validação
usuario_servidor = "admin" #input("Digite o usuario do servidor: ")
senha_servidor = "mdvr%66" #input("Digite a senha do servidor: ")

chamaComandosApi = comandosApi.ComandosApi()

chaveServidor = chamaComandosApi.autentica(IP_servidor, usuario_servidor, senha_servidor)