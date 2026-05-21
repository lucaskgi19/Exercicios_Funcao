import random
def imprime_diagonal():
    matriz =[
        [],
        [],
        []
    ]
    for linha in range(3):
        for coluna in range(3):
            numero = random.randint(1,100)
            matriz[linha].append(numero)

    for linha in matriz:
        print(linha)
    print("Diagonal da matriz: ")
    print(f"{matriz[0][0]}, {matriz[1][1]}, {matriz[2][2]}")
imprime_diagonal()