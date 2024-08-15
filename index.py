import random
sorteio = random.randint(1,2)
humano = 'X'
computador = '\033[0;31mO\033[m'
jogador = input('Insira o seu nome: ')
tabuleiro = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
count = 0
#IMPRIMIR O TABULEIRO
def imprimir_tabuleiro(tabuleiro):
    print('\033[0;94m  1   2   3\033[m')
    print()
    for i in range(3):
        print(f'{f'\033[0;94m{i+1}\033[m'} '  f'{tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ')
        if i < 2:
            print(' ---+---+---')
#VERIFICAR SE A CASA JOGADA PELO HUMANO ESTÁ DISPONÍVEL, SE SIM, JOGAR
def checar_casa_human(tabuleiro):
    linha_human = None
    coluna_human = None
    while True:
        #linha_human = validarinputlinha()
        #coluna_human = validarinputcoluna()
        linha_human = validarinput('Escolha a linha para jogar: ')
        coluna_human = validarinput('Escolha a coluna para jogar: ')
        
   
        if not checarvalidh(linha_human, coluna_human):
            continue
        else:
            tabuleiro[linha_human][coluna_human] = 'X'
            break


def validarinput(txt):
    while True:
        jogada_human = int(input('Escolha a ' + txt + ' para jogar: ') ) - 1
        if jogada_human > 2 or jogada_human < 0:
            print(txt.capitalize() + ' está inválida')
        else:
            break
    return jogada_human

# #CHECAR SE A COLUNA ESCOLHIDA PELO HUMANO ESTÁ VALIDA NO TABULEIRO
# def validarinputcoluna():
#     while True:
#         coluna_human = int(input('Escolha a coluna para jogar: ') ) - 1
#         if coluna_human > 2 or coluna_human < 0:
#             print('Coluna invalida')
#         else:
#             break
#     return coluna_human
# #CHECAR SE A LINHA ESCOLHIDA PELO HUMANO ESTÁ VÁLIDA NO TABULEIRO
# def validarinputlinha():
#     while True:
#         linha_human = int(input('Escolha a linha para jogar: ') ) - 1 
#         if linha_human > 2 or linha_human < 0:
#             print('Linha inválida')
#         else: 
#             break
#     return linha_human

#CHECAR SE A CASA JOGADA PELO HUMANO ESTÁ DISPONÍVEL
def checarvalidh(linha_human, coluna_human):
    if tabuleiro[linha_human][coluna_human] == ' ':
        return True
    else: 
        print('Casa inválida')
        return False
#CHECAR A LINHA E A COLUNA QUE O COMPUTADOR ESCOLHEU E FAZER A SUA JOGADA
def checar_casa_computador(tabuleiro):
    while True:
        linha_comp = random.randint(0,2)
        coluna_comp = random.randint(0,2)
        if tabuleiro[linha_comp][coluna_comp] == ' ':
            tabuleiro[linha_comp][coluna_comp] = computador
            print(f'O computador jogou na casa de linha {linha_comp+1} e coluna {coluna_comp+1}')
        else: 
            print(f'A casa de linha {linha_comp} e coluna {coluna_comp} escolhida pelo computador já está ocupada, ele irá jogar novamente!.')
            checar_casa_computador(tabuleiro=tabuleiro)
        break
#FUNÇÕES PARA VERIFICAR UM GANHADOR 
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
            print(f'\033[0;32mO computador ganhou \033[m')
            return vencedor
def verificar_diagonal():
    vencedor = ' '
    if tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[2][2] == tabuleiro[0][0] and tabuleiro[0][0] != ' ':
        vencedor = tabuleiro[0][0]
        if vencedor == 'X':
            print(f'\033[0;32mO jogador {jogador} ganhou \033[m')
            return vencedor
        if vencedor == computador:
            print(f'\033[0;32mO computador ganhou  \033[m')
            return vencedor

    if tabuleiro[2][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[0][2] and tabuleiro[0][2] == tabuleiro[2][0] and tabuleiro[2][0] != ' ':
        vencedor = tabuleiro[2][0]
        if vencedor == 'X':
            print(f'\033[0;32mO jogador {jogador} ganhou \033[m')
            return vencedor
        if vencedor == computador:
            print(f'\033[0;32mO computador ganhou \033[m')
            return vencedor

# AVISAR AO PLAYER QUEM INICIOU A PARTIDA
if sorteio == 1:
    print('O computador começou jogando')
if sorteio == 2:
    print(f'O jogador {jogador} começou o jogo')

def main():
    jogadas = 0
    placar_O = 0
    placar_X = 0
    while True:
        imprimir_tabuleiro(tabuleiro=tabuleiro)
        print(' ')
        print('=*' * 40)
        print(' ')
#COMPUTADOR COMEÇA
        if sorteio == 1:
            
            checar_casa_computador(tabuleiro=tabuleiro)
            jogadas += 1
            if verificar_horizontal() == computador or verificar_vertical() == computador or verificar_diagonal() == computador:
    
                imprimir_tabuleiro(tabuleiro=tabuleiro)
                break
            imprimir_tabuleiro(tabuleiro=tabuleiro)
            print('=*' * 40)
            print(' ')

            #DEFINIR QUANDO SERÁ EMPATE
            if jogadas > 8:
                print('Deu velha :( )')
                break
            checar_casa_human(tabuleiro=tabuleiro)
            jogadas += 1
            if verificar_horizontal() == 'X' or verificar_vertical() == 'X' or verificar_diagonal() == 'X':
               
                imprimir_tabuleiro(tabuleiro=tabuleiro)
                break
#HUMANO COMEÇA
        elif sorteio == 2:
            
            checar_casa_human(tabuleiro=tabuleiro)
            jogadas += 1
            if verificar_horizontal() == 'X' or verificar_vertical() == 'X' or verificar_diagonal() == 'X':    
                imprimir_tabuleiro(tabuleiro=tabuleiro)
                break
            print('=*' * 40)
            print(' ')
            imprimir_tabuleiro(tabuleiro=tabuleiro)
            print('=*' * 40)
            print(' ')
            #DEFINIR QUANDO SERÁ EMPATE
            if jogadas > 8:
                print('Deu velha :()')
                break
            checar_casa_computador(tabuleiro=tabuleiro)
            jogadas += 1
            if verificar_horizontal() == computador or verificar_vertical() == computador or verificar_diagonal() == computador:
                imprimir_tabuleiro(tabuleiro=tabuleiro)
                break  
main()