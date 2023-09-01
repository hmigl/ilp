qntd_requerida, disponivel = map(int, input().split())

qntd_restante_eh_par_e_menor_igual_estoque: bool = (
    disponivel - qntd_requerida
) % 2 == 0 and (disponivel - qntd_requerida) >= 0

print("vendido") if qntd_restante_eh_par_e_menor_igual_estoque else print("sinto muito")
