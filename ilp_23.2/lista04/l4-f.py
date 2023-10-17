num_fases = int(input())
fases = [int(n) for n in input().split()]
hp = aux = int(input())

for n in fases:
    if n == 1:
        hp = aux
    elif n != 0:
        hp -= n
        if hp <= 0:
            break

print("Yes, you can") if hp > 0 else print("You Died")
