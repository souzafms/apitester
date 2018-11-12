# apitester

Aplicação para realizar uma série de testes em dispositivos por compandos API.

Documentações úteis sobre HTTP GET POST request usando Python:
- https://www.geeksforgeeks.org/get-post-requests-using-python/
- 
- 

Como instalar a biblioteca 'requests' usando pip

1. Navegar para C:\Users\ -usuário- \AppData\Local\Programs\Python\Python36-32\Scripts
2. Rodar o comando: pip.exe install requests

Estrutura da aplicação

1. Obter do usuário:
	a. IP do servidor
	b. usuário do servidor
	c: senha do servidor
2. Com as informações acima, autenticar a aplicação no servidor e obter a chave da API
	a. retornar ao usuário "CONECTADO" caso tenha sucesso
	b. "FALHA NA CONEXÃO" caso não tenha tido sucesso e solicitar os dados novamente
3. Caso CONECTADO, listar as possíveis requisições