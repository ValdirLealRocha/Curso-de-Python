# Aula 11 - https://youtu.be/bIJK6f4ygGo?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Condicional If Elif Else

# declaração de vaiáveil
a = 10
b = 5
res = 0
op = '+' 
#
# Preste atenção aos recuos, é o que define o que está dentro da estrutura do IF...
# Conforme vou alterando o operador e cada bloco de IF faz a avaliação certinho pra cada operação.
# Observe que nesta aula 11 vamos usar o IF e o ELSE... 
# Ajuda a organizar melhor o bloco de condição...
# Neste exemplo fica um único bloco e ajuda a ficar mais rápido no processamento...
op = '+' 
if (op == '+'): # soma
  res = a + b
elif (op == '-'): # subtrai
  res = a - b
elif (op == '*'): # multiplica
  res = a * b
elif (op == '/'): # divide
  res = a / b
else:
  print('Operador inválido')

print('Operação (a' + op + 'b) : res = ' + str(res))

# como estamos em aula, criei aqui as variaveis, mas o legal é sempre no topo
clima = 'sol'
lugar = ''

# uma condição lógica
if clima == 'sol':
  lugar = 'clube'
else:
  lugar = 'cinema'

print('Vou ao ' + lugar)

dinheiro = 500
# mais condição lógica
if (clima == 'sol') and (dinheiro > 300):
  lugar = 'clube'
  print('Vou ao ' + lugar + ' tem SOL!')
else:
  lugar = 'cinema'
  print('Vou ao ' + lugar + ' está CHOVENDO!')

clima = 'chuva'
if (clima == 'sol') and (dinheiro > 300):
  lugar = 'clube'
  print('Vou ao ' + lugar + ' tem SOL e estou com DINHEIRO!')
else:
  lugar = 'cinema'
  print('Vou ao ' + lugar + ' está CHOVENDO! e estou sem grana.')

dinheiro = 200
clima = 'sol'
if (clima == 'sol') and (dinheiro >= 300 and dinheiro <= 500):
  lugar = 'clube'
  print('Vou ao ' + lugar + ' tem SOL e estou com DINHEIRO!')
else:
  lugar = 'cinema'
  print('Vou ao ' + lugar + ' está CHOVENDO! e estou sem grana.')

# operado AND - todas as condições devem ser verdadeiras para validar a operação
# and
# V V = V
# V F = F
# F V = F
# F F + F
dinheiro = 300
clima = 'sol'
if (clima == 'sol') and (dinheiro >= 300 and dinheiro <= 500):
  lugar = 'clube'
  print('Vou ao ' + lugar + ' tem SOL e estou com DINHEIRO!')
else:
  lugar = 'cinema'
  print('Vou ao ' + lugar + ' está CHOVENDO! e estou sem grana.')

# operador OR - uma das condições deve ser verdadeira para validar a operação
# or
# V V = V
# V F = V
# F V = V
# F F + F
dinheiro = 650
clima = 'sol'
if (clima == 'sol') or (dinheiro >= 300 and dinheiro <= 500):
  lugar = 'clube'
  print('Vou ao ' + lugar + ' tem SOL e estou com DINHEIRO!')
else:
  lugar = 'cinema'
  print('Vou ao ' + lugar + ' está CHOVENDO! e estou sem grana.')

print('\nFim do programa\n')
