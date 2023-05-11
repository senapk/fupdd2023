import random
                     
minimo = 0
maximo = 100
# print("segredo: " + str(segredo))

print("Escolha um numero e digite enter")
input()

while True:
    print("Chute entre ]" + str(minimo) + ", " + str(maximo) + "[")
    chute = random.randint(minimo + 1, maximo - 1)
    print("Chutei:" + str(chute))
    print("(1) eh menor, (2) eh maior, (3) acertei:")
    resp = input()

    if resp == "1":
        maximo = chute
    if resp == "2":
        minimo = chute
    if resp == "3":
        print("Maquina ganhou")
        break

    if maximo - minimo == 2:
        print("Jogador ganhou")
        break