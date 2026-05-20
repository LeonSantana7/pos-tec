import urllib.request
import json


def exibir_cabecalho():
    print("=" * 50)
    print("      SISTEMA DE CONSULTA A API DO GITHUB")
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


def exibir_resultado(dados):
    print("-" * 50)
    print("  ENDPOINTS DISPONIVEIS NA API DO GITHUB")
    print("-" * 50)
    print()

    for chave, valor in dados.items():
        print(f"  {chave}")
        print(f"  {valor}")
        print()

    print("-" * 50)
    print(f"  Total de endpoints retornados: {len(dados)}")
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()
    print("  Consultando API do GitHub...")
    print()

    dados, erro = consultar_api()

    if erro:
        print(f"  [ERRO] {erro}")
        print()
    else:
        exibir_resultado(dados)


main()
