# Aula 25 - https://youtu.be/cN4esJ0DhqI?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# POO - Herança / P3
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
#
# Herança
# Herança é uma classe que herda outra classe...
# Cria a classe PAI, depois cria as classes filhos que vão herdar da classe PAI.
# Todas as características da classe PAI são herdadas pelas clases filhas...
# 

# criação da classe NPC...
class NPC: # Base, Pai, Super
  # Construtor
  def __init__(self, nome, time, forca, municao):
    self.nome = nome
    self.time = time
    self.forca = forca
    self.municao = municao
    self.vivo = True
    self.energia = 100
  # Informações
  def info(self):
    print("Nome....: " + self.nome)
    print("Time....: " + str(self.time))
    print("Força...: " + str(self.forca))
    print("Munição.: " + str(self.municao))
    print("Vivo....: " + (self.vivo and "SIM" or "NÃO"))
    print("Energia.: " + str(self.energia))
    print("\n--------------------------------------------")
# FIM CLASSE NPC

# Classe Soldado - Herada de NPC
class Soldado(NPC):
  # Construtor
  # Irá sobrescrever o construtor da classe pai (herdada)
  def __init__(self, nome, time):
    self.forca = 200
    self.municao = 200
    super().__init__(nome, time, self.forca, self.municao)
# FIM CLASSE SOLDADO
 
# Classe Guarda - Herada de NPC
class Guarda(NPC):
  # Construtor
  # Irá sobrescrever o construtor da classe pai (herdada)
  def __init__(self, nome, time):
    self.forca = 100
    self.municao = 20
    super().__init__(nome, time, self.forca, self.municao)
# FIM CLASSE GUARDA
 
# Classe Elite - Herada de NPC
class Elite(NPC):
  # Construtor
  # Irá sobrescrever o construtor da classe pai (herdada)
  def __init__(self, nome, time):
    self.forca = 400
    self.municao = 500
    super().__init__(nome, time, self.forca, self.municao)
  # Informações da classe herdada
  def inf(self):
    super().info()
# FIM CLASSE ELITE

# Instânciar os Objetos
s1 = Guarda("Olho Vivo", 1)
s2 = Soldado("Bala na Agulha", 1)
s3 = Elite("Ninja", 1)
s4 = Guarda("Super Atento", 2)
s5 = Soldado("Tiro Certo", 2)
s6 = Elite("Samurai", 2)

# Chama métodos 
s1.vivo = False
s6.vivo = False

# Informações
s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf()
