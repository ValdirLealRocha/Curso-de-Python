# Aula 18 - https://youtu.be/XpqWFn-gnFI?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Jogo simples de adivinhação em Python

import random # gera número aleatório...
import os # permite usar comandos na linha de comandos do terminal...

# declaração de vaiáveil
erros = 0 # erroa do jogador
sorteado = random.randrange(0, 100) # um número aleatório entre 0 e 100
# número digitado pelo jogador
# captura dados via teclado... 
# Tem que ser número, ou validar este processo...
print("-----------------------------------------")
jogador = int(input("Digite seu número: "))

while (sorteado != jogador) :
  os.system('cls') # limpa tela
  # validação
  if (sorteado > jogador):
    print("ERRO, o número sorteado é MAIOR que o número informado!")
  elif(sorteado < jogador):
    print("ERRO, o número sorteado é MENOR que o número informado!")
  # incrementa o erro
  erros += 1
  # solicitar novo número
  jogador = int(input("Digite um NOVO número: "))
print("Número " + str(jogador) + ", você acertou em " + str(erros + 1) + " tentativas.5")

print("-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")

