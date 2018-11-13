import requests
import ipaddress

##### O proximo bloco solicita ao usuário o IP do servidor e verifica se é um IP válido
IP = 0
while IP == 0:
	IP_servidor = input("Digite o IP do servidor (ex 192.168.0.1): ")
	IP = 1
	try:
		valida_ip = ipaddress.ip_address(IP_servidor)
	except:
		print("IP Inválido")
		IP = 0

##### Solicitamos usuário e senha sem validação
usuario_servidor = input("Digite o usuario do servidor: ")
senha_servidor = input("Digite a senha do servidor: ")

##### O próximo bloco trata a autenticação para obter a chave de autenticação do servidor
##### http:///api/v1/basic/key?username=admin&password=admin
#			|data: data result
#Resposta:	|--- key: verification key
#			|errorcode: error code

def autentica (IP_servidor, usuario_servidor, senha_servidor):
	URL_autenticacao = "http://" + str(IP_servidor) + "/api/v1/basic/key?username=" + str(usuario_servidor) + "&password=" + str(senha_servidor)
	autenticacao = requests.get(url = URL_autenticacao)
	return autenticacao

print(URL_autenticacao)
