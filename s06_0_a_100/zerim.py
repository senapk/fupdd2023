


# op: "par" ou "impar"
# num sao um numero inteiro
# saida: "jog1", "jog2"
def par_ou_impar(op1, num1, num2):
    if (op1 == "par" and (num1 + num2) % 2 == 0) or \
       (op1 == "impar" and (num1 + num2) % 2 == 1):
        return "jog1"
    return "jog2"

def zerim(jog1, jog2, jog3):
    if jog1 == jog2 and jog2 == jog3:
        return "empate"
    if jog2 == jog3:
        return "jog1"
    if jog1 == jog3:
        return "jog2"
    return "jog3"

jog1 = input()
jog2 = input()
jog3 = input()

print(zerim(jog1, jog2, jog3))
