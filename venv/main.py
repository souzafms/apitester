import requests
import ipaddress
import comandosApi

##### O proximo bloco solicita ao usuário o IP do servidor e verifica se é um IP válido
##### utilizando a biblioteca ipaddress

IP = 0
while IP == 0:
	IP_servidor = input("Digite o IP do servidor (ex 192.168.0.1): ")
	IP = 1
	try:
		valida_ip = ipaddress.ip_address(IP_servidor)
	except:
		print("IP Inválido, digite novamente.")
		IP = 0

##### Solicitamos usuário e senha sem validação
usuario_servidor = input("Digite o usuario do servidor: ")
senha_servidor = input("Digite a senha do servidor: ")

##### Chamada da classe de comandos API
chamaComandosApi = comandosApi.ComandosApi()

##### Chamada da função de autenticação passando os parâmetros colhidos do usuário
chaveServidor = chamaComandosApi.autentica(IP_servidor, usuario_servidor, senha_servidor)
print(chaveServidor)