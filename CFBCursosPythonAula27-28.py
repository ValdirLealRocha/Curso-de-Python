# PRIMEIRA PARTE...
# Aula 27 - https://youtu.be/Gw7hgDe6m34?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Exercício Prático 1 / Parte 1

# SEGUNDA PARTE...
# Aula 28 - https://youtu.be/czCpjtzqDGY?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Exercício Prático 1 / Parte 2

import os # utilização do cls limpoar a tela...

# lista de carros vazia
carros = []

# criar um objeto da classe carros, e cada objeto vai ficar dentro 
# desta lista carros...
# uma forma de gerenciar objetos dentro de listas... dentre outras formas...
# Classe Carro
class Carro:
  # declaração das propriedades da classe
  nome = ""
  potencia = 0
  velocidademaxima = 0
  ligado = False

  # método construtor
  def __init__(self, nome, potencia): # os parametros vem como any...
    self.nome = nome
    self.potencia = potencia
    self.velocidademaxima = int(potencia) * 2
    self.ligado = False
  
  # método ligado
  def ligar(self):
    self.ligado = True
  
  # método ligado
  def desligar(self):
    self.ligado = False
  
  # método de informações
  def info(self):
    print("Nome..............: " + self.nome)
    print("Potência..........: " + str(self.potencia))
    print("Velocidade Máxima.: " + str(self.velocidademaxima))
    print("Ligado............: " + (self.ligado and "SIM" or "NÃO"))
# FIM DA CLASSE CARRO ################################################

# Menu
def Menu():
  # limpar tela
  os.system("cls") or None # or None previne erro do sistema operacional...
  # definir as opções do menu...
  print("1 - Novo Carro")
  print("2 - Informações do Carro")
  print("3 - Excluir o Carro")
  print("4 - Ligar o Carro")
  print("5 - Desligar o Carro")
  print("6 - Listar o(s) Carro(s)")
  print("7 - Sair")
  print("Quantidade de Carros: " + str(len(carros)))
  # captura a opção selecionada...
  opc = input("Digite uma opção: ")
  # retorno da opcção...
  return opc

# Criar novo carro
def novoCarro():
  # limpar tela
  os.system("cls") or None # or None previne erro do sistema operacional...
  # captura a opção selecionada...
  n = input("Nome do carro.....: ")
  p = input("Potência do carro.: ")
  # cria o carro na lista...
  car = Carro(n, p)
  carros.append(car)
  print("Novo Carro criado!")
  # ponto deparada no sistema...
  os.system("pause")

# Informações do Carro...
def informacoes():
  # limpar tela
  os.system("cls") or None # or None previne erro do sistema operacional...
  # captura a opção selecionada...
  n = input("Informe o número do carro que deseja ter as informações.: ")
  try: # valida e trata erro se houver...
    carros[int(n)].info()
  except:
    print("Carro não existe na lista!")
  # ponto deparada no sistema...
  os.system("pause")

# Excluir carro
def excluirCarro():
  # limpar tela
  os.system("cls") or None # or None previne erro do sistema operacional...
  # captura a opção selecionada...
  n = input("Informe o número do carro que deseja excluir.: ")
  try: # valida e trata erro se houver...
    del carros[int(n)]
  except:
    print("Carro não existe na lista!")
  # ponto deparada no sistema...
  os.system("pause")

# Ligar carro
def ligarCarro():
  # limpar tela
  os.system("cls") or None # or None previne erro do sistema operacional...
  # captura a opção selecionada...
  n = input("Informe o número do carro que deseja ligar.: ")
  try: # valida e trata erro se houver...
    carros[int(n)].ligar()
    print("Carro número " + str(n) + " ligado!")
  except:
    print("Carro não existe na lista!")
  # ponto deparada no sistema...
  os.system("pause")

# Desligar carro
def desligarCarro():
  # limpar tela
  os.system("cls") or None # or None previne erro do sistema operacional...
  # captura a opção selecionada...
  n = input("Informe o número do carro que deseja desligar.: ")
  try: # valida e trata erro se houver...
    carros[int(n)].desligar()
    print("Carro número " + str(n) + " desligado!")
  except:
    print("Carro não existe na lista!")
  # ponto deparada no sistema...
  os.system("pause")

# Listar carro
def listarCarro():
  # limpar tela
  os.system("cls") or None # or None previne erro do sistema operacional...
  # varrer a lista e mostrar todos os carros...
  p = 0
  for c in carros:
    print(str(p) + " - " + c.nome)
    #p = p + 1
    p += 1
  # ponto deparada no sistema...
  os.system("pause")

# Tratar o retorno de Menu()
ret = Menu()
# laço para manter a execução do programa enquanto o usuário teclar 7-Sair...
while ret < "7":
  if ret == "1":
    novoCarro()
  elif ret == "2":
    informacoes()
  elif ret == "3":
    excluirCarro()
  elif ret == "4":
    ligarCarro()
  elif ret == "5":
    desligarCarro()
  elif ret == "6":
    listarCarro()
  # chama Menu()
  ret = Menu()

# limpar tela
os.system("cls") or None # or None previne erro do sistema operacional...
#
print("--------------------")
print("Programa Finalizado!")