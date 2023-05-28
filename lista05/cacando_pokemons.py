rows, cols = [int(n) for n in input().split()]
poke_capture_field = [[int(n) for n in input().split()] for _ in range(rows)]
pokemon_type = int(input())

got = sum(row.count(pokemon_type) for row in poke_capture_field)
print(f"Ash pegou {got} pokemon")
