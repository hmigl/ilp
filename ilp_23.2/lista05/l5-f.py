T, teleports = map(int, input().split())
coords = [[int(n) for n in input().split()] for _ in range(T)]
naves_destruidas = 0

for _ in range(teleports):
    x, y = map(int, input().split())
    for i in range(x, -1, -1):
        if coords[i][y] == 1:
            naves_destruidas += 1
            coords[i][y] = 0
            break

print(naves_destruidas)
