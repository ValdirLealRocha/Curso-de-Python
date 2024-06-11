# Aula 14 - https://youtu.be/AqvSMMcybTI?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Loop While

import os # permite usar comandos na linha de comandos do terminal...

# declaração de vaiáveil
i = 0

# looping
os.system('cls') # limpa tela
while (i < 10): # controlar a variável, incremento e decremento...
  print(i)
  i += 1 # i = i + 1 

# looping
i = 0
os.system('cls') # limpa tela
while (i < 10): # controlar a variável, incremento e decremento...
  print(i)
  i += 1 # i = i + 1 
  if(i >= 5):
    break

os.system('cls') # limpa tela
# lista de carros
carros = ["HRV", "Golf", "Argo", "Onix", "Focus"]
# usar o looping para mostrar a lista na tela
i = 0
tam = len(carros) # pega o tamanho da lista
while(i < tam):
  print(carros[i])
  i += 1 # i = i + 1
print("Fim do Loop\n")

os.system('cls') # limpa tela
# lista de carros
carro = input("Digite o nome do novo carro: ")
# usar o looping para mostrar a lista na tela
i = 0
while(carro != "-1"):
  carros.append(carro)
  carro = input("Digite o nome do novo carro: ")

for x in carros:
  print(x)

print("Fim do Loop\n")


print("-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")

