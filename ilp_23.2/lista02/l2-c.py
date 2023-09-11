q1: int = int(input())

vm = az = am = q1 // 3
sobra: int = q1 % 3

if sobra == 1:
    vm += 1
elif sobra == 2:
    vm += 1
    az += 1

print("Vermelho", vm)
print("Azul", az)
print("Amarelo", am)
