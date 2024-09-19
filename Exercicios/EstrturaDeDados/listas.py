#Criando Listas
frutas = ["laranja", "maca", "uva"]

letras = list("python") #elemento iteravel

numeros = list(range(10)) #0 a 9

carro = ["Ferrari", "F8", 42000, 2020, 2900, "São Paulo", True]

# Acesso Direto
print(frutas[0])
print(frutas[2])

#Indices negativos, pega do último elemento 
frutas = ["laranja", "maca", "uva", "roma"]

print(frutas[-1])
print(frutas[-3])

#Listas Alinhadas para representação de Matriz
matriz = [
    ["a", 1, 2],
    [ 3,"b", 4],
    [5, 6, "c"]
]

print(matriz [0])
print(matriz [0][0])
print(matriz [0][-1])
print(matriz [-1][-1])

'''FATIAMENTO
índice inicial e/ou final para acessar o conjunto. ou pode-se 
informar quantas posições o cursor deve "pular" no acesso
'''
palavra = list("python")

print(palavra[2:])
print(palavra[:2])
print(palavra[1:3])
print(palavra[0:3:2])
print(palavra[::])
print(palavra[::-1]) #espelha

#Iterar listas com for (acessar os itens da lista)

carros = ["Ferrari", "F8", 42000, 2020, 2900, "São Paulo", True]

for carro in carros:
    print(carro)

#função enumerate quando é necessário saber qual o índice do obj
for indice, carro in enumerate(carro):
    print(f"{indice}: {carro}")
    
'''COMPREENSÃO DE LISTAS
criar uma nova lista com base nos valores de uma lista existente
(filtro) ou gerar uma nova lista aplicando alguma modificação nos 
elementos de uma lista existente.
'''
numeros = [1, 20, 30, 45, 63, 8, 97]
pares = []
#forma 1
for numeros in numeros:
    if numeros % 2 == 0:
        pares.append(numeros)
print(pares)

#compreensão
pares = [numero for numero in numeros if numeros % 2 == 0]
print(pares)
