
#funcao e um def - jogar_forca
import random

from jogos import escolha_jogo

#Funcao para Imprime messagem de abertura
def bem_vindo():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

#Funcao de palvra secreta
def carrega_palavara_secreta():
    # ler arquivo que tem palavras e escolher aleatoriamente
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return  palavra_secreta #retorna a palvra

#separar palavras
def inicializa_letras_acertadas(palavra):
   return  ["_" for letra in palavra]


#funcao para palavra chute do jogador
def pede_chute():
    chute = input("Qual letra? ") #caputar a palavra chute
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,palavra_secreta,letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def messagem_vencedor():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

def messagem_perdedor(palavra_secreta):
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

#forca quando errar
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



# funcao de principal
def jogar_forca():
#chamadas de funcao
    bem_vindo() #funcao e messagem de bem vindo
    palavra_secreta = carrega_palavara_secreta()#funcao e para palavra secreta e carrega palavra secreta
    
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

#variaves
    enforcou = False
    acertou = False
    erros = 0

# loop de while true e false
    while (not acertou and not enforcou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute,palavra_secreta,letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas) #imprime qual e a palvra que foi escolida

    if (acertou):
        messagem_vencedor()
    else:
        messagem_perdedor(palavra_secreta)
    print("Fim de jogo")

if(__name__ == "__main__" ):
    escolha_jogo()




