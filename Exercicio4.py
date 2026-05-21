texto = input("Digite um texto: ")
caractere = "a"

def contar_caracteres(texto,caractere):
    contador = 0
    for letra in texto:
        if letra == caractere:
            contador += 1
    print(f"O caractere a aparece {contador} vezes no texto")
contar_caracteres(texto,caractere)