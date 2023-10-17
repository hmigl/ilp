interessados = int(input())
forcas = [int(n) for n in input().split()]
forca_yoda = int(input())

selecionados = []
forca_min = forca_yoda / 2

for i, n in enumerate(forcas):
    if n >= forca_min:
        selecionados.append(i)

print(*selecionados)
