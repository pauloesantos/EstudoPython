# Paulo Eduardo Faundes dos Santos
# Curso Python para Zumbis
# Lista de Exercício 1
# Questão 9
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro cusra R$ 60,00 por dia e R$ 0,15 por km rodado.
kmPercorridos = float(input("Qual a quantidade de km percorridos: ")) 
diasAlugado = float(input("Qual a quantidade de dias de aluguel: "))
totalPagar = (diasAlugado * 60) + (kmPercorridos * 0.15)
print("O preço a pagar pelo aluguel do carro é R$ %2.f" %totalPagar)