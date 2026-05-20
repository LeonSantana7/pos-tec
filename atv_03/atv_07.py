def exibir_cabecalho():
    print("=" * 50)
    print("       SISTEMA DE CONTROLE DE ACESSO")
    print("=" * 50)
    print()


def obter_idade():
    while True:
        try:
            idade = int(input("  Informe sua idade: "))
            if idade < 0 or idade > 120:
                print("  [AVISO] Idade invalida. Informe um valor entre 0 e 120.")
                print()
            else:
                return idade
        except ValueError:
            print("  [AVISO] Entrada invalida. Digite apenas numeros inteiros.")
            print()


def verificar_acesso(idade):
    if idade >= 18:
        return True
    else:
        return False


def exibir_resultado(idade, acesso_permitido):
    print()
    print("-" * 50)
    print("  RESULTADO DA VERIFICACAO")
    print("-" * 50)
    print(f"  Idade informada : {idade} anos")

    if acesso_permitido:
        print("  Status          : ACESSO PERMITIDO")
        print()
        print("  Voce atende aos requisitos minimos de idade.")
        print("  Bem-vindo a plataforma.")
    else:
        print("  Status          : ACESSO NEGADO")
        print()
        print("  Voce nao atende aos requisitos minimos de idade.")
        print("  O acesso e permitido apenas para maiores de 18 anos.")

    print("-" * 50)
    print()


def main():
    exibir_cabecalho()
    idade = obter_idade()
    acesso_permitido = verificar_acesso(idade)
    exibir_resultado(idade, acesso_permitido)


main()
