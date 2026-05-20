import json


def exibir_cabecalho():
    print("=" * 50)
    print("        CHATBOT COM RESPOSTA EM JSON")
    print("=" * 50)
    print()


def obter_pergunta():
    pergunta = input("  Digite sua pergunta: ").strip()
    return pergunta


def gerar_resposta(pergunta):
    pergunta_lower = pergunta.lower()

    if "oi" in pergunta_lower or "ola" in pergunta_lower:
        return "Ola! Como posso te ajudar hoje?"
    elif "tudo bem" in pergunta_lower or "como vai" in pergunta_lower:
        return "Estou funcionando perfeitamente! E voce, como esta?"
    elif "nome" in pergunta_lower:
        return "Meu nome e ChatBot. Estou aqui para te ajudar!"
    elif "horas" in pergunta_lower or "hora" in pergunta_lower:
        return (
            "Nao tenho acesso ao relogio, mas voce pode verificar no seu dispositivo."
        )
    elif "obrigado" in pergunta_lower or "obrigada" in pergunta_lower:
        return "De nada! Fico feliz em ajudar."
    elif "tchau" in pergunta_lower or "ate logo" in pergunta_lower:
        return "Ate logo! Tenha um otimo dia."
    else:
        return "Recebi sua mensagem. No momento nao possuo uma resposta especifica, mas estou aprendendo!"


def criar_json(pergunta, resposta):
    estrutura = {"chatbot": {"pergunta": pergunta, "resposta": resposta}}
    return estrutura


def exibir_resultado(dados):
    dados_json = json.dumps(dados, indent=4, ensure_ascii=False)

    print()
    print("-" * 50)
    print("  MENSAGEM ORGANIZADA EM JSON")
    print("-" * 50)
    print()
    print(dados_json)
    print()
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()
    pergunta = obter_pergunta()

    if not pergunta:
        print()
        print("  [AVISO] Nenhuma pergunta digitada. Encerrando.")
        print()
        return

    resposta = gerar_resposta(pergunta)
    dados = criar_json(pergunta, resposta)

    exibir_resultado(dados)


main()
