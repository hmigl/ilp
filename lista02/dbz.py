team_total_ki = 0

for i in range(5):
    team_total_ki += int(input())

if team_total_ki > 5000:
    print("Acesso proibido")
else:
    print("Acesso liberado")
