# Paulo Eduardo Faundes dos Santos
# Curso Python para Zumbis
# Lista de Exercício 1
# Questão 6
# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer
# e a velocidade média esperada para a viagem
distancia = float(input("Qual a distância a ser percorria em Km: "))
velocidade = float(input("Qual a velocidade média em km/h: "))
tempo = distancia / velocidade
print("Tempo aproximado em horas: %1.f" %tempo)