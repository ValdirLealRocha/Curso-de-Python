# Aula 15 - https://youtu.be/tYvyHy1cE1s?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# O que são as Tuplas em Python

import os # permite usar comandos na linha de comandos do terminal...

# declaração de vaiáveil
l_carros = ["HRV", "Golf", "Argo"] # lista / array / vetor
t_carros = ("HRV", "Golf", "Argo") # Tupla - depois de criada não muda...

# DIFERENÇA ENTRE LISTA E TUPLA:
# lista pode ser inicializada... Lista usa []
# tuplas não pode ser alterada... Tupla usa ()

# imprime na tela a LISTA
os.system('cls') # limpa tela
print("-----------------------------------------")
print("LISTA de Carros")
for x in l_carros:
  print(x)

# imprime na tela a TUPLA
print("-----------------------------------------")
print("TUPLA de Carros")
for x in t_carros:
  print(x)

# Excessão para manipular a TUPLA... :(
# convertendo uma tupla numa lista...
os.system('cls') # limpa tela
l1_carros = list(t_carros) # pega a tupla e inicializa numa lista... Usando list()
l1_carros[2] = "Focus" # altero a lista...
t_carros = tuple(l1_carros) ## volto a lista numa TUPLA... Usando tuple()
print("-----------------------------------------")
print("TUPLA de Carros - tupla pra lista e lista pra tupla...")
for x in t_carros:
  print(x)

print("-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")

