# set é uma coleção que elimina itens duplicados
#ele pode mudar a ordem dos dados (tira a primeira ocorrência)

set([1, 2, 3, 1, 3, 4])

set("abacaxi")

set(("palio", "gol", "palio", "celta")) #também funciona com tuplas

# Acessando dados em set
#conjuntos empython não suportam indexação nem fatiamento, portanto é necessário converte-los para listas

numeros = {1, 2, 3, 2}#conjunto
print(numeros)

numeros = list(numeros)

print(numeros[0])


#iteras = percorrer
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

#Função enumerate para saber o indice
carros = {"gol", "celta", "palio"}
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


"""MÉTODOS DA CLASSE SET"""
#{}.union
conjunto_a = {1, 2}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b))

#{}.intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.intersection(conjunto_b))

#{}.difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#{}.symmetric_difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.symmetric_difference(conjunto_b))

#{}.issuperset (retorna boolean)
conjunto_a = {1, 2, 3}
conjunto_b = {4, 2, 3, 5, 6, 1}
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

#{}.isdisjoint (retorna boolean)
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}
print(conjunto_a.isdisjoint(conjunto_b)) #não tem nenhum elemento em comum com a
print(conjunto_a.isdisjoint(conjunto_c)) #há intersecção com o a

#{}.add
sorteio = {1, 23}
#adiciona, mas não adciona os já existentes
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

#{}.clear
print(sorteio)
sorteio.clear()
print(sorteio)

#{}.copy
sorteio.copy()

#{}.discard
print(conjunto_a)

conjunto_a.discard(1)
print(conjunto_a)

'''#{}.pop
numero = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numero)
print(numero.pop(0))
print(numero.pop(1))
print(numero)'''

#{}.remove
numero = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numero.remove(0)
print(numero)

#len
len(numero)

#in saber se o objeto etá no conjunto
print(1 in numeros)
print(10 in numeros)