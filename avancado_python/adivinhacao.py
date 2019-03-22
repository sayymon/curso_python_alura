import random
import sys

def imprime_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    print("Qual o nivel de dificuldade ?")
    print("1  nivel facil")
    print("2  nivel medio")
    print("3  nivel dificil")

def jogar():
    imprime_mensagem_abertura()

    total_de_tentativas = definir_nivel_jogo()

    pontos = 1000

    numero_secreto = random.randrange(101)
    # print(f"Numero secreto {numero_secreto}")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número de 1 a 100: ")

        print("Você digitou ", chute_str)
        chute = int(chute_str)
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (acertou):
            print("Parabéns! Você acertou!")
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (maior):
                print("O seu chute foi maior do que o número secreto!")
            elif (menor):
                print("O seu chute foi menor do que o número secreto!")

        rodada = rodada + 1

    print(f"Fim do jogo sua pontuacao foi {pontos}")


def definir_nivel_jogo():
    nivel = int(input("Digite o nivel: "));
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5
    else:
        print("Nivel invalido")
        sys.exit()
    return total_de_tentativas


if __name__ == "__main__" :
    jogar()