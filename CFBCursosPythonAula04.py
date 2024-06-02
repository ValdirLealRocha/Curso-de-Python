# Aula 04 - https://youtu.be/FgB-uFuFcwo?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Tipos de dados em Python
x = 1 # int
x = "CFB Cursos" # string
x = 15.6 # float
x = False # booblean

# a variavel se define pela última especificação de valor...
print("Valor: " + str(x)) # mostra o conteúdo de x
print("Tipo.: " + str(type(x))) # mostra o tipo da variável

# array no Paython chama de list
x = ["Carro", "Avião", "Navio"] # list/array
print("Variável Valor: " + str(x[0])) # mostra o conteúdo de x
print("Tipo.: " + str(type(x))) # mostra o tipo da variável

# List / Array - cada posição pode ser editada/alterada
x = ["Carro", "Avião", "Navio", 1, 58.3, True] # list/array com vários tipos e sem erro...
print("Array Valor: " + str(x[5])) # mostra o conteúdo de x
print("Tipo.: " + str(type(x))) # mostra o tipo da variável

# A Tupla não pode ser modificada...
x = ("Carro", "Avião", "Navio", 1, 58.3, True) # Tuplas com vários tipos e sem erro...
print("Tupla Valor: " + str(x[3])) # mostra o conteúdo de x
print("Tipo.: " + str(type(x))) # mostra o tipo da variável

x = range(0, 100, 1) # inicializa a lista de 0 a 100 de 1 em 1
print("Range Valor: " + str(x[98])) # mostra o conteúdo de x
print("Tipo.: " + str(type(x))) # mostra o tipo da variável

x = {
  "canal" : "CFB Cursos",
  "curso" : "Curso de Python",
  "nome" : "Bruno",
} # Dictionary
print("Dicionário: " + x["curso"]) # mostra o conteúdo de x
print("Tipo.: " + str(type(x))) # mostra o tipo da variável

x = {5, 7, 4, 5, 7, 4, 8} # Set
print("set: " + str(x)) # mostra o conteúdo de x
print("Tipo.: " + str(type(x))) # mostra o tipo da variável

x = frozenset({5, 7, 4, 5, 7, 4, 8}) # Set
print("set: " + str(x)) # mostra o conteúdo de x
print("Tipo.: " + str(type(x))) # mostra o tipo da variável

n1 =5; n2 = 2; x = complex(n1, n2) # tipo complex
n1 =5; n2 = 2; x = complex(1j) # tipo complex
print(x.real) # parte real
print(x.imag) # parte imaginária

