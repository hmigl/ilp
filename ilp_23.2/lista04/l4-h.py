sapos, qntd_pedras = map(int, input().split())
caminho = [0] * qntd_pedras

for _ in range(sapos):
    pulo = int(input())
    for j in range(0, qntd_pedras, pulo):
        caminho[j] = 1

print(*caminho)
