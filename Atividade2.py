import random
def maior():
    lista = []
    for linha in range(3):
        numero = random.randint(1,1000)
        lista.append(numero)
    print(lista)
    print("O maior valor da lista é:")
    print(max(lista))

maior()