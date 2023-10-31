T = 8
tab = [[int(n) for n in input().split()] for _ in range(T)]
x, y = map(int, input().split())

direcoes = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # esquerda, direita, cima, baixo
qntd_inimigos = 0

for dir_x, dir_y in direcoes:
    i, j = x + dir_x, y + dir_y

    while 0 <= i < T and 0 <= j < T:
        if tab[i][j] == 1:
            break
        if tab[i][j] == 2:
            qntd_inimigos += 1
            break
        i += dir_x
        j += dir_y

print(qntd_inimigos)
