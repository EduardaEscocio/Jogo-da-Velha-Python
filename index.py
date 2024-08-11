import random
sorteio = random.randint(1,2)
humano = 'X'
computador = '\033[0;31mO\033[m'
jogador = input('Insira o seu nome: ')
tabuleiro = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
placar_X = 0
placar_O = 0

def verificar_vertical():
    vencedor = ' '
    for i in range(2):
        if tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] == tabuleiro[2][i] and tabuleiro[0][i] != ' ':
            vencedor = tabuleiro[0][i]
        if vencedor == 'X':
            print(f'\033[0;32mO jogador {jogador} ganhou \033[m')
            return vencedor
        if vencedor == computador:
            print(f'\033[0;32mO computador ganhou \033[m')
            return vencedor
def verificar_horizontal():
    vencedor = ' '
    for i in range(2):
        if tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][2] == tabuleiro[i][0] and tabuleiro[i][0] != ' ':    
            vencedor = tabuleiro[i][0]
        if vencedor == 'X':
            print(f'\033[0;32mO jogador {jogador} ganhou \033[m')
            return vencedor
                
        if vencedor == computador:
            print(f'\033[0;32mO computador ganhou 3 \033[m')
            return vencedor
    

def verificar_diagonal():
    vencedor = ' '
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[2][2] == tabuleiro[0][0] and tabuleiro[0][0] != ' ':
        vencedor = tabuleiro[0][0]
        if vencedor == 'X':
            print(f'\033[0;32mO jogador {jogador} ganhou \033[m')
            return vencedor
            
        if vencedor == computador:
            print(f'\033[0;32mO computador ganhou 2 \033[m')
            return vencedor
    if tabuleiro[2][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[0][2] and tabuleiro[0][2] == tabuleiro[2][0] and tabuleiro[2][0] != ' ':

        vencedor = tabuleiro[2][0]
        if vencedor == 'X':
            print(f'\033[0;32mO jogador {jogador} ganhou \033[m')
            return vencedor
        if vencedor == computador:
            print(f'\033[0;32mO computador ganhou 1 \033[m')
            return vencedor
    
    
def imprimir_tabuleiro(tabuleiro):
    print('\033[0;94m  0   1   2\033[m')
    print()
    for i in range(3):
        print(f'{f'\033[0;94m{i}\033[m'} '  f'{tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ')
        if i < 2:
            print(' ---+---+---')

def checar_casa_human(tabuleiro):
    while True:
        linha_human = int(input('Escolha a linha para jogar: '))
        if linha_human > 2:
            
        coluna_human = int(input('Escolha a coluna para jogar: '))
        if tabuleiro[linha_human][coluna_human] == ' ':
            tabuleiro[linha_human][coluna_human] = 'X'
        
        else:
            print(f'A casa de linha: {linha_human} e coluna: {coluna_human} está ocupada, escolha outra')
            checar_casa_human(tabuleiro=tabuleiro)
        break

def checar_casa_comp(tabuleiro):
    while True:
        linha_comp = random.randint(0,2)
        coluna_comp = random.randint(0,2)
        if tabuleiro[linha_comp][coluna_comp] == ' ':
            tabuleiro[linha_comp][coluna_comp] = computador
            print(f'O computador jogou na casa de linha {linha_comp} e coluna {coluna_comp}')
        else: 
            print(f'A casa de linha {linha_comp} e coluna {coluna_comp} escolhida pelo computador já está ocupada, ele irá jogar novamente!.')
            checar_casa_comp(tabuleiro=tabuleiro)
        break

# def placar():
    # if verificar_diagonal() == True or verificar_horizontal() == True or verificar_vertical() == True:
        

# AVISAR AO PLAYER QUEM INICIOU A PARTIDA
if sorteio == 1:
    print('O computador começou jogando')
if sorteio == 2:
    print(f'O jogador {jogador} começou o jogo')

while True:
    imprimir_tabuleiro(tabuleiro=tabuleiro)
    print(' ')
    print('=*' * 40)
    print(' ')
    if sorteio == 1:
        
        checar_casa_comp(tabuleiro=tabuleiro)
        
        # verificar_vertical()
        # verificar_horizontal()
   
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
    if verificar_horizontal() == 'X' or verificar_vertical() == 'X' or verificar_diagonal() == 'X':
        placar_X += 1
        print(f'Jogador: {placar_X} Computador: {placar_O}')
        imprimir_tabuleiro(tabuleiro=tabuleiro)
        print('Obrigada por jogar!')
        break
    if verificar_horizontal() == computador or verificar_vertical() == computador or verificar_diagonal() == computador:
        placar_O += 1
        print(f'Jogador: {placar_X} Computador: {placar_O}')
        imprimir_tabuleiro(tabuleiro=tabuleiro)
        break
# def escolher_jog(sorteio):
#     if sorteio == 1:
#         checar_casa_comp()
#     else:
#         checar_casa_human()