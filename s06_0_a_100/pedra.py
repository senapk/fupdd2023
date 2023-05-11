import random
    
# entrada:  "R", "S", "P"
# saida : "empate", "jog1", "jog2"
def quem_ganhou(jog1, jog2):
    if jog1 == jog2:
        return "empate"
    if  (jog1 == "S" and jog2 == "P") or \
        (jog1 == "P" and jog2 == "R") or \
        (jog1 == "R" and jog2 == "S"):
        return "jog1"
    return "jog2"

def maquina_escolhe():
    maq_num = random.randint(1, 3)
    maq = ""
    if   maq_num == 1:
        maq = "S"
    elif maq_num == 2:
        maq = "P"
    else:
        maq = "R"
    return maq

def usuario_escolhe():
    print("Escolha (Paper / Scissors / Rock): ", end = "")
    user = input()
    return user

def mostrar_resultado(ganhador):
    if ganhador == "empate":
        print("Voces empataram")
    elif ganhador == "jog1":
        print("Maquina ganhou")
    else:
        print("Voce ganhou")

def main():
    maq = maquina_escolhe()
    user = usuario_escolhe()
    print("Maquina escolheu: " + maq)
    ganhador = quem_ganhou(maq, user)
    mostrar_resultado(ganhador)

main()