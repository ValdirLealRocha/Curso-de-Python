# Aula 07 - https://youtu.be/1Wq5QSdLAKE?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Strings P2

# declaração de variáveis
texto = "Curso de Python"
palavra = "python"

curso = "Curso de Python"
canal = "CFB Cursos"

# procura parte da string
res = palavra in texto # está contido
print(res)
res = palavra not in texto # não está contido
print(res)
res = palavra.upper() in texto.upper() # está contido em maiusculas
print(res)

# concatenação de strings e variáveis
res = "Curso: " + curso + " do Canal " + canal
print(res)

# string de data
cidade = "Belo Horizonte"
dia = 15
mes = "Dezembro"
ano = 2019

# concatenação de strings e variáveis
print(cidade + ", " + str(dia) + " de " + mes + " de " + str(ano))

# concatenação de strings e variáveis - com formatação - Place Holders - Parametros
data = "{}, {} de {} de {}"
print(data.format(cidade, dia, mes, ano))

# caracteres de escape, imprimir caracteres especiais e teclas... pula linha...
data = "{}, {} de {} de {}\n{}"
print(data.format(cidade, dia, mes, ano, canal))

# \' - aspas simples
# \" - aspas duplas
# \n - quebra linha
# \r - quebra linha
# \t - tabulação
# \b - BackSpace
data = "{}, {} de {} de {}\n\"{}\""
print(data.format(cidade, dia, mes, ano, canal))
