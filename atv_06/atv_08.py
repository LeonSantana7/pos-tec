def exibir_cabecalho():
    print("=" * 50)
    print("     SISTEMA DE AVALIACAO DE DESEMPENHO")
    print("=" * 50)
    print()


def obter_notas():
    notas = []
    print("  Informe as 3 notas do aluno (de 0 a 10):")
    print()

    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"  Nota {i}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("  [AVISO] A nota deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("  [AVISO] Entrada invalida. Digite apenas numeros.")

    return notas


def calcular_media(notas):
    return sum(notas) / len(notas)


def classificar_desempenho(media):
    if media >= 8.0:
        return (
            "Excelente desempenho",
            "O aluno demonstrou dominio completo do conteudo.",
        )
    elif media >= 6.0:
        return "Bom desempenho", "O aluno atingiu um nivel satisfatorio de aprendizado."
    else:
        return (
            "Desempenho insuficiente",
            "O aluno nao atingiu o nivel minimo necessario.",
        )


def exibir_resultado(notas, media, classificacao, descricao):
    print()
    print("-" * 50)
    print("  RELATORIO DE DESEMPENHO")
    print("-" * 50)
    print(f"  Notas informadas : {', '.join(str(n) for n in notas)}")
    print(f"  Media calculada  : {media:.2f}")
    print(f"  Classificacao    : {classificacao}")
    print()
    print("  Observacao:")
    print(f"  {descricao}")
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()

    notas = obter_notas()
    media = calcular_media(notas)
    classificacao, descricao = classificar_desempenho(media)

    exibir_resultado(notas, media, classificacao, descricao)


main()
