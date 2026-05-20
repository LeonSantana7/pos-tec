def exibir_cabecalho():
    print("=" * 50)
    print("        CHATBOT DE ATENDIMENTO AO CLIENTE")
    print("=" * 50)
    print()
    print("  Bem-vindo ao atendimento automatizado.")
    print("  Digite sua mensagem para iniciar.")
    print()


def processar_mensagem(mensagem):
    mensagem = mensagem.strip().lower()

    if mensagem == "oi":
        return "Ola! Como posso ajudar?", False
    elif mensagem == "tchau":
        return "Atendimento encerrado. Tenha um otimo dia!", True
    elif mensagem == "":
        return "Nenhuma mensagem digitada. Por favor, tente novamente.", False
    else:
        return "Nao entendi sua mensagem. Pode reformular?", False


def exibir_resposta(resposta):
    print()
    print(f"  Chatbot: {resposta}")
    print()


def main():
    exibir_cabecalho()

    while True:
        mensagem = input("  Voce: ")
        resposta, encerrar = processar_mensagem(mensagem)
        exibir_resposta(resposta)

        if encerrar:
            print("-" * 50)
            print("  Sessao encerrada.")
            print("=" * 50)
            print()
            break


main()
