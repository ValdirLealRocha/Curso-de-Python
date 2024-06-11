# Aula 20 - https://youtu.be/eXUNdKVnUjU?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Funções P2 / argumentos de entrada

# declaração de variáveis - Escopo Global...

# cria a função somar... Com parametros...
def somar(n1, n2):
  r = n1 + n2 # se refere a variáveis globais
  print("Soma de " + str(n1) + " e " + str(n2) + " = " + str(r))
  print("youtube.com/cfbcursos\n")

# chama a função...
print("1 -----------------------------------------")
somar(5, 7) # executa a soma... Informa os valores...

print("2 -----------------------------------------")
somar(12, 8) # executa a soma... Informa os valores...

print("3 -----------------------------------------")
somar(1, 2) # executa a soma... Informa os valores...

print("4 -----------------------------------------")
# Função com argumentos arbitrarios - n argumanetos/oparamentros, 
# e preparar a função pra trarar
# pega os parametros e mostra todos na tela na sequencia...
def textos(*txt):
  for t in txt:
    print(t)

# recebe 5 argumentos...
textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")
print("5 -----------------------------------------")
# recebe 2 argumentos...
textos("CFB Cursos", "Python")

# cria a função somar... Com n parametros arbitrarios...
def somar1(*num):
  r = 0
  for n in num: # varre os parametros e soma...
    r += n
  print("Somar1 = " + str(r))
  print("youtube.com/cfbcursos\n")

# chama a função...
print("6 -----------------------------------------")
somar1(5, 2, 3, 5, 20, 15, 0, 1, 37) # executa a soma... Informa os valores...

print("7 -----------------------------------------")
# Função com argumentos arbitrarios - n argumanetos/oparamentros, 
# e preparar a função pra trarar
# pega os parametros e mostra todos na tela na sequencia...
def carros(c = "Golf"):
  print("Modelo: " + c)

# imprime ne tela...
carros()
carros("HRV")

# cria a função somar... Passando uma lista/tupla como parametros arbitrarios...
valores1 = (1, 5, 3, 2) # tuple
valores2 = {1, 5, 3, 2} # set que não sei o que é - mas funcionou...
valores3 = [1, 5, 3, 2] # list
def somar2(num):
  r = 0
  for n in num: # varre os parametros e soma...
    r += n
  print("Somar2 = " + str(r))

# chama a função...
print("8 -----------------------------------------")
somar2(valores1) # executa a soma...
somar2(valores2) # executa a soma...
somar2(valores3) # executa a soma...

print("-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")

