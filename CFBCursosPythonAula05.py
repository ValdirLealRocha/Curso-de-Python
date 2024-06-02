# Aula 05 - https://youtu.be/Vsrhr5bh5u0?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Tipos numéricos, random e operações de casting

# importar bilbioteca
import random

# declaração de variáveis e inicialização
num_i = 10
num_f = 5.2
num_c = 1j

# mostra conteúdo das variáveis
x = num_i
print("\nValor: " + str(x) + " - Tipo: " + str(type(x)) + "\n")

# mostra conteúdo das variáveis
x = num_f
print("\nValor: " + str(x) + " - Tipo: " + str(type(x)) + "\n")

# mostra conteúdo das variáveis
x = num_c
print("\nValor: " + str(x) + " - Tipo: " + str(type(x)) + "\n")

# mostra conteúdo das variáveis
x = int(num_f) # casting / conversão de tipos, perde a decimal...
print("\nValor: " + str(x) + " - Tipo: " + str(type(x)) + "\n")

# mostra conteúdo das variáveis
x = float(num_i) # casting / conversão de tipos, perde a decimal...
print("\nValor: " + str(x) + " - Tipo: " + str(type(x)) + "\n")

# mostra conteúdo das variáveis
num_r = random.randrange(0, 59)
x = num_r # casting / conversão de tipos, perde a decimal...
print("\nValor: " + str(x) + " - Tipo: " + str(type(x)) + "\n")

# mostra conteúdo das variáveis
num_r = [
  random.randrange(0, 59),
  random.randrange(0, 59),
  random.randrange(0, 59),
  random.randrange(0, 59),
  random.randrange(0, 59),
  random.randrange(0, 59),
  ]
x = num_r # casting / conversão de tipos, perde a decimal...
print("\nValor 1: " + str(x[0]) + " - Tipo: " + str(type(x)) + "")
print("Valor 2: " + str(x[1]) + " - Tipo: " + str(type(x)) + "")
print("Valor 3: " + str(x[2]) + " - Tipo: " + str(type(x)) + "")
print("Valor 4: " + str(x[3]) + " - Tipo: " + str(type(x)) + "")
print("Valor 5: " + str(x[4]) + " - Tipo: " + str(type(x)) + "")
print("Valor 6: " + str(x[5]) + " - Tipo: " + str(type(x)) + "\n")
