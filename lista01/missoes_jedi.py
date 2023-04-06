total_xp = eval(input().replace(" ", "*"))
current_xps = list(map(int, input().split()))

print(f"Yoda {current_xps[0] + total_xp}")
print(f"Luke {current_xps[1] + total_xp}")
print(f"Ahsoka {current_xps[2] + total_xp}")
