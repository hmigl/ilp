rows, cols = [int(n) for n in input().split()]
cinema = [[int(n) for n in input().split()] for _ in range(rows)]

for row in cinema:
    for i in range(len(row) - 1):
        if row[i : i + 2] == [0, 0]:
            print(f"Fileira: {cinema.index(row) + 1}")
            print(f"Assentos: {i + 1} e {i + 2}")
            break
