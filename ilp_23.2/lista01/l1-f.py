tamanho_estrada, dist_pedagios = map(int, input().split())
valor_por_km, valor_por_pedagio = map(int, input().split())

total: int = (
    tamanho_estrada * valor_por_km
    + (tamanho_estrada // dist_pedagios) * valor_por_pedagio
)
print(total)
