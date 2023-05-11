import random

print("Escolha um número e tecle enter")
input()

menor = 0
maior = 100
while True:
    chute = random.randint(menor + 1, maior - 1)
    print("Escolhi um valor ]" + str(menor) + ", " + str(maior) + "[    : " + str(chute))
    print("(1) Eh menor? (2) Eh maior? (3) Acertou :", end = "")
    resp = input()

    if resp == "1":
        maior = chute
    if resp == "2":
        menor = chute
    if resp == "3":
        print("eu ganhei")
        break
    if maior - menor <= 2:
        print("eu perdi")
        break
