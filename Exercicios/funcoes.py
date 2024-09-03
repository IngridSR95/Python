'''FUNÇÕES'''
def exibir_mensagem():
    print("Olá Mundo!\n")

def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo, {nome}!\n")

def exibir_mensagem_3(nome = "Antônio"):
    print(f"Seja bem-vindo, {nome}!\n")

exibir_mensagem()
exibir_mensagem_2("Pedro")
exibir_mensagem_3()
exibir_mensagem_3(nome = "Matheus")

#Lista que retorna números:

def calcular_total(numero):
    return sum(numero)

def retorns_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34]))
print(retorns_antecessor_sucessor(10))

#ARGUMENTOS NOMEADOS
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro ("Fiat", "Palio", 1999, "ABC-1234\n")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234\n")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234\n"}) #dicionário

#*args e **kwargs (tupla e dicionário)
def exibir_poema (data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema ("Dom, 01 set 2024", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)



'''FUNÇÕES EM PYTHON Parte 2'''
#Positional Only (valores passados por posição)
def criar_carrop (modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carrop ("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
'''criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido'''

#Keyword Only (valores passados por nome)
def criar_carrok (*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carrok (modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
'''criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido'''

#Keyword and Positional
def criar_carro (modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro ("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
'''criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido'''

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
salvar_carro ("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC- 1234"})

