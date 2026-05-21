import random
def maior_elemento():
    lista = []
    for linha in range(5):
        numero = random.randint(1,1000)
        lista.append(numero)
    print(lista)
    print("O maior valor da lista é:")
    print(max(lista))

maior_elemento()