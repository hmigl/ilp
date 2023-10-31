m, n = map(int, input().split())
terreno = [[int(n) for n in input().split()] for _ in range(m)]
char, num = input().split()
num = int(num) - 1

total = 0

if char == "L":
    for j in range(n):
        total += terreno[num][j]
else:
    for i in range(m):
        total += terreno[i][num]

print(total)
