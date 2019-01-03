import adivinhacao
import forca

ADIVINHACAO = 1
FORCA = 2

if __name__ == '__main__':

    print("*************************")
    print("****Escolha seu jogo ****")
    print("*************************")

    print(" 1 - Adivinhacao ")
    print(" 2 - Forca")
    escolha = int(input("Entre com sua opção:"))

    if (escolha == ADIVINHACAO):
        adivinhacao.jogar()
    elif (escolha == FORCA):
        forca.jogar()
