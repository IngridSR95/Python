lista = []
#append
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)
#.copy()
l2 = lista.copy()
print(l2)

#.clear()
l2.clear()
print(l2)

cores = ["vermelho", "azul", "amarelo", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("amarelo"))

#adicionar 
cores.extend(["roxo","preto"])
print(cores)

#index encontra as ocorrências de cada uma selecionada
print(cores.index("vermelho"))
print(cores.index("azul"))
print(cores.index("preto"))

#pilhas (tira o último elemento da lista ou o elemento pedido)
'''
cores.pop()
cores.pop()
cores.pop()
cores.pop(0)
'''

#remove (tira o objeto selecionado)
cores.remove("azul")
print(cores)
cores.reverse()#espelha a lista
print(cores) 
'''ORDENAÇÃO DA LISTA
em ordem alfabética se String e crescente se numérica
'''
cores.sort() #apenas ordena
print(cores) 

cores.sort(reverse=True)
print(cores) 

'''cores.sort(key=i x: len(x)) #do menor para o menor em tamanho
print(cores)
cores.sort(key=i x: len(x), reverse=True) #maoir para o menor tamanho
print(cores)'''

#saber a quantidade de elementos 
len(cores)

sorted(cores, key=lambda x: len(x))
print(cores)