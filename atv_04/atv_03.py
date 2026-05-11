nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")

arquivo = open("notas.txt", "w")
arquivo.write(nota1 + "\n")
arquivo.write(nota2 + "\n")
arquivo.close()
