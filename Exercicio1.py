import random
def soma_elementos():
    soma = []
    for linha in range(5):
        numero = random.randint(1,1000)
        soma.append(numero)
        adição = sum(soma)
    print(soma)
    print(f"soma dos valores: {adição} ")

soma_elementos()