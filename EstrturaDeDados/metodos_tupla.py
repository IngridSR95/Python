'''MÉTODOS DA CLASSE TUPLE'''

cores = ("vermelho", "azul", "amarelo", "azul",)

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("amarelo"))

print(cores.index("vermelho"))
print(cores.index("azul"))

print(len(cores))

carros = ("gol") 
print(isinstance(carros, tuple))