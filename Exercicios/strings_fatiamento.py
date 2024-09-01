'''MÉTODOS ÚTEIS DA CLASSE STRING'''
#MAIÚSCULA, minúscula e Título

curso = "PyThOn"
print(curso)
print(curso.upper()) #MAIÚSCULA
print(curso.lower()) #minúscula
print(curso.title()) #Título
print(" ")

#Eliminando Espaços em Branco
curso = "!   Python  !"
print(curso.strip()) #remove qualquer espaço em branco
print(curso.lstrip()) #remove apenas da esquerda
print(curso.rstrip()) #remove apenas da direita
print(" ")

#Junções e Centralizações
curso = "Python"
print(curso.center(10, '#'))
'''O texto fica centralizado de acordo com o número de 
caractéres definido (10) e completa com o símbolo definido'''

print(".".join(curso)) #intercala o simbolo à palavra
print(" ")

'''INTERPOLAÇÃO DE VARIÁVEIS'''
nome = "Ingrid"
idade = 19
linguagem = "Python"

#Old Style % (%d int e %f float)
print("Olá, sou %s. Eu tenho %d anos de idade e estudo %s" %(nome, idade, linguagem))
print(" ")

#Método Format
print("Olá, sou {}. Eu tenho {} anos de idade e estudo {}".format(nome, idade, linguagem))
print(" ")

print("Olá, sou {2}. Eu tenho {1} anos de idade e estudo {0}".format(linguagem, idade, nome))
print(" ")

#Método f-string (melhor forma)
print(f"Olá, sou {nome}. Eu tenho {idade} anos de idade e estudo {linguagem}")
print(" ")

#Formatar strings com f-string
PI = 3.14159
print(f"Valor de PI: {PI:.2f}") #numero de casas dps do .
print(f"Valor de PI: {PI:10.2f}")