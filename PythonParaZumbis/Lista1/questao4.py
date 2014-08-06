# Paulo Eduardo Faundes dos Santos
# Curso Python para Zumbis
# Lista de Exercício 1
# Questão 4
# Faça um programa que calcule o aumento de um salário. Ele deve Solicitar o valor do Salário e a
# porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salario = float(input("Entre com o salário: "))
porcentagem = float(input("Entre com a porcentagem de aumento: "))
aumento = salario * porcentagem / 100
novoSalario = salario + aumento
print('Aumento: R$ %.2f' %aumento)
print('Novo salário: R$ %.2f' %novoSalario)
