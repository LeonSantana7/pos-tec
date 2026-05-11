nome = input("Digite seu nome: ")

arquivo = open("usuario.txt", "w")
arquivo.write(nome)
arquivo.close()
