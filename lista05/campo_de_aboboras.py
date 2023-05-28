size = int(input())
pumpkin_plantation = [[int(n) for n in input().split()] for _ in range(size)]
harry_row_number, ron_col_number = [int(n) for n in input().split()]

harry_row = pumpkin_plantation[harry_row_number]
ron_row = [row[ron_col_number] for row in pumpkin_plantation]
total_harry_collected, total_ron_collected = sum(harry_row), sum(ron_row)

intersection = pumpkin_plantation[harry_row_number][ron_col_number]
harry_distance = min(
    i for i, n in enumerate(harry_row) if n == intersection and i >= ron_col_number
)
ron_distance = min(
    i for i, n in enumerate(ron_row) if n == intersection and i >= harry_row_number
)

if harry_distance < ron_distance:
    total_ron_collected -= intersection
else:
    total_harry_collected -= intersection

print(f"Harry {total_harry_collected}")
print(f"Ron {total_ron_collected}")
