'''MÉTODOS ÚTEIS DA CLASSE STRING'''
#MAIÚSCULA, minúscula e Título

curso = "PyThOn"
print(curso)
print(curso.upper()) #MAIÚSCULA
print(curso.lower()) #minúscula
print(curso.title()) #Título

#Eliminando Espaços em Branco
curso = "!   Python  !"
print(curso.strip()) #remove qualquer espaço em branco
print(curso.lstrip()) #remove apenas da esquerda
print(curso.rstrip()) #remove apenas da direita

#Junções e Centralizações
curso = "Python"
print(curso.center(10, '#'))
'''O texto fica centralizado de acordo com o número de 
caractéres definido (10) e completa com o símbolo definido'''

print(".".join(curso)) #intercala o simbolo à palavra

