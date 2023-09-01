# v2
area_total, qntd_difusores = map(int, input().split())
CAPACIDADE_ALIMENTACAO = 9

area_alimentada: int = area_total - qntd_difusores * CAPACIDADE_ALIMENTACAO

if area_alimentada <= 0:
    print("Lar doce lar.")
else:
    print("Precisa de mais difusores!")
    difusores_extras, sobra = (
        area_alimentada // CAPACIDADE_ALIMENTACAO,
        area_alimentada % CAPACIDADE_ALIMENTACAO,
    )
    if sobra > 0:
        difusores_extras += 1
    print(difusores_extras)
