x, y = map(int, input().split())

if not (0 < x < 100) or not (0 < y < 100):
    print("Coordenada invalida")
elif x > 70 or y > 70:
    print("Coordenada valida e o navio esta longe")
else:
    print("Coordenada valida e o navio esta perto")
