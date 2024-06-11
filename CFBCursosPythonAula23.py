# Aula 23 - https://youtu.be/AvS6MNwX3lU?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# POO - Classes / P1
#
# Classes e objetos...
# --------------------
# O que é uma classe?
# É a especificação de um objeto, ela vaio ser o desenho o conjunto de regras
# de um determinado objeto, por sua vez o objeto é uma instância da classe, 
# é quando eu intâncio um objeto daquela classe e posso utilizar este objeto 
# dentro do nosso programa, que é o resultado da classe, pois a gente entende 
# uma classe como um projeto, certo, é como sendo a planta de uma casa, e a casa
# é uma classe instânciada, um objeto daquela planta, pronto pra gente poder 
# utilizar. Em Python é muito simples, não tem tantas regras do convencional.

# criação da classe Carro...
class Carro:
  # definição das propriedades
  velMax = 0
  ligado = False
  cor = ""

## intânciar o objeto da classe Carro...
c1 = Carro()
c2 = Carro()
c3 = Carro()

# definir os valores das propriedades...
c1.velMax = 200 # defini velocidade máxima pro C1
c1.cor = "Preto" # define a cor
c1.ligado = False # define se o carr estará ligado...

# mostrar dados na tela...
print("Velocidade Máxima.: " + str(c1.velMax))
print("Cor...............: " + c1.cor)
print("Ligado............: " + (c1.ligado and "SIM" or "NÃO")) # validação if
print("Ligado............: " + ("SIM" if c1.ligado else "NÃO")) # validação ternária

print("\n-----------------------------------------")

# mostrar dados na tela... 
# c2 não foi inicializado, logo assumiu o padrão nos valores...
print("Velocidade Máxima.: " + str(c2.velMax))
print("Cor...............: " + c2.cor)
print("Ligado............: " + (c2.ligado and "SIM" or "NÃO")) # validação if
print("Ligado............: " + ("SIM" if c2.ligado else "NÃO")) # validação ternária

print("\n-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")

