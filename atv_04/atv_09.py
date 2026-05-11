print("Gêneros disponíveis: ação, comédia, terror, romance")
genero = input("Digite seu gênero favorito: ").lower()

if genero == "ação":
    filme = "John Wick"
elif genero == "comédia":
    filme = "Se Beber, Não Case"
elif genero == "terror":
    filme = "O Iluminado"
elif genero == "romance":
    filme = "A Culpa é das Estrelas"
else:
    filme = "Gênero não reconhecido, tente novamente."

recomendacao = f"Gênero: {genero} → Filme recomendado: {filme}"

print(recomendacao)

with open("recomendacoes.txt", "w") as arquivo:
    arquivo.write(recomendacao + "\n")

print("Recomendação salva em recomendacoes.txt!")
