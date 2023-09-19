n = int(input())

player_lvl = 1
for _ in range(n):
    codigo_porta, variacao_lvl = input().split()
    variacao_lvl = int(variacao_lvl)

    if codigo_porta == "t":
        player_lvl += variacao_lvl
        aventura_completa = player_lvl >= 5
        if aventura_completa:
            print("Aventura concluida")
            break

    elif codigo_porta == "m":
        print("Combate iniciado")
        if player_lvl >= variacao_lvl:
            print("VITORIA")
            player_lvl += 1
            aventura_completa = player_lvl >= 5
            if aventura_completa:
                print("Aventura concluida")
                break
        else:
            print("Derrota! Fim da aventura")
            break

    elif codigo_porta == "b":
        player_lvl -= variacao_lvl
        if player_lvl < 0:
            player_lvl = 0

    else:
        print()
