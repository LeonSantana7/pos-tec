import urllib.request
import json


def exibir_cabecalho():
    print("=" * 50)
    print("    SISTEMA DE COLETA E ARMAZENAMENTO DE DADOS")
    print("=" * 50)
    print()


def consultar_api():
    url = "https://api.github.com"

    try:
        requisicao = urllib.request.Request(url, headers={"User-Agent": "Python"})
        with urllib.request.urlopen(requisicao) as resposta:
            dados = json.loads(resposta.read().decode())
            return dados, None
    except urllib.error.URLError:
        return None, "Erro de conexao. Verifique sua internet."
    except json.JSONDecodeError:
        return None, "Erro ao interpretar os dados retornados pela API."
    except Exception as e:
        return None, f"Erro inesperado: {str(e)}"


def salvar_json(dados, nome_arquivo):
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        return True, None
    except IOError as e:
        return False, f"Erro ao salvar o arquivo: {str(e)}"


def exibir_resultado(dados, nome_arquivo):
    print("-" * 50)
    print("  RESUMO DA OPERACAO")
    print("-" * 50)
    print(f"  API consultada    : https://api.github.com")  # noqa: F541
    print(f"  Registros obtidos : {len(dados)}")
    print(f"  Arquivo salvo     : {nome_arquivo}")
    print("-" * 50)
    print()
    print("  Previa dos dados salvos:")
    print()

    for i, (chave, valor) in enumerate(dados.items()):
        if i >= 5:
            print(f"  ... e mais {len(dados) - 5} registros.")
            break
        print(f"  {chave}: {valor}")

    print()
    print("-" * 50)
    print("  Dados armazenados com sucesso.")
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()
    nome_arquivo = "dados_api.json"

    print("  Consultando API...")
    dados, erro = consultar_api()

    if erro:
        print(f"  [ERRO] {erro}")
        print()
        return

    print("  Salvando dados no arquivo...")
    print()

    salvo, erro = salvar_json(dados, nome_arquivo)

    if erro:
        print(f"  [ERRO] {erro}")
        print()
        return

    exibir_resultado(dados, nome_arquivo)


main()
