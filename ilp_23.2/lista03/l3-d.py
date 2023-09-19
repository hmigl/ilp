n, y = input().split()

n = int(n)
y = float(y)

total = m = 0
comprou = False
for _ in range(n):
    x = float(input())
    if total < y and not comprou:
        m += 1
    else:
        comprou = True
    total += x

if total >= y or comprou:
    print(f"{m} {(total - y):.2f}")
else:
    print(f"0 {total:.2f}")
