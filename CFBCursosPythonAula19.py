# Aula 19 - https://youtu.be/lf7lWsQ2V38?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Funções P1

# declaração de variáveis - Escopo Global...
n1 = 10
n2 = 5

# cria a função somar...
def somar():
  r = n1 + n2 # se refere a variáveis globais
  print("Soma de " + str(n1) + " e " + str(n2) + " = " + str(r))
  print("Curso de Python - CFB Cursos")
  print("youtube.com/cfbcursos\n")

# cria a função subtrair...
def subtrair():
  r = n1 - n2 # se refere a variáveis globais
  print("Subtração de " + str(n1) + " e " + str(n2) + " = " + str(r))
  print("Curso de Python - CFB Cursos")
  print("youtube.com/cfbcursos\n")

# cria a função calcular...
def calcular():
  somar()
  subtrair()

# cria a função multiplicação...
def multiplicar():
  r = n1 * n2 # se refere a variáveis globais
  print("Multiplicação de " + str(n1) + " e " + str(n2) + " = " + str(r))


# chama a função...
print(" somar-----------------------------------------")
somar() # executa a soma...

print("subtrair-----------------------------------------")
subtrair() # executa a função...

print("calcular-----------------------------------------")
calcular() # chama as funções...

print("multiplicar-----------------------------------------")
multiplicar() # executa a função...

print("-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")
