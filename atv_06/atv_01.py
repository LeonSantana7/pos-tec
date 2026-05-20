def exibir_cabecalho():
    print("=" * 50)
    print("         ASSISTENTE VIRTUAL INTELIGENTE")
    print("=" * 50)
    print()


def obter_pergunta():
    pergunta = input("  Voce: ").strip()
    return pergunta


def gerar_resposta(pergunta):
    pergunta_lower = pergunta.lower()

    if (
        "oi" in pergunta_lower
        or "ola" in pergunta_lower
        or "bom dia" in pergunta_lower
        or "boa tarde" in pergunta_lower
    ):
        return "Ola! Seja bem-vindo. Como posso te ajudar hoje?"

    elif (
        "tudo bem" in pergunta_lower
        or "como vai" in pergunta_lower
        or "como esta" in pergunta_lower
    ):
        return "Estou funcionando perfeitamente! Pronto para responder suas perguntas."

    elif "nome" in pergunta_lower or "quem e voce" in pergunta_lower:
        return "Sou um assistente virtual. Fui desenvolvido para responder suas perguntas automaticamente."

    elif "horas" in pergunta_lower or "que horas" in pergunta_lower:
        return "Nao tenho acesso ao relogio do sistema, mas voce pode verificar no seu dispositivo."

    elif (
        "clima" in pergunta_lower
        or "tempo" in pergunta_lower
        or "chuva" in pergunta_lower
    ):
        return "Para informacoes de clima em tempo real, recomendo consultar a previsao do tempo da sua regiao."

    elif "capital" in pergunta_lower and "brasil" in pergunta_lower:
        return "A capital do Brasil e Brasilia, localizada no Distrito Federal."

    elif "inteligencia artificial" in pergunta_lower or "ia" in pergunta_lower:
        return "Inteligencia Artificial e a area da computacao que desenvolve sistemas capazes de simular o raciocinio humano."

    elif "python" in pergunta_lower:
        return "Python e uma linguagem de programacao de alto nivel, muito utilizada em IA, ciencia de dados e automacao."

    elif (
        "obrigado" in pergunta_lower
        or "obrigada" in pergunta_lower
        or "valeu" in pergunta_lower
    ):
        return "De nada! Fico feliz em ajudar. Se tiver mais duvidas, pode perguntar."

    elif (
        "tchau" in pergunta_lower
        or "ate logo" in pergunta_lower
        or "encerrar" in pergunta_lower
    ):
        return "Ate logo! Tenha um excelente dia."

    elif pergunta == "":
        return "Nenhuma pergunta foi digitada. Por favor, tente novamente."

    else:
        return "Nao possuo uma resposta especifica para isso ainda. Tente reformular sua pergunta."


def exibir_resposta(resposta):
    print()
    print(f"  Assistente: {resposta}")
    print()
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()
    print("  Ola! Digite sua pergunta abaixo.")
    print("  (Digite 'tchau' para encerrar)")
    print("-" * 50)
    print()

    pergunta = obter_pergunta()
    resposta = gerar_resposta(pergunta)

    exibir_resposta(resposta)


main()
