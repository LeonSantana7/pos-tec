import urllib.request
import json


def exibir_cabecalho():
    print("=" * 50)
    print("       SISTEMA DE COTACAO DE MOEDAS")
    print("=" * 50)
    print()


def consultar_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    try:
        with urllib.request.urlopen(url) as resposta:
            dados = json.loads(resposta.read().decode())
            return dados["USDBRL"], None
    except urllib.error.URLError:
        return None, "Erro de conexao. Verifique sua internet."
    except KeyError:
        return None, "Erro ao interpretar os dados da API."
    except Exception as e:
        return None, f"Erro inesperado: {str(e)}"


def exibir_resultado(dados):
    print("-" * 50)
    print("  COTACAO DO DOLAR AMERICANO (USD)")
    print("-" * 50)
    print(f"  Valor atual : R$ {float(dados['bid']):.2f}")
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()
    print("  Consultando cotacao em tempo real...")
    print()

    dados, erro = consultar_cotacao()

    if erro:
        print(f"  [ERRO] {erro}")
    else:
        exibir_resultado(dados)


main()
