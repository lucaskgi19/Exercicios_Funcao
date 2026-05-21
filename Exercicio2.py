def e_palindromo():
    texto = input("Digite um texto: ")
    texto_invertido = texto[::-1]
    print(texto_invertido)
    if texto == texto_invertido:
        True
        print("Esse texto é um palindromo.")
    else:
        False
        print("Esse texto não é um palindromo.")
e_palindromo()