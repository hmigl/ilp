steel, wood, leather = map(int, input().split())
used_steel = 2
used_wood = 3
used_leather = 5

max_swords = min(steel // used_steel, wood // used_wood, leather // used_leather)
print(max_swords)
