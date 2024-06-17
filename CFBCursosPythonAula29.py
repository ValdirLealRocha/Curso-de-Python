# PRIMEIRA PARTE...
# Aula 29 - https://youtu.be/FuuYavr-Bu8?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Iterators - percorre valores de uma coleção...
# Interators é um objeto que implementa dois métodos:
# iter - contrutor
# next - passa para o próximo elemento de uma coleção

# imprime na tela
print("--------------------")
print("Lista de Carros-----")

# coleção de carros...
carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion"]

# for percorre coleções...
for c in carros:
  print(c) # lista todos os carros - 5

# imprime na tela
print("--------------------")
print("Lista com Iterator--")

# cria um iterator
itCarros = iter(carros)

# percorre a coleção... um a um...
print(next(itCarros)) # 0 - 1
print(next(itCarros)) # 1 - 2
print(next(itCarros)) # 2 - 3
print(next(itCarros)) # 3 - 4
print(next(itCarros)) # 4 - 5
#print(next(itCarros)) # aqui gera uma exceção pois ultrapassou a qtde da coleção...

# imprime na tela
print("--------------------")
print("while lista coleção-")
i = 0
while i < 5:
  print(carros[i])
  i += 1

# imprime na tela
print("--------------------")
print("while com iterator--")
# coleção de carros...
carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion", "Golf", "Focus", "Onyx", "Fit"]
# cria um iterator
itCarros = iter(carros)
# da forma apresentado abaixo, não precisa controlar o tamanho da coleção...
while itCarros:
  try:
    print(next(itCarros))
  except StopIteration:
    print("Fim da impressão da coleção de Carros!")
    break

# imprime na tela
print("--------------------")
print("Programa Finalizado!")
print("--------------------")
