n: int = int(input())

j: int = 1
while j <= n:
    print(f"{' ' * (n - j)}{str(j) * (j * 2 - 1)}")
    j += 1
