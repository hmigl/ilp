dim_map = int(input())
map = [[int(n) for n in input().split()] for _ in range(dim_map)]

num_coord = int(input())
coords = [[int(n) for n in input().split()] for _ in range(num_coord)]

num_esp = 0

for coord in coords:
    num_esp += map[coord[0]][coord[1]]

print(num_esp)
