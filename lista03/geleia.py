hamburgers = int(input())
with_jam = 0
without_jam = 0

for i in range(hamburgers):
    if int(input()) == 10:
        without_jam += 1
    else:
        with_jam += 1

print("Tradicional") if without_jam > with_jam else print("Geleia")
