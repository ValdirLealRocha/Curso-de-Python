# Aula 06 - https://youtu.be/DUZoz0HuuCU?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Strings P1

curso = " Curso de Python "

# acessando um indice de uma stringum campo string
print(curso[9]) # posição 9 = P
print(curso[0:5]) # posição inicial 0 pega 4 caracteres = Curso
print(curso[9:15]) # posição inicial 0 pega 4 caracteres = Python
print("Tamanho: " + str(len(curso))) # tamanho da string
print("Curso: " + curso) # msotra com espaços
print("Curso: " + curso.strip()) # mostra SEM espaços
print("Curso: " + curso.lower()) # caixa baixa
print("Curso: " + curso.lower().strip()) # caixa baixa SEM espaços
print("Curso: " + curso.upper()) # caixa baixa
print("Curso: " + curso.upper().strip()) # caixa baixa SEM espaços
curso = "Curso de Python"
print("Curso: " + curso.replace("Python", "C#")) # troca parte da string
curso = "Curso de Python"
a = curso.split(" ") # quebra string e cria um list
print("Curso: " + a[2]) # mostra o indice da lista
