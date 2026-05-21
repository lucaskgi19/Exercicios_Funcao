def media():
    notas = []
    for linhas in range(5):
        n = int(input("digite suas notas: "))
        notas.append(n)
        print(notas)
        soma = sum(notas)
        media = soma / 5
    print(media)
media()