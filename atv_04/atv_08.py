positivos = ["bom", "ótimo"]
negativos = ["ruim", "péssimo"]

palavra = input("Digite uma palavra: ").lower()

if palavra in positivos:
    resultado = f"A palavra '{palavra}' representa um sentimento POSITIVO."
elif palavra in negativos:
    resultado = f"A palavra '{palavra}' representa um sentimento NEGATIVO."
else:
    resultado = f"A palavra '{palavra}' não foi reconhecida."

print(resultado)

with open("sentimentos.txt", "w") as arquivo:
    arquivo.write(resultado + "\n")

print("Resultado salvo em sentimentos.txt!")
