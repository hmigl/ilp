n1: float = float(input())
n2: float = float(input())
n3: float = float(input())
n4: float = float(input())

nota: float = (n1 + n2 + n3 + n4) / 4

print("Parabens bruxao, eh nois que voa, voce passou!") if nota >= 5 else print(
    "Voce nao passou, tente usar a varinha na proxima vez!"
)
