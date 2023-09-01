q1: int = int(input())

vm = az = am = 0

incremento_vm: int = q1 // 3
incremento_az: int = q1 // 3
incremento_am: int = q1 // 3

sobra: int = q1 % 3
if sobra == 1:
    incremento_vm += 1
elif sobra == 2:
    incremento_vm += 1
    incremento_az += 1

vm += incremento_vm
az += incremento_az
am += incremento_am

print("Vermelho", vm)
print("Azul", az)
print("Amarelo", am)
