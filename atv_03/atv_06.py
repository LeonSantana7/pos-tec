def exibir_cabecalho():
    print("=" * 50)
    print("     SISTEMA DE ANALISE DE OPINIAO EM TEXTO")
    print("=" * 50)
    print()
    print("  Digite palavras uma por vez para analise.")
    print("  Quando terminar, digite 'fim' para encerrar.")
    print()


def obter_palavras_positivas():
    return [
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
        "aprovado",
        "top",
    ]


def processar_palavra(palavra, palavras_positivas):
    palavra = palavra.strip().lower()

    if palavra == "fim":
        return "encerrar", None
    elif palavra == "":
        return "vazio", None
    elif palavra in palavras_positivas:
        return "positivo", palavra
    else:
        return "outro", palavra


def exibir_feedback(status, palavra):
    if status == "positivo":
        print(f"  Classificacao: POSITIVO  |  Palavra: '{palavra}'")
    elif status == "outro":
        print(f"  Classificacao: NEUTRO/NEGATIVO  |  Palavra: '{palavra}'")
    elif status == "vazio":
        print("  [AVISO] Nenhuma palavra digitada. Tente novamente.")
    print()


def exibir_relatorio(
    palavras_digitadas, palavras_positivas_encontradas, total_positivas
):
    print()
    print("=" * 50)
    print("         RELATORIO FINAL DA ANALISE")
    print("=" * 50)
    print(f"  Total de palavras analisadas : {len(palavras_digitadas)}")
    print(f"  Total de palavras positivas  : {total_positivas}")
    print(
        f"  Total de outras palavras     : {len(palavras_digitadas) - total_positivas}"
    )
    print()

    if palavras_positivas_encontradas:
        print("  Palavras positivas identificadas:")
        for p in palavras_positivas_encontradas:
            print(f"    - {p}")
    else:
        print("  Nenhuma palavra positiva foi identificada.")

    print()

    if total_positivas == 0:
        parecer = "Opiniao predominantemente negativa ou neutra."
    elif total_positivas <= len(palavras_digitadas) // 2:
        parecer = "Opiniao mista com poucas palavras positivas."
    else:
        parecer = "Opiniao predominantemente positiva."

    print(f"  Parecer geral: {parecer}")
    print("=" * 50)
    print()


def main():
    exibir_cabecalho()

    palavras_positivas = obter_palavras_positivas()
    palavras_digitadas = []
    palavras_pos_encontradas = []
    total_positivas = 0

    while True:
        entrada = input("  Palavra: ")
        status, palavra = processar_palavra(entrada, palavras_positivas)

        if status == "encerrar":
            break

        exibir_feedback(status, palavra)

        if status in ("positivo", "outro"):
            palavras_digitadas.append(palavra)

        if status == "positivo":
            total_positivas += 1
            palavras_pos_encontradas.append(palavra)

    if palavras_digitadas:
        exibir_relatorio(palavras_digitadas, palavras_pos_encontradas, total_positivas)
    else:
        print()
        print("  Nenhuma palavra foi analisada. Encerrando.")
        print()


main()
