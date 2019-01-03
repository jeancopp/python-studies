import random

FACIL   = 1
NORMAL  = 2
DIFICIL = 3

def nivel():
    print("Entre com o nível do jogo:")
    print(f"{FACIL} - Fácil", f"{NORMAL} - Normal", f"{DIFICIL} - Difícil", sep="\n")
    numero = int(input("Escolha:"))
    return numero

def tentativas(nivel):
    if nivel == FACIL:
        return 20
    elif nivel == NORMAL:
        return 10
    else:
        return 5

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    nivel_escolhido = nivel()
    total_tentativas = tentativas(nivel_escolhido)
    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    for rodada in range(1, total_tentativas + 1):
        print( "Rodada {} de {}".format(rodada, total_tentativas) )
        chute = int(input("Entre com um numero entre 1 e 100:"))

        if(chute < 1 or chute > 100):
            print("Número inválido!")
            continue;

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print(f"Você acertou! Pontuacao: {pontos}")
            break
        else:
            print("Você errou!", end="")
            if(maior):
                print("Voce entrou com um numero maior")
            elif(menor):
                print("Voce entrou com um numero menor")

            pontos -= abs(numero_secreto - chute)


    print("Fim de jogo")

if(__name__=="__main__" ):
    jogar()
