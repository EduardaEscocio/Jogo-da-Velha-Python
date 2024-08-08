import random
sorteio = random.randint(1,2)
humano = 'X'
computador = '\033[0;31mO\033[m'

tabuleiro = [[0,0,0], [0,0,0], [0,0,0]]

def imprimir_tabuleiro(tabuleiro):
    
    for i in range(3):
        print(f' {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ')
        if i < 2:
            print('---+---+---')

def checar_casa_human(tabuleiro):
    while True:
        linha_human = int(input('Escolha a linha para jogar: '))
        
        coluna_human = int(input('Escolha a coluna para jogar: '))
        if tabuleiro[linha_human][coluna_human] == 0:
            tabuleiro[linha_human][coluna_human] = 'X'

        else:
            print(f'A casa de linha: {linha_human} e coluna: {coluna_human} está ocupada, escolha outra')
        break

def checar_casa_comp(tabuleiro):
    while True:
        linha_comp = random.randint(0,2)
        coluna_comp = random.randint(0,2)
        if tabuleiro[linha_comp][coluna_comp] == 0:
            tabuleiro[linha_comp][coluna_comp] = computador
        break
      

while True:
    imprimir_tabuleiro(tabuleiro=tabuleiro)
    print(' ')
    print('=*' * 40)
    print(' ')
    if sorteio == 1:
        checar_casa_comp(tabuleiro=tabuleiro)
        print('=*' * 40)
        print(' ')

        imprimir_tabuleiro(tabuleiro=tabuleiro)
        print('=*' * 40)
        print(' ')

        checar_casa_human(tabuleiro=tabuleiro)

    elif sorteio == 2:
        checar_casa_human(tabuleiro=tabuleiro)
        print('=*' * 40)
        print(' ')

        imprimir_tabuleiro(tabuleiro=tabuleiro)
        print('=*' * 40)
        print(' ')

        checar_casa_comp(tabuleiro=tabuleiro)

# def escolher_jog(sorteio):
#     if sorteio == 1:
#         checar_casa_comp()
#     else:
#         checar_casa_human()
