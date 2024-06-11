# Aula 16 - https://youtu.be/zBLCSLW5Y54?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Matrizes

import os # permite usar comandos na linha de comandos do terminal...

# declaração de vaiáveil
carros = ["HRV", "Golf", "Focus", "Argo"] # array / vetor / LISTA

os.system('cls') # limpa tela
print("-----------------------------------------")
# lista carros...
for x in carros:
  print(x)

os.system('cls') # limpa tela
print("-----------------------------------------")
# Array multidimencional - MATRIZ
carros = [
  ["Modelo", "HRV"], 
  ["Fabricante", "Honda"], 
  ["Ano", 2016]
] # MATRIZ - podemos utilizar vários tipoos de dados...

# imprime manual
print(carros[0][0] + " - " + carros[0][1])
print(carros[1][0] + " - " + carros[1][1])
print(carros[2][0] + " - " + str(carros[2][1])) # atentos as strings
print("-----------------------------------------")

# lista carros com o for...
for l,c in carros:
  # str(c) - atentos as strings por causa do item 2016
  print("Linha: " + l + " | Coluna: " + str(c))
print("-----------------------------------------")

# manipular a matriz
carros.append(["Cor", "Prata"]) # adiciona dados
carros[2][1] = 2019 # edita/altera o elemento
for l,c in carros:
  print(l + " | " + str(c))

print("-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")

