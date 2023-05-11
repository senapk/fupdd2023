import random


segredo = random.randint(1, 99)
                    
minimo = 0
maximo = 100
print("segredo: " + str(segredo))

while True:
    print("Chute entre ]" + str(minimo) + ", " + str(maximo) + "[")
    chute = random.randint(minimo + 1, maximo - 1)
    print("chutei: " + str(chute))
    input()
    
    if segredo < chute:
        print("Eh menor")
        maximo = chute
    if segredo > chute:
        print("Eh maior")
        minimo = chute
    if segredo == chute:
        print("chutadora ganhou")
        break
    if maximo - minimo == 2:
        print("O numero era " + str(segredo))
        print("chutadora perdeu")
        break