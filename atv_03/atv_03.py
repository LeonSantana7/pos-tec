def exibir_cabecalho():
    print("=" * 50)
    print("       SISTEMA DE AUTENTICACAO DE USUARIOS")
    print("=" * 50)
    print()


def obter_credenciais():
    usuario = input("  Usuario: ").strip()
    senha = input("  Senha  : ").strip()
    return usuario, senha


def autenticar(usuario, senha):
    base_usuarios = {"admin": "admin123", "joao": "joao2024", "maria": "maria@99"}

    if usuario in base_usuarios and base_usuarios[usuario] == senha:
        return True
    return False


def exibir_resultado(usuario, autenticado):
    print()
    print("-" * 50)
    print("  RESULTADO DA AUTENTICACAO")
    print("-" * 50)
    print(f"  Usuario : {usuario}")

    if autenticado:
        print("  Status  : ACESSO PERMITIDO")
        print()
        print("  Bem-vindo ao sistema. Suas credenciais")
        print("  foram validadas com sucesso.")
    else:
        print("  Status  : ACESSO NEGADO")
        print()
        print("  Usuario ou senha incorretos.")
        print("  Caso necessario, contate o administrador.")

    print("-" * 50)


def main():
    exibir_cabecalho()
    usuario, senha = obter_credenciais()
    autenticado = autenticar(usuario, senha)
    exibir_resultado(usuario, autenticado)
    print()


main()
