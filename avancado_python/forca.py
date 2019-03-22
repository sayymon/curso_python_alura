import random



def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = inicializa_palavra_secreta()

    letras_acertadas = inicializa_letras_acentuadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not acertou and not enforcou):
        print("Jogando")
        chute = input("Qual letra? ").strip()
        if chute.lower() in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    exibe_fim_jogo(acertou,palavra_secreta)

def imprime_mensagem_abertura():
    print("****************************************")
    print("***Bem vindo ao jogo da Gaby Jequiti!***")
    print("*****************************************")

def inicializa_letras_acentuadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def inicializa_palavra_secreta(nome_arquivo="palavras.txt"):
    lista_palavras = []
    with open(nome_arquivo) as arquivo:
        for linha in arquivo:
            lista_palavras.append(linha.strip())
    # print(lista_palavras)
    numero = random.randrange(0, len(lista_palavras))
    palavra_secreta = lista_palavras[numero].lower()
    return palavra_secreta


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute.lower() == letra.lower():
            print("Encontrei a letra {} na posição {}".format(letra, index))
            letras_acertadas[index] = letra

        index += 1


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

def exibe_fim_jogo(acertou,palavra_secreta):
    if (acertou):
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
    else:
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


if __name__ == "__main__" :
    jogar()