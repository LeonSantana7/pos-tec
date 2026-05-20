import urllib.request
import json


def exibir_cabecalho():
    print("=" * 50)
    print("      SISTEMA DE CONSULTA DE PAISES")
    print("=" * 50)
    print()


def consultar_api(pais):
    url = f"https://restcountries.com/v3.1/name/{pais}"

    try:
        requisicao = urllib.request.Request(url, headers={"User-Agent": "Python"})
        with urllib.request.urlopen(requisicao) as resposta:
            dados = json.loads(resposta.read().decode())
            return dados[0], None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, "Pais nao encontrado. Verifique o nome informado."
        return None, f"Erro HTTP: {e.code}"
    except urllib.error.URLError:
        return None, "Erro de conexao. Verifique sua internet."
    except json.JSONDecodeError:
        return None, "Erro ao interpretar os dados retornados pela API."
    except Exception as e:
        return None, f"Erro inesperado: {str(e)}"


def exibir_resultado(dados):
    nome_oficial = dados["name"]["official"]
    nome_comum = dados["name"]["common"]
    capital = dados["capital"][0] if "capital" in dados else "Nao informada"
    populacao = f"{dados['population']:,}".replace(",", ".")

    print("-" * 50)
    print("  INFORMACOES DO PAIS")
    print("-" * 50)
    print(f"  Nome comum    : {nome_comum}")
    print(f"  Nome oficial  : {nome_oficial}")
    print(f"  Capital       : {capital}")
    print(f"  Populacao     : {populacao} habitantes")
    print("-" * 50)
    print()


def main():
    exibir_cabecalho()
    print("  Consultando dados do Brasil...")
    print()

    dados, erro = consultar_api("brazil")

    if erro:
        print(f"  [ERRO] {erro}")
        print()
    else:
        exibir_resultado(dados)


main()
