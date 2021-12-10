import forca
import adivinhacao

def escolha_jogo():
    print("*********************************")
    print("****Escolha seu jogo ****")
    print("*********************************")


    print("(1)Forca (2) Adivinhacao")

    jogos = int(input("Qual e o jogo ? "))

    if(jogos == 1):
        print("jogo da Forca")
        forca.jogar_forca() #funcao
    elif(jogos == 2):
        print("jogo da Adivinhacao")
        adivinhacao.jogar_adivinhacao() #funcao

#roda os outros arquivos - modulos
if(__name__ == "__main__"):
    escolha_jogo()
