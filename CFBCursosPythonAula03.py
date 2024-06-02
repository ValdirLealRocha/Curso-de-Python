# Aula 03 - https://youtu.be/_p4dPzetzpE?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Variáveis em Python
num = num2 = res = 0

#canal = "CFB Cursos" # escopo global 

def cn():
  # após eu defini a variavel global ela será vista globalmente...
  global canal # depois add global pra aacessar globalmente
  canal = "CFB Cursos" # escopo somente dentro da função cn()
  print(canal)

cn() ## executa pra mostrar a variavel canal

print(canal) # mostra o conteúdo da variavel global, deu erro quando comentei...
