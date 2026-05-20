def exibir_cabecalho():
    print("=" * 50)
    print("     SISTEMA DE AVALIACAO DE DESEMPENHO")
    print("=" * 50)
    print()


def obter_notas():
    notas = []
    print("  Informe as 5 notas do aluno (de 0 a 10):")
    print()

    for i in range(1, 6):
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


def classificar_aluno(media):
    if media >= 7.0:
        situacao = "APROVADO"
        descricao = "O aluno atingiu a media minima exigida."
    elif media >= 5.0:
        situacao = "RECUPERACAO"
        descricao = "O aluno esta abaixo da media e deve realizar recuperacao."
    else:
        situacao = "REPROVADO"
        descricao = "O aluno nao atingiu o desempenho minimo necessario."

    return situacao, descricao


def exibir_resultado(notas, media, situacao, descricao):
    print()
    print("-" * 50)
    print("  RELATORIO DE DESEMPENHO")
    print("-" * 50)
    print(f"  Notas registradas : {', '.join(str(n) for n in notas)}")
    print(f"  Media calculada   : {media:.2f}")
    print(f"  Situacao          : {situacao}")
    print()
    print("  Observacao:")
    print(f"  {descricao}")
    print("-" * 50)


def main():
    exibir_cabecalho()
    notas = obter_notas()
    media = calcular_media(notas)
    situacao, descricao = classificar_aluno(media)
    exibir_resultado(notas, media, situacao, descricao)
    print()


main()
