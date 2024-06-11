# Aula 21 - https://youtu.be/ZSXrLnQ8s0E?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Funções P3 / Retorno de valores

valores = [1, 5, 3, 2, 10, 4, 8]

# define a função que irá somar e retoinar a somatória em r
def somar(num):
  r = 0
  for n in num:
    r += n
  return r

# converter que retorna inteiro...
print(str(valores) + ": soma = " + str(somar(valores)))

print("-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")

