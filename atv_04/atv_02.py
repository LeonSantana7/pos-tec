mensagem = input("Digite uma mensagem: ")
arquivo = open("chatbot.txt", "w")
arquivo.write(mensagem)
arquivo.close()
