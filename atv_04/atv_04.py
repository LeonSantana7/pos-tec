arquivo = open("dados.txt", "w")
arquivo.write("Olá, este é um arquivo de texto.\n")
arquivo.close()


arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)

arquivo.close()
