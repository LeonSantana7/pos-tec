def exibir_cabecalho():
    print("=" * 50)
    print("       ASSISTENTE VIRTUAL INTERATIVO")
    print("=" * 50)
    print()
    print("  Assistente ativo e aguardando perguntas.")
    print("  Digite 'sair' a qualquer momento para encerrar.")
    print()
    print("-" * 50)
    print()


def obter_pergunta():
    pergunta = input("  Voce: ").strip().lower()
    return pergunta


def gerar_resposta(pergunta):
    if "oi" in pergunta or "ola" in pergunta or "bom dia" in pergunta:
        return "Ola! Como posso te ajudar?"

    elif "tudo bem" in pergunta or "como vai" in pergunta:
        return "Estou funcionando perfeitamente! E voce?"

    elif "nome" in pergunta or "quem e voce" in pergunta:
        return "Sou um assistente virtual. Estou aqui para te ajudar!"

    elif "como voce funciona" in pergunta or "como você funciona" in pergunta:
        return "Utilizo programacao e Inteligencia Artificial para responder suas perguntas."

    elif "capital" in pergunta and "brasil" in pergunta:
        return "A capital do Brasil e Brasilia, localizada no Distrito Federal."

    elif "python" in pergunta:
        return "Python e uma linguagem de programacao muito utilizada em IA e ciencia de dados."

    elif "obrigado" in pergunta or "obrigada" in pergunta or "valeu" in pergunta:
        return "De nada! Fico feliz em ajudar. Pode perguntar mais."

    elif pergunta == "":
        return "Nenhuma mensagem digitada. Por favor, tente novamente."

    else:
        return "Nao compreendi sua pergunta. Pode reformular?"


def exibir_resposta(resposta):
    print()
    print(f"  Assistente: {resposta}")
    print()
    print("-" * 50)
    print()


def exibir_encerramento(total_interacoes):
    print()
    print("=" * 50)
    print("          SESSAO ENCERRADA")
    print("=" * 50)
    print(f"  Total de interacoes : {total_interacoes}")
    print("  Ate logo!")
    print("=" * 50)
    print()


def main():
    exibir_cabecalho()

    total_interacoes = 0

    while True:
        pergunta = obter_pergunta()

        if pergunta == "sair":
            exibir_encerramento(total_interacoes)
            break

        resposta = gerar_resposta(pergunta)
        exibir_resposta(resposta)
        total_interacoes += 1


main()
