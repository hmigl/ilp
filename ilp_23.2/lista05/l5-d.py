TAM = int(input())
plant = [[int(n) for n in input().split()] for _ in range(TAM)]
h, r = map(int, input().split())

fica_com_ron = (TAM - r) <= (TAM - h)

total_harry = total_ron = 0

for j in range(TAM):
    if (h, j) == (h, r) and fica_com_ron:
        continue
    total_harry += plant[h][j]

for i in range(TAM):
    if (i, r) == (h, r) and not fica_com_ron:
        continue
    total_ron += plant[i][r]

print("Harry", total_harry)
print("Ron", total_ron)
