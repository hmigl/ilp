comprimento_cubo_grande, comprimento_cubo, qntd_cubos = map(int, input().split())

print("Eh possivel") if (
    (comprimento_cubo_grande**3) / (comprimento_cubo**3) <= qntd_cubos
) else print("!Eh possivel")
