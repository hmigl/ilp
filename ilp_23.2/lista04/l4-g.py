qntd_secoes = int(input())
s = [int(n) for n in input().split()]

sum_esq = 0
sum_dir = sum(s)

for i in range(qntd_secoes):
    sum_esq += s[i]
    sum_dir -= s[i]
    if sum_esq == sum_dir:
        print(i + 1)
        break
