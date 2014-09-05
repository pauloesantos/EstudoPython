from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Vamos jogar Batalha Naval!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Tudo a partir daqui deve ir dentro do laco!
# Tenha certeza de recuar quatro espacos!
for turn in range(4):
    guess_row = int(raw_input("Adivinhe a Linha:"))
    guess_col = int(raw_input("Adivinhe a Coluna:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Parabens, voce afundou meu couracado!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, isso nao e nem mesmo no oceano."
        elif(board[guess_row][guess_col] == "X"):
            print "Voce ja tentou esse."
        else:
            print "Voce errou meu couracado!"
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print "Game Over"
        # Exiba aqui (turn + 1)!
        print "Turn: %s" % (turn + 1)
        print_board(board)

"""Créditos Extras
Você também pode incrementar seu programa Batalha Naval para torná-lo mais complexo e divertido de jogar. Eis algumas ideias de melhorias — talvez você possa pensar em mais algumas!

Tenha diversos couraçados: você precisará ter cuidado porque precisa garantir que não vai colocar couraçados um em cima do outro no tabuleiro. Você também quer garantir que vai equilibrar o tamanho do tabuleiro e o número de navios para que o jogo ainda seja desafiador de divertido de jogar.

Crie navios de tamanhos diverente: isso é mais complicado do que parece. Todas as partes do navio devem estar ligadas horizontal e verticalmente, e você precisa garantir que não vai colocar parte de um navio fora dos limites do tabuleiro.

torne seu jogo um jogo para duas pessoas.

Use funções para permitir que seu jogo tenha mais recursos, como desempates, estatísticas, e outras!

Algumas dessas opções serão mais fáceis depois que abordarmos os laços na próxima lição. Pense em voltar à Batalha Naval depois de mais algumas lições e ver que mudanças você pode fazer!"""    