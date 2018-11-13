class comandosApi()

##### O próximo bloco trata a autenticação para obter a chave de autenticação do servidor
##### http:///api/v1/basic/key?username=admin&password=admin
#			|data: data result
#Resposta:	|--- key: verification key
#			|errorcode: error code

def autentica (IP_servidor, usuario_servidor, senha_servidor):
	URL_autenticacao = "http://" + str(IP_servidor) + ":12056/api/v1/basic/key?username=" + str(usuario_servidor) + "&password=" + str(senha_servidor)
	autenticacao = requests.get(url = URL_autenticacao)
	data = autenticacao.json()
	chave = data['data']['key']
	return chave