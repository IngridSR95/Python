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

