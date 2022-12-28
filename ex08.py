print("**************************")
print("***Jogo da adivinhação***")
print("**************************")

rodada = 1
total_de_tentativas = 5
numero_secreto = 51

while(rodada <= total_de_tentativas):
    escolha = int(input("Escolha um número inteiro "))
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    if (escolha == numero_secreto):
        print("Você acertou!")
    else:
        if (escolha > numero_secreto):
            print("Você errou! O número secreto é menor")
        if (escolha < numero_secreto):
            print("Você errou! O núermo secreto é maior")

    rodada = rodada + 1

    if (rodada > 5):
        print("Acabou suas tentivas... :(")

print("Fim de jogo")
            
    

    