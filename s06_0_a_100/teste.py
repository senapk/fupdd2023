import random

segredo = random.randint(1, 99)
menor = 0
maior = 100
while True:
    print("Escolha um valor ]" + str(menor) + ", " + str(maior) + "[")
    chute = random.randint(menor + 1, maior - 1)
    print("escolhi: " + str(chute))
    input()
    if  segredo > chute:
        print("eh maior")
        menor = chute
    elif segredo < chute:
        print("eh menor")
        maior = chute
    else:
        print("acertou")
        break

    if maior - menor == 2:
        print("voce perdeu")
        break
