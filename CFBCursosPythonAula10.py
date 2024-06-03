# Aula 10 - https://youtu.be/EY505u2h_VQ?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Como usar o comando IF em Python

# declaração de vaiáveil
a = True

# Estrutura de condição lógica, usa os operadores de comparação verdadeiro ou falso
if a: # avalia se está vazio sim ou não, se verdadeiro mostra a mensagem
  print('1 - CFB Cursos - condição verdadeira pois a variável \'a\' não está vazia')
  
# Estrutura de condição lógica, usa os operadores de comparação verdadeiro ou falso
a = 10
b = 5
if (a > b): # valida a comparação
  print('2 - CFB Cursos - mostrou a mensagem pois \'a\' é maior que \'b\'')

if (a < b): # valida a comparação
  print('3 - CFB Cursos - não vai mostrar a mensagem pois \'a\' é menor que \'b\'')

# op = '+' # retorna verdadeiro no if
# res = 0
# if (op == '+'): # valida a comparação '==' compara igualdade
#   res = a + b
#   print('4 - Operação (a' + op + 'b) : res = ' + str(res))

#
# Preste atenção aos recuos, é o que define o que está dentro da estrutura do IF...
#

#
# Conforme vou alterando o operador e cada bloco de IF faz a avaliação certinho pra cada operação.
#

#
# Observe que vamos usar só o IF e não o esle...
#

op = '+' # soma
res = 0
if (op == '+'): # valida a comparação '==' compara igualdade
  res = a + b
print('5 - Operação (a' + op + 'b) : res = ' + str(res))

op = '-' # subtrai
if (op == '-'): # valida a comparação '==' compara igualdade
  res = a - b
print('6 - Operação (a' + op + 'b) : res = ' + str(res))

op = '*' # multiplica
if (op == '*'): # valida a comparação '==' compara igualdade
  res = a * b
print('7 - Operação (a' + op + 'b) : res = ' + str(res))

op = '/' # divide
if (op == '/'): # valida a comparação '==' compara igualdade
  res = a / b
print('8 - Operação (a' + op + 'b) : res = ' + str(res))

print('Fim do programa')