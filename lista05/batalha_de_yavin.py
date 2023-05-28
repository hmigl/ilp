size, teleports = [int(n) for n in input().split()]
coordinates = [[int(n) for n in input().split()] for _ in range(size)]
destroyed_probes = 0

for _ in range(teleports):
    x, y = [int(n) for n in input().split()]
    current_column = [row[y] for row in coordinates[: x + 1]][::-1]
    if 1 in current_column:
        first_probe_index = current_column.index(1)
        coordinates[x - first_probe_index][y] = 0
        destroyed_probes += 1

print(destroyed_probes)
