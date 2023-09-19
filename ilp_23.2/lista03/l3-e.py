resistencia_oponente, dano_causado = map(int, input().split())

ataques_necessarios = 0
while dano_causado != 0:
    ataques_necessarios += 1
    resistencia_oponente -= dano_causado
    if resistencia_oponente <= 0:
        break
    dano_causado -= 1

print("F") if resistencia_oponente >= 0 and dano_causado == 0 else print(
    ataques_necessarios
)
