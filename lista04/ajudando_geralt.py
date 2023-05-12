n = int(input())
id_of_each_person = list(map(int, input().split()))

seen = set()
found = False

for num in id_of_each_person:
    if num in seen:
        found = True
        print(num)
        break
    seen.add(num)

if not found:
    print(-1)
