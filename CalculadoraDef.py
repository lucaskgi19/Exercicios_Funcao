def soma():
    num1 = int(input("Digite o 1º numero: "))
    num2 = int(input("Digite o 2º numero: "))
    soma = num1 + num2
    print(f"O resultado da soma é: {soma}")

def sub():
    num1 = int(input("Digite o 1º numero: "))
    num2 = int(input("Digite o 2º numero: "))
    sub = num1 - num2
    print(f"O resultado da subtração é: {sub}")

def multi():
    num1 = int(input("Digite o 1º numero: "))
    num2 = int(input("Digite o 2º numero: "))
    multi = num1 * num2
    print(f"O resultado da multiplicação é: {multi}")

def div():
    num1 = float(input("Digite o 1º numero: "))
    num2 = float(input("Digite o 2º numero: "))
    div = num1 / num2
    print(f"O resultado da divisão é: {div}")



def menu():
    while True:
        n = int(input("Escolha uma opcao: 1 - soma; 2 - sutracao; 3 - multiplicacao; 4 - divisao; 0 - sair: "))
        if n == 1:
            soma()
        elif n == 2:
            sub()
        elif n == 3:
            multi()
        elif n == 4:
            div()
        elif n == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opção invalida.")
menu()