# Aula 08 - https://youtu.be/yGXpyEpNSe0?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Tipo Boolean

# declaração de variáveis
aula = True
print(aula)

# condição...
aula = 10 < 15
print(aula)

aula = "CFB Cursos"
print(aula)

# string convertido para Boolean, string vazias retornan FALSE
print(bool(aula))

# um exemplo de estrutura condicional... verifica se aula tem string
if aula:
  print("Possui texto")
else:
  print("Vazio")

# qualquer valor diferente de zero é verdadeiro, caso seja zero será falso
# se vazio = false
# se não vazio igual a true
# verificar strings e expressões...
aula = 1
print(bool(aula))
