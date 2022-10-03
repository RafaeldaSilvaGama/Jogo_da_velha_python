import random
import sys


matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
pontoJogador1 = 0
pontoJogador2 = 0
pontoMaquina = 0
vitoria = "n"

def inicializarTabuleiro():     
    global matriz
    matriz = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return matriz


def imprimirTabuleiro():
    print("    0   1   2")
    print("0:  " + matriz[0][0] + " | " + matriz[0][1] + " | " + matriz[0][2])
    print("   -----------")
    print("1:  " + matriz[1][0] + " | " + matriz[1][1] + " | " + matriz[1][2])
    print("   -----------")
    print("2:  " + matriz[2][0] + " | " + matriz[2][1] + " | " + matriz[2][2])


def imprimirMenuPrincipal():
    escolha = int(input("Modo de jogo: \n(1)Jogador vs Jogador \n(2)Jogador vs Máquina(Fácil) \n(3)Jogador vs Máquina(Díficil) \n(4)Sair\n"))
    if escolha == 4:
        print('Encerrando programa.')
        print('Obrigado por jogar com a gente! :)')
        sys.exit(0)
    return escolha
    
def modoJogador(escolha):
        global pontoJogador1
        global pontoJogador2
        totalJogadas = 10
        jogadas = 2 
        while jogadas <= totalJogadas:
            if((totalJogadas - jogadas)%2 == 0):
                print("Jogador 1")
                jogador = 1
                print(f'Jogada..: {jogadas - 1}')
                imprimirTabuleiro()
                jogadaUsuario(jogador)
                vitoria = verificaVencedor()
                if vitoria == "s":
                    imprimirTabuleiro()
                    print('Jogador 1 Venceu')
                    pontoJogador1 += 1
                    jogadas = 10
                jogadas += 1
                if jogadas == 10:
                    verificaVelha(vitoria)
            else:
                print("Jogador 2")
                jogador = 2
                print(f'Jogada..: {jogadas - 1}')
                imprimirTabuleiro()
                jogadaUsuario(jogador)
                vitoria = verificaVencedor()
                if vitoria == "s":
                    imprimirTabuleiro()
                    print('Jogador 2 Venceu')
                    pontoJogador2 += 1
                    jogadas = 10
                jogadas += 1
                if jogadas == 10:
                    verificaVelha(vitoria)   
        imprimirPontuação()
            

def leiaCoordenadadaLinha():
    l = int(input("Escolha a linha..: "))
    return l


def leiaCoordenadadaColuna():
    c = int(input("Escolha a coluna..: "))
    return c

def imprimirPontuação():
    print("Placar..:")
    print(f'Jogador 1..: {pontoJogador1}')
    print(f'Jogador 2..: {pontoJogador2}')
    print(f'CPU........: {pontoMaquina}')

def posicaoValida(l, c):

    if matriz[l][c] == " ":
        return True
    else: 
        print("Posição inválida")
        return False
    
def verificaVencedor():
    if matriz[0][0] == "X" and matriz[0][1]  == "X" and matriz[0][2] == "X" or matriz[0][0] == "O" and matriz[0][1]  == "O" and matriz[0][2] == "O":
        vitoria = "s"
    elif matriz[1][0] == "X" and matriz[1][1]  == "X" and matriz[1][2] == "X" or matriz[1][0] == "O" and matriz[1][1]  == "O" and matriz[1][2] == "O":
        vitoria = "s"
    elif matriz[2][0] == "X" and matriz[2][1]  == "X" and matriz[2][2] == "X" or matriz[2][0] == "O" and matriz[2][1]  == "O" and matriz[2][2] == "O":
        vitoria = "s"
    elif matriz[0][0] == "X" and matriz[1][1]  == "X" and matriz[2][2] == "X" or matriz[0][0] == "O" and matriz[1][1]  == "O" and matriz[2][2] == "O":
        vitoria = "s"
    elif matriz[2][0] == "X" and matriz[1][1]  == "X" and matriz[0][2] == "X" or matriz[2][0] == "O" and matriz[1][1]  == "O" and matriz[0][2] == "O":
        vitoria = "s"
    elif matriz[0][0] == "X" and matriz[1][0]  == "X" and matriz[2][0] == "X" or matriz[0][0] == "O" and matriz[1][0]  == "O" and matriz[2][0] == "O":
        vitoria = "s"
    elif matriz[0][1] == "X" and matriz[1][1]  == "X" and matriz[2][1] == "X" or matriz[0][1] == "O" and matriz[1][1]  == "O" and matriz[2][1] == "O":
        vitoria = "s"
    elif matriz[0][2] == "X" and matriz[1][2]  == "X" and matriz[2][2] == "X" or matriz[0][2] == "O" and matriz[1][2]  == "O" and matriz[2][2] == "O":
        vitoria = "s"
    else:
        vitoria = "n"
    return vitoria



def verificaVelha(vitoria):
    if vitoria == "n":
        print("Velha")


def jogar(l, c, jogador):
    if jogador == 1:
      matriz[l][c] = "X"
    else:
      matriz[l][c] = "O"
     
   

def jogadaUsuario(jogador):
    posVal = False
    while  posVal == False:

     l = leiaCoordenadadaLinha()
     c = leiaCoordenadadaColuna()
     posVal = posicaoValida(l, c)
     if posVal == True:
        jogar(l, c, jogador)


def modoFacil(escolha):
    global pontoJogador1
    global pontoMaquina
    totalJogadas = 10
    jogadas = 2 
    while jogadas <= totalJogadas:
        if((totalJogadas - jogadas)%2 == 0):
            print("Jogador")
            jogador = 1
            print(f'Jogada..: {jogadas - 1}')
            imprimirTabuleiro()
            jogadaUsuario(jogador)
            vitoria = verificaVencedor()
            if vitoria == "s":
                imprimirTabuleiro()
                print('Jogador 1 Venceu')
                pontoJogador1 += 1
                jogadas = 10
            jogadas += 1
            if jogadas == 10:
                verificaVelha(vitoria)
        else:
            print("CPU")
            jogador = 2
            print(f'Jogada..: {jogadas - 1}')
            imprimirTabuleiro()
            jogadaMaquinaFacil(jogador)
            vitoria = verificaVencedor()
            if vitoria == "s":
                imprimirTabuleiro()
                print('CPU Venceu')
                pontoMaquina += 1
                jogadas = 10
            jogadas += 1
            if jogadas == 10:
                verificaVelha(vitoria)   
    imprimirPontuação()
# def modoDificil():

def jogadaMaquinaFacil(jogador):
    posVal = False
    while  posVal == False:
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        posVal = posicaoValida(l, c)
        if posVal == True:
           jogar(l, c, jogador)

# def jogadaMaquinaDificil():

def funcaoPrincipal():
    while True:
        inicializarTabuleiro()
        escolha = imprimirMenuPrincipal()
        if escolha == 1:
            modoJogador(escolha)
        elif escolha == 2:
            modoFacil(escolha)

    

#MAIN
while True:
    funcaoPrincipal()


