#DESAFIO

print("Bem-Vindas ao jogo!")
#rodadas = int(input("Quantas rodadas vocês desejam jogar? "))
pontos_jog1 = 0
pontos_jog2 = 0

rodadas = 3
nome1 = input("Jogadora 1 qual o seu nome? ").upper()
nome2 = input("Jogadora 2 qual o seu nome? ").upper()


for i in range(1, rodadas+1):
  print(f" {nome1}, escolha a sua jogada: pedra, papel ou tesoura: ")
  jogada_jogadora1 = input().lower()

  print(f" {nome2}, escolha a sua jogada: pedra, papel ou tesoura: ")
  jogada_jogadora2 = input().lower()

  #comparar as jogadas
    #pedra ganha da tesoura
  if jogada_jogadora1 == "pedra" and jogada_jogadora2 == "tesoura":
    print(f"{nome1} venceu a rodada")
    pontos_jog1 = pontos_jog1 + 1

  elif jogada_jogadora2 == "pedra" and jogada_jogadora1 == "tesoura":
    print(f"{nome2} venceu a rodada")
    pontos_jog2 = pontos_jog2 + 1

    #tesoura ganha da papel
  elif jogada_jogadora1 == "tesoura" and jogada_jogadora2 == "papel":
    print(f"{nome1} venceu a rodada")
    pontos_jog1 = pontos_jog1 + 1

  elif jogada_jogadora2 == "tesoura" and jogada_jogadora1 == "papel":
    print(f"{nome2} venceu a rodada")
    pontos_jog2 = pontos_jog2 + 1

    #papel ganha da pedra
  elif jogada_jogadora1 == "papel" and jogada_jogadora2 == "pedra":
    print(f"{nome1} venceu a rodada")
    pontos_jog1 = pontos_jog1 + 1

  elif jogada_jogadora2 == "papel" and jogada_jogadora1 == "pedra":
    print(f"{nome2} venceu a rodada")
    pontos_jog2 = pontos_jog2 + 1

    #EMPATE
  elif jogada_jogadora1 == "pedra" and jogada_jogadora2 == "pedra":
    print("EMPATE!")

  elif jogada_jogadora1 == "papel" and jogada_jogadora2 == "papel":
    print("EMPATE!")
  else:
    print("EMPATE!")
    break

if pontos_jog1 > pontos_jog2:
  print(f"{nome1}, GANHOU O JOGO")
elif pontos_jog2 > pontos_jog1:
  print(f"{nome2}, GANHOU O JOGO")
else:
  print(f"{nome1} e {nome2}, EMPATARAM O JOGO")
