# Aula 26 - https://youtu.be/jT-C3OjUBvQ?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Try Except / tratamento de erros

# Abaixo utilizei indicar os comandos na linha do print, assim entendo o que ocorreu
# em cada linha de execção, mas é lógico que o debug é o melhor... :)

print("---------------------------------------")
# valida erro x não declarado...
try:
  print(x)
except: # valida erro desconhecido
  print("except: Erro!")

print("---------------------------------------")
# valida erro x não declarado...
try:
  print(x)
except NameError: # valida erro conhecido...
  print("except NameError: X não definido!")
except: # valida erro desconhecido
    print("except: Erro desconhecido!")

print("---------------------------------------")
# valida erro x não declarado...
try:
  print(x)
except NameError: # valida erro conhecido...
  print("except NameError: Erro no programa!")
else: # caso não gera erro/excessão no except executa o que está em else...
    print("else: Tudo certo..")

print("---------------------------------------")
# validação com o x inicializado...
x1 = 10
try:
  print(x1)
except NameError: # valida erro conhecido...
  print("except NameError: Erro no programa!")
else: # caso não gera erro/excessão no except executa o que está em else...
    print("else: Tudo certo..")

print("---------------------------------------")
# validação com o x inicializado...
x2 = 10
try:
  print(x2)
except NameError: # valida erro conhecido...
  print("except NameError: Erro no programa!")
else: # caso não gera erro/excessão no except executa o que está em else...
    print("else: Tudo certo..")
finally: # independnte se ocorreu ou não o erro, executa tudo dentro de finally...
    print("finally: Fim do Tratamento...")

print("---------------------------------------")
# validação sem o x inicializado...
try:
  print(x3)
except NameError: # valida erro conhecido...
  print("except NameError: Erro no programa!")
else: # caso não gera erro/excessão no except executa o que está em else...
    print("else: Tudo certo..")
finally: # independnte se ocorreu ou não o erro, executa tudo dentro de finally...
    print("finally: Fim do Tratamento...")

print("---------------------------------------")
# validação num negativo...
num =- 10
if num < 1:
  # gera um exception...
  #raise Exception("num =- 10 if num < 1: Valor não permitido!")
  print("raise Exception(num =- 10 if num < 1: Valor não permitido!)")

print("---------------------------------------")
# validação num positivo...
num = 10
if num < 1:
  # gera um exception...
  #raise Exception("num = 10 if num < 1: Valor não permitido!")
  print("raise Exception(num = 10 if num < 1: Valor não permitido!)")

print("---------------------------------------")
# validação num string...
num = ""
if type(num) is int:
  # gera um exception...
  #raise Exception("num = '' if type(num) is int: Valor não permitido!")
  print("raise Exception(num = '' if type(num) is int: Valor não permitido!)")

print("---------------------------------------")
# validação num string...
num = 10
if type(num) is int:
  # gera um exception...
  raise Exception("num = '' if type(num) is int: Somente números permitido!")
  try:
    print("Normal...")
  except: # valida erro conhecido...
    print("raise Exception...")
else:
  print(str(num))
  print("num = '' if type(num) is int: else: num!")

print("---------------------------------------")
#
