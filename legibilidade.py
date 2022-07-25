# Perguntando o texto
texto = input("Texto: ")

# Declarando variaveis
letras = 0
palavras = 1
frases = 0

# Loop verificando letra por letra
tamanho_texto = len(texto)
for i in range(tamanho_texto):

    # Contando as letras
    if texto[i] >= "a" and texto[i] <= "z":
        letras += 1
    elif texto[i] >= "A" and texto[i] <= "Z":
        letras += 1
    # Contando as palavras
    elif texto[i] == " ":
        palavras += 1
    # Contando as frases
    elif texto[i] == "." or texto[i] == "!" or texto[i] == "?":
        frases += 1

# Fazendo o calculo do indice
L = letras * 100 / palavras
S = frases * 100 / palavras
indice = 0.0588 * L - 0.296 * S - 15.8

# Imprimindo as notas
if indice < 1:
    print("Before Grade 1")
elif indice > 16:
    print("Grade 16+")
else:
    print("Grade " + str(round(indice)))

