'''Desafio de Código - Criando um Sistema Bancário com Python'''

#Criar um sistema bancário com as operações: sacar, depositar e vizualizar extrato.


menu = '''
------BEM-VINDO AO DIO BANK :)----
    digite a operção desejada:
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [s] Sair
----------------------------------
'''

#Variáveis:
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#loop para as operações
while True:
    operacao = input(menu)

    #Operação de Depósito
    if (operacao == '1'):
        valor = float(input("Informe o valor do Depósito:"))
        if(valor > 0):
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("valor inválido!")

    #Operação de Saque
    elif(operacao == '2'):
        valor = float(input("Informe o valor do Saque:"))
        #excedeu_saques = numero_saques >= LIMITE_SAQUES

        if (valor > limite):
            print("Falha na Operação: o valor de saque desejado excede o limite!")
        elif(valor > saldo):
            print("Falha na Operação: o valor de saque desejado excede o saldo!")
        elif (valor > 0):
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            if (numero_saques >= LIMITE_SAQUES):
                print("Falha na Operação: quandidade de saques excedida!")
        else:
            print("Operação falhou! O valor informado é Inválido!")

    #Exibição do Extrato
    elif (operacao == '3'):
        print("------------ EXTRATO -------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("----------------------------------")

    #Saída
    elif (operacao == 's'):
        break
    else:
        print("Operção Inválida, por favor, selecione a opção desejada!")
    