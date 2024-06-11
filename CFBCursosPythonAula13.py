# Aula 13 - https://youtu.be/4RdiUs2xoGg?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Função Input

# possibilita usar comandos no ternimal
import os

# declaração de vaiáveil
os.system('cls')
nome = input("\nDigite seu nome: ")
print("\nNome Digitado: " + nome)
print("\n-----------------------------------------")

os.system('cls')
num1 = int(input("Digite o primeiro valor..: "))
num2 = int(input("Digite o segundo valor...: "))
res = num1 + num2 # converter pois no padrão fica string...
print("Soma dos Valores: " + str(res))

print("\n-----------------------------------------")
print("\nFIM DO PROGRAMA!\n")

