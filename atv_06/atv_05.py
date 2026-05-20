def exibir_cabecalho():
    print("=" * 50)
    print("     SISTEMA DE HISTORICO DE PERGUNTAS IA")
    print("=" * 50)
    print()


def obter_pergunta():
    pergunta = input("  Digite sua pergunta: ").strip()
    return pergunta


def salvar_historico(pergunta, nome_arquivo):
    from datetime import datetime

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = f"[{timestamp}] {pergunta}\n"

    try:
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
            arquivo.write(registro)
        return registro, None
    except IOError as e:
        return None, f"Erro ao salvar o arquivo: {str(e)}"


def exibir_confirmacao(pergunta, registro, nome_arquivo):
    print()
    print("-" * 50)
    print("  CONFIRMACAO DE REGISTRO")
    print("-" * 50)
    print(f"  Pergunta  : {pergunta}")
    print(f"  Arquivo   : {nome_arquivo}")
    print(f"  Registro  : {registro.strip()}")
    print()
    print("  Pergunta salva com sucesso no historico.")
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()

    nome_arquivo = "historico_ia.txt"
    pergunta = obter_pergunta()

    if not pergunta:
        print()
        print("  [AVISO] Nenhuma pergunta digitada. Encerrando.")
        print()
        return

    registro, erro = salvar_historico(pergunta, nome_arquivo)

    if erro:
        print()
        print(f"  [ERRO] {erro}")
        print()
    else:
        exibir_confirmacao(pergunta, registro, nome_arquivo)


main()
