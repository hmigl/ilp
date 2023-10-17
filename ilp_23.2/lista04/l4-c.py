num_obs = int(input())
alturas = [int(n) for n in input().split()]
alt_max = int(input())

i = 0
while i < num_obs:
    if alturas[i] > alt_max:
        break
    i += 1

print(i)
print(0) if i < num_obs else print(1)
