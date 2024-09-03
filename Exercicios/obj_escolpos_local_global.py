'''OBJETOS DE PRIMEIRA CLASSE'''
#Strings e funções são exemplos de objetos de primeira classe

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 5, subtrair)

#Em variáveis
op = somar
print(op(1, 19))

'''ESCOPO LOCAL E ESCOPO GLOBAL'''
#esta prática deve ser evitada
salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista.append(2)
    salario += bonus
    return salario

lista = [1] #por referência, obj mutável
novo_salario = salario_bonus(500, lista)
print(novo_salario)
print(lista)