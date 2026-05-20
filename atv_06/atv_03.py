def exibir_cabecalho():
    print("=" * 50)
    print("      SISTEMA DE RECOMENDACAO DE FILMES")
    print("=" * 50)
    print()


def exibir_generos():
    print("  Generos disponiveis:")
    print()
    print("  1. Acao")
    print("  2. Comedia")
    print("  3. Terror")
    print("  4. Romance")
    print("  5. Ficcao Cientifica")
    print()


def obter_genero():
    genero = input("  Digite o genero favorito: ").strip().lower()
    return genero


def recomendar_filme(genero):
    recomendacoes = {
        "acao": {
            "titulo": "Mad Max: Estrada da Furia (2015)",
            "diretor": "George Miller",
            "duracao": "120 min",
            "avaliacao": "8.1/10 no IMDb",
            "sinopse": "Em um mundo pos-apocaliptico, Max se une a Furiosa em uma fuga contra um senhor da guerra tirano.",
        },
        "comedia": {
            "titulo": "Se Beber, Nao Case! (2009)",
            "diretor": "Todd Phillips",
            "duracao": "100 min",
            "avaliacao": "7.7/10 no IMDb",
            "sinopse": "Um grupo de amigos acorda em Las Vegas sem lembrar nada de uma despedida de solteiro que saiu do controle.",
        },
        "terror": {
            "titulo": "O Iluminado (1980)",
            "diretor": "Stanley Kubrick",
            "duracao": "146 min",
            "avaliacao": "8.4/10 no IMDb",
            "sinopse": "Um escritor aceita zelar por um hotel isolado no inverno e começa a perder a sanidade de forma perturbadora.",
        },
        "romance": {
            "titulo": "Diario de uma Paixao (2004)",
            "diretor": "Nick Cassavetes",
            "duracao": "123 min",
            "avaliacao": "7.8/10 no IMDb",
            "sinopse": "Um homem le para uma mulher com Alzheimer a historia de um casal que enfrentou todas as barreiras pelo amor.",
        },
        "ficcao cientifica": {
            "titulo": "Interestelar (2014)",
            "diretor": "Christopher Nolan",
            "duracao": "169 min",
            "avaliacao": "8.7/10 no IMDb",
            "sinopse": "Um grupo de astronautas viaja por um buraco de minhoca em busca de um novo lar para a humanidade.",
        },
    }

    if genero in recomendacoes:
        return recomendacoes[genero], None
    else:
        return (
            None,
            "Genero nao encontrado. Escolha entre: acao, comedia, terror, romance ou ficcao cientifica.",
        )


def exibir_resultado(genero, filme):
    print()
    print("-" * 50)
    print(f"  RECOMENDACAO PARA O GENERO: {genero.upper()}")
    print("-" * 50)
    print(f"  Titulo    : {filme['titulo']}")
    print(f"  Diretor   : {filme['diretor']}")
    print(f"  Duracao   : {filme['duracao']}")
    print(f"  Avaliacao : {filme['avaliacao']}")
    print()
    print("  Sinopse:")
    print(f"  {filme['sinopse']}")
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()
    exibir_generos()

    genero = obter_genero()
    filme, erro = recomendar_filme(genero)

    if erro:
        print()
        print(f"  [AVISO] {erro}")
        print()
    else:
        exibir_resultado(genero, filme)


main()
