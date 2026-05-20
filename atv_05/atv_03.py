import json


def exibir_cabecalho():
    print("=" * 50)
    print("    SIMULADOR DE RESPOSTA DE IA EM JSON")
    print("=" * 50)
    print()


def criar_resposta_ia():
    resposta_ia = {
        "id": "resp_001",
        "modelo": "claude-sonnet-4",
        "pergunta": "O que e Inteligencia Artificial?",
        "resposta": "Inteligencia Artificial e um campo da computacao que desenvolve sistemas capazes de realizar tarefas que normalmente exigiriam inteligencia humana, como aprendizado, raciocinio e tomada de decisoes.",
        "tokens_usados": 42,
        "status": "sucesso",
    }
    return resposta_ia


def converter_para_json(dicionario):
    return json.dumps(dicionario, indent=4, ensure_ascii=False)


def exibir_dicionario(dados):
    print("-" * 50)
    print("  DICIONARIO PYTHON (antes da conversao)")
    print("-" * 50)
    print()
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")
    print()


def exibir_json(dados_json):
    print("-" * 50)
    print("  FORMATO JSON (apos a conversao)")
    print("-" * 50)
    print()
    print(dados_json)
    print()


def main():
    exibir_cabecalho()

    dicionario = criar_resposta_ia()
    dados_json = converter_para_json(dicionario)

    exibir_dicionario(dicionario)
    exibir_json(dados_json)

    print("-" * 50)
    print("  Conversao realizada com sucesso.")
    print("  Tipo original : dict")
    print(f"  Tipo final    : {type(dados_json).__name__}")
    print("-" * 50)
    print()


main()
