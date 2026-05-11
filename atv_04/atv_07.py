tarefa1 = input("Digite a primeira tarefa: ")
tarefa2 = input("Digite a segunda tarefa: ")
tarefa3 = input("Digite a terceira tarefa: ")

tarefas = open("tarefas.txt", "w")
tarefas.write(str(tarefa1) + "\n")
tarefas.write(str(tarefa2) + "\n")
tarefas.write(str(tarefa3) + "\n")
tarefas.close()
