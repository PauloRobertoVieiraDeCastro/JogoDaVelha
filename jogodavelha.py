import numpy as np
def layout(s,c,b): #função layout do jogo da velha
    b[0,s] = c
    print('   ','|','   ','|')
    print(b[0,0],'|',b[0,1],'|',b[0,2])
    print('___','|','___','|','___')
    print('   ','|','   ','|')
    print(b[0,3],'|',b[0,4],'|',b[0,5])
    print('___','|','___','|','___')
    print('   ','|','   ','|')
    print(b[0,6],'|',b[0,7],'|',b[0,8])
    print('   ','|','   ','|')
    return b


#funções para checar ganhador
def checkcoluna(kk): #função checar coluna para ver se alguém ganha
    if (kk[0,0] == ' X ' and kk[0,1] == ' X ' and kk[0,2] == ' X ') or (kk[1,0] == ' X ' and kk[1,1] == ' X ' and kk[1,2] == ' X ') or (kk[2,0] == ' X ' and kk[2,1] == ' X ' and kk[2,2] == ' X '):
        return 'saida'
    if (kk[0,0] == ' O ' and kk[0,1] == ' O ' and kk[0,2] == ' O ') or (kk[1,0] == ' O ' and kk[1,1] == ' O ' and kk[1,2] == ' O ') or (kk[2,0] == ' O ' and kk[2,1] == ' O ' and kk[2,2] == ' O '):
        return 'saida'

def checklinha(kk): #função checar coluna para ver se alguém ganha
    if (kk[0,0] == ' X ' and kk[1,0] == ' X ' and kk[2,0] == ' X ') or (kk[0,1] == ' X ' and kk[1,1] == ' X ' and kk[2,1] == ' X ') or (kk[0,2] == ' X ' and kk[1,2] == ' X ' and kk[2,2] == ' X '):
        return 'saida'
    if (kk[0,0] == ' O ' and kk[1,0] == ' O ' and kk[2,0] == ' O ') or (kk[0,1] == ' O ' and kk[1,1] == ' O ' and kk[2,1] == ' O ') or (kk[0,2] == ' O ' and kk[1,2] == ' O ' and kk[2,2] == ' O '):
        return 'saida'

def checkdiagonal(kk): #função checar diagonal para ver se alguém ganha
    if (kk[0,0] == ' X ' and kk[1,1] == ' X ' and kk[2,2] == ' X ') or (kk[2,0] == ' X ' and kk[1,1] == ' X ' and kk[0,2] == ' X '):
        return 'saida'
    if (kk[0,0] == ' O ' and kk[1,1] == ' O ' and kk[2,2] == ' O ') or (kk[2,0] == ' O ' and kk[1,1] == ' O ' and kk[0,2] == ' O '):
        return 'saida'
   
a = '   '
lista = []
b = np.matrix([[a,a,a,a,a,a,a,a,a]]) #vetor de vazios
bb = np.reshape(b,(3,3)) #matriz 3 x 3 como em jogo da velha
cont = 0 #contador de jogada
print('------------------------------')
print('         Jogo da Velha        ')
print('------------------------------')
while True:    
    while True:
        print('Jogador X joga')
        playerX = int(input('Qual posição inserir (De 0 até 8)? '))
        if playerX in lista:
            print('Jogada já ocorreu. Tente novamente.')
        elif playerX<0 or playerX>8:
            print('Jogada impossível. Tente novamente.')
        else:
            break
    lista.append(playerX) #acrescenta numeros para evitar jogadas repetidas
    print('')
    k = layout(playerX,' X ',b)
    kk = np.reshape(k,(3,3))
    print('')
    resultado = checkcoluna(kk) #checa se a coluna foi preenchida
    if resultado == 'saida':
        print(' X ganhou!! ')
        break
    resultado = checklinha(kk) #checa se a linha foi preenchida
    if resultado == 'saida':
        print(' X ganhou!! ')
        break
    resultado = checkdiagonal(kk) #checa se a diagonal foi preenchida
    if resultado == 'saida':
        print(' X ganhou!! ')
        break
    cont += 1
    if cont == 9:
        print('Empate !!!!') #checa empate
        break
#--------------------------------------------------------------------------------------------    
    while True:
        print('Jogador O joga')
        playerO = int(input('Qual posição inserir (De 0 até 8)? '))
        if playerO in lista:
            print('Jogada já ocorreu. Tente novamente.') #evita jogadas repetidas
        elif playerO>8 or playerO<0:
            print('Jogada impossível. Tente novamente.') #evita números diferentes de 0 até 8
        else:
            break
    lista.append(playerO) #acrescenta numeros para evitar jogadas repetidas
    print('')
    k = layout(playerO,' O ',b)
    kk = np.reshape(k,(3,3))
    print('')
    kk = np.reshape(k,(3,3)) #organizo em matriz
    resultado = checkcoluna(kk) #checa se a coluna foi preenchida
    if resultado == 'saida':
        print(' O ganhou!! ')
        break
    resultado = checklinha(kk)
    if resultado == 'saida': #checa se a linha foi preenchida
        print(' O ganhou!! ')
        break
    resultado = checkdiagonal(kk)
    if resultado == 'saida': #checa se a diagonal foi preenchida
        print(' O ganhou!! ')
        break
    cont += 1
    if cont == 9: #termina o jogo com empate
        print('Empate !!!!')
        break
