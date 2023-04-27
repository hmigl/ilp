pokemon_num = int(input())

for i in range(pokemon_num):
    damage_points, increment = map(int, input().split())
    damage_points += increment
    print(damage_points)
