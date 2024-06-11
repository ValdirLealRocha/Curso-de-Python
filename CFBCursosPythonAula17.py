# Aula 17 - https://youtu.be/CRwWTw7ayc8?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Dictionary - é uma coleção aberta, podemos manipular a vontade...

import os # permite usar comandos na linha de comandos do terminal...

# declaração de vaiáveil
# [] array
# () tuple
# {} dictionary
#         Key/Chave   e  Value/valor
carro = {
  "Fabricante" : "Honda", 
  "Modelo" : "HRV", 
  "Ano" : "2016", 
  "Cor" : "Prata"
  }

os.system('cls') # limpa tela
print("-----------------------------------------")
print(carro)

print("-----------------------------------------")
print(carro["Modelo"]) # agora com colchetes usa a chave pra mostrar o valor...
mod = carro.get("Modelo") ## similar a linha de cima... Usando um método..
print("mod: " + mod)
print(carro["Fabricante"]) # agora com colchetes usa a chave pra mostrar o valor...
fab = carro.get("Fabricante") ## similar a linha de cima... Usando um método..
print("fab: " + fab)

print("-----------------------------------------")
carro["Cor"] = "Preto"
print(carro)

print("-----------------------------------------")
for x in carro:
  print("listar x | " + x) # imprime as chaves, após percorrer o dictionary...

print("-----------------------------------------")
for x in carro:
  print("Listar carro[x] | " + carro[x]) # percorre as chaves e imprime os valores...

print("-----------------------------------------")
for x in carro:
  print("Listar x e carro[x] | " + x + ": " + carro[x]) # percorre as chaves e imprime os valores...

print("-----------------------------------------")
for c, v in carro.items():
  print("Listar c e v | " + c + ": " + v) # percorre as chaves e imprime os valores...

print("-----------------------------------------")
if ("Modelo" in carro): ## verificação/validação
  print("SIM, o modelo é uma Chave")

print("-----------------------------------------")
print(carro)
print("Tamanho do Dictionary: " + str(len(carro)))
# ao inicialiar um novo ele adiciona ao dictionary
# inicializa uma valor a uma chave...
carro["Cambio"] = "Automático"
print("Tamanho do Dictionary: " + str(len(carro)))
print(carro)

# remover uma chave e seu valor...
print("-----------------------------------------")
carro.pop("Cambio") # outra forma > del carro["Cambio"]
print("Tamanho do Dictionary: " + str(len(carro)))
print(carro)

# remover tudo no dictionary...
print("-----------------------------------------")
carro.clear()
print("Tamanho do Dictionary: " + str(len(carro)))

# dictionary um  de um dictionary...
print("-----------------------------------------")
carros = {
  "Carro1":{
    "Fabricante":"Honda",
    "Modelo":"HRV"
  },
  "Carro2":{
    "Fabricante":"Volkswagem",
    "Modelo":"Golf"
  },
  "Carro3":{
    "Fabricante":"Ford",
    "Modelo":"Focus"
  }
}
print(carros["Carro1"]) # sem o texto pra concatenar...
#print("Carro1 - " + str(carros["Carro1"])) # com o texto concatenado...
print(carros["Carro1"]["Fabricante"]) # sem o texto pra concatenar...
#print("Carro1 - " + str(carros["Carro1"]["Fabricante"])) # com o texto concatenado...
print("Tamanho do Dictionary: " + str(len(carros)))

print("-----------------------------------------")
carro1 = {
  "Fabricante":"Honda",
  "Modelo":"HRV",
}
carro2 = {
  "Fabricante":"Volkswagem",
  "Modelo":"Golf",
}
carro3 = {
  "Fabricante":"Ford",
  "Modelo":"Focus",
}

carros = {
  "C1" : carro1,
  "C2" : carro2,
  "C3" : carro3,
}

print(carros["C1"])
print(carros["C1"]["Fabricante"])
print(carros["C1"]["Modelo"])

print("Tamanho do Dictionary: " + str(len(carros)))

print("-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")

