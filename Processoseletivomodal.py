print("Questão 1")
def contar_letras_a(texto):
    contador = 0
    for letra in texto:
        if letra.islower() and letra == 'a':
            contador += 1
    return contador

entrada = input("Digite uma palavra ou frase: ")
quantidade_a = contar_letras_a(entrada)

print("Quantidade de letras 'a' minúsculas:", quantidade_a)


print("Questão 2")
def encontrar_repetidos(a, b):
    repetidos = []
    for num in a:
        if num in b and num not in repetidos:
            repetidos.append(num)
    return repetidos

# Mensagem de entrada
print("Digite os números do vetor A, separados por espaço:")
entrada_a = input().split()
vetor_a = [int(num) for num in entrada_a]

print("Digite os números do vetor B, separados por espaço:")
entrada_b = input().split()
vetor_b = [int(num) for num in entrada_b]

# Encontrar números repetidos
vetor_final = encontrar_repetidos(vetor_a, vetor_b)

# Mensagem de saída
print("Números repetidos encontrados nos dois vetores:")
print(vetor_final)



print("Questão 3")
# Solicitar a entrada dos dados
data = input("Insira os dados separados por vírgula: ")

# Separar os dados em uma lista
dados = data.split(',')

# Listas para armazenar os dados numéricos e as strings
numeros = []
strings = []

# Verificar cada elemento da lista
for dado in dados:
    # Remover espaços em branco do início e fim
    dado = dado.strip()
    
    # Verificar se o dado é numérico
    if dado.replace('.', '', 1).isdigit():
        numeros.append(dado)
    else:
        strings.append(dado)

# Exibir os dados numéricos
print("Dados numéricos:")
for numero in numeros:
    print(numero)

# Exibir as strings
print("Strings:")
for string in strings:
    print(string)

    