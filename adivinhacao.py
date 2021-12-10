import random




def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    #condicao e defincao de variavens
    numero_secreto = random.randrange(1,101)  #gerecao de numero secreto
    total_de_tentativas = 3
    pontos = 1000

    print("Qual e o nivel de dificuldade ?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Defina um nivel: "))

    #Codicao e nivel de dificuldade do jogo
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5



    #for para entra na condicao e numero
    for rodada in range(1 , total_de_tentativas +1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas)) #server para da o format nas 2 variaveis

        chute_str = input("Digite o seu número: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str) #convertendo o string para int


        if(chute < 1 or chute > 100):
            print("voce deve conttinuar entre 1 e 100")
            continue

        #condicionais de acerto, maior e menor - condicional
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        # chamada dos pontos ue foram  perdidos - condicional
        pontos_perdidos = abs(numero_secreto - chute) #abs - ou seja abreveacao
        pontos = pontos - pontos_perdidos


        if(acertou):
            print("Parabéns! Você acertou!" .format(pontos))
            break #parar a execucao do programa
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
        rodada = rodada + 1

    print("Fim do jogo")

