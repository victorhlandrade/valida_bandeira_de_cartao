def validar_bandeira_cartao(numero_cartao):
    """
    Valida a bandeira de um cartão de crédito com base nos primeiros números e no comprimento.
    """
    numero_cartao = str(numero_cartao)
    comprimento = len(numero_cartao)

    # Dicionário com as regras de validação
    bandeiras = {
        "Mastercard": {"prefixos": range(51, 56), "comprimento": 16},
        "Visa": {"prefixos": [4], "comprimento": 16},
        "American Express": {"prefixos": [34, 37], "comprimento": 15},
        "Diners Club": {"prefixos": [300, 301, 302, 303, 304, 305, 36, 38], "comprimento": 14},
        "Discover": {"prefixos": [6011, 65] + list(range(622126, 622926)), "comprimento": 16},
        "EnRoute": {"prefixos": [2014, 2149], "comprimento": 15},
        "JCB": {"prefixos": list(range(3528, 3590)), "comprimento": 16},
        "Voyager": {"prefixos": [8699], "comprimento": 15},
        "HiperCard": {"prefixos": [606282, 637095, 637568, 637599, 637609, 637612], "comprimento": 16},
        "Aura": {"prefixos": [50], "comprimento": 16},
    }

    for bandeira, regras in bandeiras.items():
        prefixos = regras["prefixos"]
        if any(str(numero_cartao).startswith(str(prefixo)) for prefixo in prefixos) and comprimento == regras["comprimento"]:
            return f"Bandeira: {bandeira}"

    return "Bandeira desconhecida ou número inválido."


# Exemplo de uso
if __name__ == "__main__":
    try:
        numero = input("Digite o número do cartão de crédito: ").strip()
        if not numero.isdigit():
            print("Erro: O número do cartão deve conter apenas dígitos.")
        else:
            resultado = validar_bandeira_cartao(numero)
            print(resultado)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")