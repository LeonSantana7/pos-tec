import json


def exibir_cabecalho():
    print("=" * 50)
    print("       SISTEMA DE LEITURA DE DADOS JSON")
    print("=" * 50)
    print()


def carregar_json():
    dados_json = '{"nome": "Marcela Luz", "idade": 21}'
    return json.loads(dados_json)


def exibir_resultado(dados):
    print("-" * 50)
    print("  DADOS EXTRAIDOS DO JSON")
    print("-" * 50)
    print(f"  Nome  : {dados['nome']}")
    print(f"  Idade : {dados['idade']} anos")
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()

    dados = carregar_json()
    exibir_resultado(dados)


main()
