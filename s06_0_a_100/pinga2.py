import random

segredo = random.randint(1, 99)
                     
minimo = 0
maximo = 100
# print("segredo: " + str(segredo))

while True:
    while True:
        print("Chute entre ]" + str(minimo) + ", " + str(maximo) + "[")
        chute = int(input())
        if chute > minimo and chute < maximo:
            break
    
    if segredo < chute:
        print("Eh menor")
        maximo = chute
    if segredo > chute:
        print("Eh maior")
        minimo = chute
    if segredo == chute:
        print("Voce ganhou")
        break
    if maximo - minimo == 2:
        print("O numero era " + str(segredo))
        print("Maquina ganhou")
        break