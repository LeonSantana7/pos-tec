nome = input("Digite seu nome: ")
arquivo = open("acesso.txt", "a")
arquivo.write(nome + "\n")
arquivo.close()
