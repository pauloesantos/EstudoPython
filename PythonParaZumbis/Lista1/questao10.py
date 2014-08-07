# Paulo Eduardo Faundes dos Santos
# Curso Python para Zumbis
# Lista de Exercício 1
# Questão 10
# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
# quantidade de cigarros fumados por dia e quantos anos ele fumou. Considere que um fumante
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá.
# Exiba o total de dias.

'''
   Fazendo uma regra de três chegamos que 144 cigarros tiram 1 dia
   de vida da pessoa (1 dia = 1440 minutos = 144 cigarros)
'''
cigarros = int(input("Qual a quantidade de cigarros por dia: "))
anos = int(input("Quantos anos fumando: "))
total_cigarros = anos * 365 * cigarros
dias_perdidos = total_cigarros / 144
print ("Você perdeu aproximadamente %.2f dias de vida" %dias_perdidos)