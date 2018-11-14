# Esse arquivo contém todos os testes a serem executados na aplicação com o objetivo de 
# desenvolver baseado em TDD.

import unittest
import comandosApi

IP_servidor = "192.168.5.5" #Fixa IP para execução dos testes
usuario_servidor = "admin" #Fixa usuário para execução dos testes
senha_servidor = "mdvr%66" #Fixa senha para execução dos testes

class testeAPI(unittest.Testcase):

	def autenticacaoIpIncorreto(self):
		chaveServidor = chamaComandosApi.autentica(IP_servidor, usuario_servidor, senha_servidor)

		self.assertFalse


if __name__ == '__main__':
    unittest.main()