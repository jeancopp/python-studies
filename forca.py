
def exibir(palavra):
    print(palavra)

def jogar():
    print("********************************")
    print("    Bem vindo ao jogo de força  ")
    print("********************************")

    palavra_secreta = "banana"
    acertou=False
    enforcou=False



    while(not acertou and not enforcou):
        chute = input("Entre com seu chute:").strip()[0];
        indice = 0
        for letra in palavra_secreta.upper():
            if(letra == chute.upper()):
                print(f"Encontrei a letras {letra} na posicao {indice}")
            indice+=1


    print("Fim do jogo")


if( __name__ == '__main__' ):
    jogar();
