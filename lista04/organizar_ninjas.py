battlefronts = int(input())
ninjas_per_battlefront = input().split()[::-1]

for i in range(battlefronts):
    print(f"{battlefronts - i}: {ninjas_per_battlefront[i]}")
