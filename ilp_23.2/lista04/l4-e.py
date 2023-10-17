num_dobr = int(input())
hab_dobr = [int(n) for n in input().split()]
id_dobr = [int(n) for n in input().split()]
elemento = int(input())

res = []
for i in range(num_dobr):
    if hab_dobr[i] == elemento:
        res.append(id_dobr[i])

print(*res) if len(res) > 0 else print("Nenhum")
