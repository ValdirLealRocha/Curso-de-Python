# Aula 02 - https://youtu.be/5JdEoBZYHFY?list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR
# Sintaxe básica P2 e Comentários
# Na aula de hoje do curso de Python vamos aprender como instalar e 
# preparar o ambiente para desenvolvimento e criar nosso primeiro 
# programa em Python.
# Python é uma linguagem de programação que permite trabalhar 
# rapidamente e integrar sistemas de forma mais eficaz.
# Python não é uma linguagem compilada e sim interpretada, 
# também não é fortemente tipada o que o torna uma linguagem 
# de fácil aprendizado e rápida produtividade.
# Não é tipada e pode mudar no decorrer da vida da variável
"""
três aspas duplas comenta uma sequencia de linha e o # uma linha inteira
num = 1
num = "Bruno"
num = 1.5
"""

num1=num2=res=0 # forma de inicializar variáveis na mesma linha...

# fim de linha de comando ;
# não dá erro dois comandos na mesma linha
canal = "CFB Cursos"; curso = " - " + "Curso de Python"
print(canal + curso)

# exemplo de identação e recuo para agrupar os comandos de execução do bloco.
# inicio e fim do bloco de condição do if, o recue deve ser igual.
if 10 < 2:
  print("Maior")
  print("aula 1")
  
  print("aula 2")
print("FIM")
