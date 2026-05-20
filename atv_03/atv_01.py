def exibir_cabecalho():
    print("=" * 50)
    print("     SISTEMA DE RECOMENDACAO DE FILMES")
    print("=" * 50)
    print()


def obter_genero():
    genero = input("Informe o genero desejado (acao, comedia, terror): ")
    return genero.strip().lower()


def recomendar_filme(genero):
    recomendacoes = {
        "acao": {
            "titulo": "Mad Max: Estrada da Furia (2015)",
            "diretor": "George Miller",
            "duracao": "120 min",
            "nota": "8.1/10 no IMDb",
            "sinopse": "Em um mundo pos-apocaliptico, Max Rockatansky se une a Furiosa em uma fuga desesperada contra um senhor da guerra tirano. Um filme de acao visceral com fotografia premiada e ritmo frenético.",
        },
        "comedia": {
            "titulo": "Se Beber, Nao Case! (2009)",
            "diretor": "Todd Phillips",
            "duracao": "100 min",
            "nota": "7.7/10 no IMDb",
            "sinopse": "Tres amigos acordam em Las Vegas apos uma despedida de solteiro sem lembrarem de nada, inclusive do noivo. Uma comedia de situacao com roteiro bem construido e atuacoes marcantes.",
        },
        "terror": {
            "titulo": "O Iluminado (1980)",
            "diretor": "Stanley Kubrick",
            "duracao": "146 min",
            "nota": "8.4/10 no IMDb",
            "sinopse": "Um escritor aceita o trabalho de zelador em um hotel isolado durante o inverno. Com o tempo, forcas sobrenaturais comecam a abalar sua sanidade. Um classico absoluto do terror psicologico.",
        },
    }

    if genero in recomendacoes:
        filme = recomendacoes[genero]
        print()
        print("-" * 50)
        print("  RECOMENDACAO PARA O GENERO:", genero.upper())
        print("-" * 50)
        print(f"  Titulo   : {filme['titulo']}")
        print(f"  Diretor  : {filme['diretor']}")
        print(f"  Duracao  : {filme['duracao']}")
        print(f"  Avaliacao: {filme['nota']}")
        print()
        print("  Sinopse:")
        print(f"  {filme['sinopse']}")
        print("-" * 50)
    else:
        print()
        print("[AVISO] Genero nao encontrado.")
        print("Opcoes validas: acao, comedia, terror.")


def main():
    exibir_cabecalho()
    genero = obter_genero()
    recomendar_filme(genero)
    print()


main()
