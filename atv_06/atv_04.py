import json
from datetime import datetime


def exibir_cabecalho():
    print("=" * 50)
    print("     SIMULADOR DE COMUNICACAO COM API DE IA")
    print("=" * 50)
    print()


def obter_pergunta():
    pergunta = input("  Digite sua pergunta para a IA: ").strip()
    return pergunta


def simular_envio(pergunta):
    requisicao = {
        "requisicao": {
            "modelo": "claude-sonnet-4",
            "temperatura": 0.7,
            "max_tokens": 1000,
            "mensagem": pergunta,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    }
    return requisicao


def simular_resposta(pergunta):
    pergunta_lower = pergunta.lower()

    if "capital" in pergunta_lower and "brasil" in pergunta_lower:
        resposta = (
            "A capital do Brasil e Brasilia, localizada no Distrito Federal desde 1960."
        )
    elif "inteligencia artificial" in pergunta_lower or "ia" in pergunta_lower:
        resposta = "Inteligencia Artificial e a area da computacao que desenvolve sistemas capazes de simular o raciocinio humano."
    elif "python" in pergunta_lower:
        resposta = "Python e uma linguagem de programacao de alto nivel, amplamente utilizada em IA, ciencia de dados e automacao."
    else:
        resposta = (
            "Sua pergunta foi recebida e processada com sucesso pelo modelo de IA."
        )

    retorno = {
        "resposta": {
            "status": "sucesso",
            "codigo": 200,
            "modelo": "claude-sonnet-4",
            "pergunta": pergunta,
            "resposta": resposta,
            "tokens_usados": len(pergunta.split()) + len(resposta.split()),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    }
    return retorno


def exibir_json(titulo, dados):
    dados_json = json.dumps(dados, indent=4, ensure_ascii=False)
    print()
    print("-" * 50)
    print(f"  {titulo}")
    print("-" * 50)
    print()
    print(dados_json)
    print()


def main():
    exibir_cabecalho()

    pergunta = obter_pergunta()

    if not pergunta:
        print()
        print("  [AVISO] Nenhuma pergunta digitada. Encerrando.")
        print()
        return

    requisicao = simular_envio(pergunta)
    resposta = simular_resposta(pergunta)

    exibir_json("JSON DE ENVIO PARA A API", requisicao)
    exibir_json("JSON DE RESPOSTA DA API", resposta)

    print("-" * 50)
    print("  Comunicacao simulada com sucesso.")
    print("-" * 50)
    print()


main()
