# Paulo Eduardo Faundes dos Santos
# Curso Python para Zumbis
# Lista de Exercício 1
# Questão 5
# Solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar
mercadoria = float(input("Entre com o valor da mercadoria: "))
porcentagem = float(input("Entre com a porcentagem de desconto: "))
desconto = mercadoria * porcentagem / 100
novoPreco = mercadoria - desconto
print('Desconto: R$ %.2f' %desconto)
print('Novo preço: R$ %.2f' %novoPreco)