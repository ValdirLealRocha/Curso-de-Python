# Aula 24 - https://youtu.be/Oa-E3JM3BHo?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# POO - Classes / P2 / Construtor e métodos
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
  # Método construtor...
  def __init__(self, v, l, c):
    # self equivale ao this...
    self.velMax = v
    self.ligado = l
    self.cor = c
  # Método mostrar...
  def mostrar(self):
    print("\n-----------------------------------------")
    print("Velocidade Máxima.: " + str(self.velMax))
    print("Cor...............: " + self.cor)
    print("Ligado............: " + (self.ligado and "SIM" or "NÃO")) # validação if
    print("Ligado............: " + ("SIM" if self.ligado else "NÃO")) # validação ternária
  # Método ligado...
  def ligar(self):
    self.ligado = True
  # Método desligar...
  def desligar(self):
    self.ligado = False
  # Método andar...
  def andar(self):
    print("\n-----------------------------------------")
    if(self.ligado):
      print("Andando")
    else:
      print("Carro Desligado!")

# intânciar o objeto da classe Carro...
c1 = Carro(200, False, "Preto")
c2 = Carro(120, False, "Branco")
c3 = Carro(350, False, "Vermelho")
# COMENTAR, pois acima na aula anterior não havia o método construtor...
# definir os valores das propriedades...
#c1.velMax = 200 # defini velocidade máxima pro C1
#c1.cor = "Preto" # define a cor
#c1.ligado = False # define se o carr estará ligado...

c1.ligar() # Ligar carro 1
c2.ligar() # Ligar carro 2
#c3.ligar() # Ligar carro 3

c1.mostrar()
c1.andar() # andar com o Carro 1
c2.mostrar()
c2.andar() # andar com o Carro 2
c3.mostrar()
c3.andar() # andar com o Carro 3
# COMENTAR, pois não havia um método mostrar na classe...
#print("\n-----------------------------------------")
# mostrar dados na tela...
#print("Carro 1")
#print("Velocidade Máxima.: " + str(c1.velMax))
#print("Cor...............: " + c1.cor)
#print("Ligado............: " + (c1.ligado and "SIM" or "NÃO")) # validação if
#print("Ligado............: " + ("SIM" if c1.ligado else "NÃO")) # validação ternária

# c1.andar() # andar com o Carro 1
# c2.andar() # andar com o Carro 2
# c3.andar() # andar com o Carro 3

print("\n==========================================")
print("\nFIM DO PROGRAMA!\n")
