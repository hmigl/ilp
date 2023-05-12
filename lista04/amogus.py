players = int(input())
assassinations = list(map(int, input().split()))

ranking = [-1] * (max(assassinations) + 1)

for n in assassinations:
    ranking[n] = n

print(" ".join(str(n) for n in ranking if n > -1))
