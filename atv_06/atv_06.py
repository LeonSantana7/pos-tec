def exibir_cabecalho():
    print("=" * 50)
    print("          CHATBOT INTELIGENTE")
    print("=" * 50)
    print()


def obter_pergunta():
    pergunta = input("  Voce: ").strip().lower()
    return pergunta


def gerar_resposta(pergunta):
    if pergunta == "oi":
        return "Ola!"
    elif pergunta == "como voce funciona?" or pergunta == "como você funciona?":
        return "Utilizo programacao e IA."
    elif pergunta == "":
        return "Nenhuma mensagem digitada. Por favor, tente novamente."
    else:
        return "Nao compreendi."


def exibir_resposta(resposta):
    print()
    print(f"  Chatbot: {resposta}")
    print()
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()
    pergunta = obter_pergunta()
    resposta = gerar_resposta(pergunta)
    exibir_resposta(resposta)


main()
