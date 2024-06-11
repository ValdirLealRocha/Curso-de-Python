# Aula 12 - https://youtu.be/tAELiaxFbdY?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Curso de Python #12

# declaração de vaiáveil
carros = ["HRV", "Golf", "Argo", "Focus"] # Coleção

# imprimir elemento por elemento
for x in carros:
  print(x)
  if( x == "Golf"):
    print("  VW")

print("\n-----------------------------------------\n")

# string em Python é indexada e cada letra é um elemento...
for x in "CFB Cursos":
  print(x)

print("\n-----------------------------------------\n")

# usar a lista diretamente no for...
for x in ["HRV", "Golf", "Argo", "Focus"]:
  print(x)
  if( x == "Golf"):
    print("  VW")

print("\n-----------------------------------------\n")

# usar break...
carros = ["HRV", "Golf", "Argo", "Focus", "Fit", "Fusion", "Polo"]
for x in carros:
  print(x)
  if( x == "Fit"):
    print("  HONDA")
    break # encerra looping... para a leitura da lista...

print("\n-----------------------------------------")
print("\nFIM DO PROGRAMA\n\n")

