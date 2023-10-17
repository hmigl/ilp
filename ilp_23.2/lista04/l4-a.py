n_caixas = int(input())
esmeraldas = [int(n) for n in input().split()]
esmeralda_caos = int(input())

print(esmeralda_caos) if esmeralda_caos in esmeraldas else print(-1)
