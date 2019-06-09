user = input("Nome de usuario: ")
senha = input("Senha: ")

while senha == user:
	senha = input("Digite uma senha diferente do nome de usuário: ")

print ("Usuário: %s, Senha: %s" %(user, senha))
