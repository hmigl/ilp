T = 7
jogo = [[int(n) for n in input().split()] for _ in range(T)]
pecas = 0
em_campo = []

for i in range(T):
    for j in range(T):
        if jogo[i][j] == 1 and (i, j) not in em_campo:
            em_campo.append((i, j))
            em_campo.append((j, i))
            pecas += 1

print(pecas)
