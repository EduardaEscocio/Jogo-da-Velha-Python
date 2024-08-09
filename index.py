import random
sorteio = random.randint(1,2)
humano = 'X'
computador = '\033[0;31mO\033[m'
jogador = input('Insira o seu nome: ')
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
            checar_casa_human(tabuleiro=tabuleiro)
        break

def checar_casa_comp(tabuleiro):
    while True:
        linha_comp = random.randint(0,2)
        coluna_comp = random.randint(0,2)
        if tabuleiro[linha_comp][coluna_comp] == 0:
            tabuleiro[linha_comp][coluna_comp] = computador
        else: 
            print(f'A casa de linha {linha_comp} e coluna {coluna_comp} escolhida pelo computador já está ocupada, ele irá jogar novamente!.')
            checar_casa_comp(tabuleiro=tabuleiro)
        break
      
def verificar_vertical():
    for i in range(2):
        if tabuleiro[0][i] == 'X' and tabuleiro[1][i] == 'X' and tabuleiro[2][i] == 'X':
            print(f'\033[0;32mO jogador {jogador} ganhou 1 \033[m')
            return True
        elif tabuleiro[0][i] == computador and tabuleiro[1][i] == computador and tabuleiro[2][i] == computador:
            print(f'\033[0;32mO computador ganhou 1\033[m')
            return True
    return False
def verificar_horizontal():
    for i in range(2):
        if tabuleiro[i][0] == 'X' and tabuleiro[i][1] == 'X' and tabuleiro[i][2] == 'X':
            print(f'\033[0;32mO jogador {jogador} ganhou \033[m')
            return True
        if tabuleiro[i][0] == computador and tabuleiro[i][1] == computador and tabuleiro[i][2] == computador:
            print(f'\033[0;32mO computador ganhou 2\033[m')
            return True
    return False

def verificar_diagonal():
        if tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == 'X':
            print(f'\033[0;32mO jogador {jogador} ganhou \033[m')
            return True
        if tabuleiro[0][0] == computador and tabuleiro[1][1] == computador and tabuleiro[2][2] == computador:
            print(f'\033[0;32mO computador ganhou 2\033[m')
            return True
        if tabuleiro[2][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[0][2] == 'X':
            print(f'\033[0;32mO jogador {jogador} ganhou \033[m')
            return True
        if tabuleiro[2][0] == computador and tabuleiro[1][1] == computador and tabuleiro[0][2] == computador:
            print(f'\033[0;32mO computador ganhou 2\033[m')
            return True
        return False
while True:
    imprimir_tabuleiro(tabuleiro=tabuleiro)
    print(' ')
    print('=*' * 40)
    print(' ')
    if sorteio == 1:
        checar_casa_comp(tabuleiro=tabuleiro)
        # verificar_vertical()
        # verificar_horizontal()
        print('=*' * 40)
        print(' ')

        imprimir_tabuleiro(tabuleiro=tabuleiro)
        print('=*' * 40)
        print(' ')

        checar_casa_human(tabuleiro=tabuleiro)
        # verificar_vertical()
        # verificar_horizontal()

    elif sorteio == 2:
        checar_casa_human(tabuleiro=tabuleiro)
        # verificar_vertical()
        # verificar_horizontal()

        print('=*' * 40)
        print(' ')

        imprimir_tabuleiro(tabuleiro=tabuleiro)
        print('=*' * 40)
        print(' ')

        checar_casa_comp(tabuleiro=tabuleiro)
        # verificar_vertical()
        # verificar_horizontal()
    if verificar_horizontal() == True or verificar_vertical() == True or verificar_diagonal() == True:
        imprimir_tabuleiro(tabuleiro=tabuleiro)
        break
# def escolher_jog(sorteio):
#     if sorteio == 1:
#         checar_casa_comp()
#     else:
#         checar_casa_human()
