n: int = int(input())

while n > 0:
    dano, acres = map(int, input().split())
    print(dano + acres)
    n -= 1
