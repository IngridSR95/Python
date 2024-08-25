nome = input("qual é o seu nome? ")
snome = input(f"\n{nome}, qual o seu sobrenome? ")

print(nome, snome)
print(nome, snome, end="...\n")
print(nome, snome, sep="#") # "Ingrid#Rodrigues"