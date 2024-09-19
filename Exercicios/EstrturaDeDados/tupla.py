# Criando Tuplas - Estrutura imutável

frutas = ('laranja', 'pera', 'morango',)

letras = tuple("python")

numeros = tuple([1,2, 3, 4])

pais = ("Brasil",)

'''Acessando os Valores da tupla
é válido, com os indices positivos e negativos'''

# TUPLAS ANINHADAS - 'tabelas'

matriz = (
    ("a", 1, 2),
    ( 3,"b", 4),
    (5, 6, "c")
)

print(matriz [0])
print(matriz [0][0])
print(matriz [0][-1])
print(matriz [-1][-1])

# FATIAMENTO

palavra = tuple("python")

print(palavra[2:])
print(palavra[:2])
print(palavra[1:3])
print(palavra[0:3:2])
print(palavra[::])
print(palavra[::-1]) #espelha