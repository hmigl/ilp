T = 10
mapa_errado = [input().split() for _ in range(T)]
mapa_correto = [row[:] for row in mapa_errado]

for i in range(T):
    for j in range(T):
        if mapa_errado[i][j] == "t":
            praia = (
                (i > 0 and mapa_errado[i - 1][j] == "*")
                or (i < T - 1 and mapa_errado[i + 1][j] == "*")
                or (j > 0 and mapa_errado[i][j - 1] == "*")
                or (j < T - 1 and mapa_errado[i][j + 1] == "*")
            )
            if praia:
                mapa_correto[i][j] = "p"

for i in range(T):
    print(*mapa_correto[i])
