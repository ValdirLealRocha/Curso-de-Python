# Aula 09 - https://youtu.be/N7zOb-wB0xI?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Coleção List - []

# declaração de variáveis
carros = ["HRV", "Golf", "Argo", "Focus"]
print(carros)
print(carros[0]) # mostra o primeiro indice da lista
print(carros[-1]) # mostra o último indice da lista

# altera um elemento da lista
carros[3] = "Fusion"
print(carros)

# adiciona um item a lista
carros.append("Fit")
carros.append("Focus")
carros.append("Polo")
print(carros)

# tamanho da lista
print(str(len(carros)) + " carros na lista")

# remover item da lista
carros.remove("Fusion")
print(str(len(carros)) + " carros na lista")

# remover último item da lista
carros.pop()
print(str(len(carros)) + " carros na lista")
print(carros)

# limpa um item especifico
del carros[2]
print(str(len(carros)) + " carros na lista")
print(carros)

# limpa toda a lista
carros.clear()
print(str(len(carros)) + " carros na lista")
print(carros)

# Copiar / Clona a lista carros em carros2
carros = ['HRV', 'Golf', 'Argo', 'Fusion', 'Fit', 'Focus', 'Polo']
carros2 = list(carros)
print(str(len(carros)) + " carros na lista")
print("Carros    " + str(carros))
print("Carros 2: " + str(carros2))

# Juntar as listas
print("\n")
print("-------------------------------------------------------------------------")
carros2 = ['Fusca', 'Fiat 147', 'Brasilia', 'Celta']
carros3 = carros + carros2 # juntar carros e carros e em carros3
print("Carros    " + str(carros))
print(str(len(carros)) + " carros na lista")
print("-------------------------------------------------------------------------")
print("Carros 2: " + str(carros2))
print(str(len(carros2)) + " carros na lista")
print("-------------------------------------------------------------------------")
print("Carros 3: " + str(carros3))
print(str(len(carros3)) + " carros na lista")
print("-------------------------------------------------------------------------")
print("\n")
