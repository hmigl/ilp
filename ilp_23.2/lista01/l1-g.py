tempo_em_segundos: int = int(input())

horas: int = tempo_em_segundos // 3600
sobra = tempo_em_segundos % 3600

minutos: int = sobra // 60

segundos: int = sobra % 60

print(f"{horas}h {minutos}m {segundos}s")
