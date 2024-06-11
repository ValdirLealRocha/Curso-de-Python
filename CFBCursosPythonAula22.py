# Aula 22 - https://youtu.be/t7wjLDQNVJg?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Funções Lamda ou Funções Anônimas

# declaração de função lambda...
soma = lambda a, b: (a + b) # dois argumentos...

print("\n1 -----------------------------------------")
# chama a função lambda
r = soma(2, 5)
print(r)
print(soma(20, 50))

print("\n2 -----------------------------------------")
# declaração de função lambda...
mult = lambda a, b, c: (a + b) * c # com 3 argumentos...
# chama a função lambda
r = mult(2, 5, 5)
print(r)
print(mult(20, 50, 3))

print("\n3 -----------------------------------------")
# declaração de função lambda...
# chama a função lambda
print((lambda a, b: (a + b)) (3, 2)) # lambda direto sem armazenar em variáveis...

print("\n4 -----------------------------------------")
# declaração de função lambda...
# chama a função lambda
r = lambda x, func: x + func(x) # lambda passando função como argumento...
print(r(2, lambda x: x * x)) # x * x
print(r(2, lambda x: x + x)) # x + x
print(r(2, lambda x: x + 3)) # x + 3

print("\n-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")

