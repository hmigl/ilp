q1, q2, q3 = map(int, input().split())
e1, e2, e3 = map(int, input().split())

coletados = q1 + q2 + q3
sobraram = coletados - (e1 + e2 + e3) * 3
print(sobraram)
