# Paulo Eduardo Faundes dos Santos
# Curso Python para Zumbis
# Lista de Exercício 1
# Questão 3
# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = int(input("Entre com os dias: "))
horas = int(input("Entre com as horas: "))
minutos = int(input("Entre com os minutos: "))
segundos = int(input("Entre com os segundos: "))
total = ((dias * 24 * 60 * 60) + horas * 60 * 60) + minutos * 60) + segundos)
print(" %i dias, %i horas, %i minutos e %i segundos são %i segundos no total" % (dias, horas, minutos, segundos, total))
