def exibir_cabecalho():
    print("=" * 50)
    print("     SISTEMA DE ANALISE DE SENTIMENTOS")
    print("=" * 50)
    print()


def obter_palavra():
    palavra = input("Digite uma palavra para analise: ")
    return palavra.strip().lower()


def classificar_sentimento(palavra):
    palavras_positivas = [
        "bom",
        "otimo",
        "excelente",
        "incrivel",
        "maravilhoso",
        "fantastico",
        "perfeito",
        "agradavel",
        "satisfatorio",
        "legal",
    ]

    palavras_negativas = [
        "ruim",
        "pessimo",
        "terrivel",
        "horrivel",
        "odioso",
        "deploravel",
        "lamentavel",
        "insatisfatorio",
        "fraco",
        "horrendo",
    ]

    if palavra in palavras_positivas:
        classificacao = "POSITIVO"
        descricao = "A palavra transmite uma mensagem favoravel ou de aprovacao."
    elif palavra in palavras_negativas:
        classificacao = "NEGATIVO"
        descricao = "A palavra transmite uma mensagem desfavoravel ou de reprovacao."
    else:
        classificacao = "NEUTRO"
        descricao = (
            "A palavra nao foi identificada como claramente positiva ou negativa."
        )

    return classificacao, descricao


def exibir_resultado(palavra, classificacao, descricao):
    print()
    print("-" * 50)
    print("  RESULTADO DA ANALISE")
    print("-" * 50)
    print(f"  Palavra      : {palavra}")
    print(f"  Classificacao: {classificacao}")
    print()
    print("  Interpretacao:")
    print(f"  {descricao}")
    print("-" * 50)


def main():
    exibir_cabecalho()
    palavra = obter_palavra()
    classificacao, descricao = classificar_sentimento(palavra)
    exibir_resultado(palavra, classificacao, descricao)
    print()


main()
