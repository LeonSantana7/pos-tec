def exibir_cabecalho():
    print("=" * 50)
    print("      SISTEMA DE ANALISE DE SENTIMENTOS")
    print("=" * 50)
    print()


def obter_palavra():
    palavra = input("  Digite uma palavra para analise: ").strip().lower()
    return palavra


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
        "adorei",
        "amei",
        "recomendo",
        "feliz",
        "top",
        "aprovado",
        "contente",
        "alegre",
        "positivo",
        "grato",
        "obrigado",
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
        "detestei",
        "odiei",
        "decepcionante",
        "triste",
        "negativo",
        "raiva",
        "frustrado",
        "irritado",
        "chateado",
        "horroso",
    ]

    if palavra == "":
        return "INDEFINIDO", "Nenhuma palavra foi informada para analise."
    elif palavra in palavras_positivas:
        return "POSITIVO", "A palavra transmite uma mensagem favoravel ou de aprovacao."
    elif palavra in palavras_negativas:
        return (
            "NEGATIVO",
            "A palavra transmite uma mensagem desfavoravel ou de reprovacao.",
        )
    else:
        return (
            "NEUTRO",
            "A palavra nao foi identificada como claramente positiva ou negativa.",
        )


def exibir_resultado(palavra, classificacao, descricao):
    print()
    print("-" * 50)
    print("  RESULTADO DA ANALISE")
    print("-" * 50)
    print(f"  Palavra       : {palavra}")
    print(f"  Classificacao : {classificacao}")
    print()
    print("  Interpretacao:")
    print(f"  {descricao}")
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()
    palavra = obter_palavra()
    classificacao, descricao = classificar_sentimento(palavra)
    exibir_resultado(palavra, classificacao, descricao)


main()
