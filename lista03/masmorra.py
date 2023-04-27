num_doors = int(input())
player_lvl = 1

for i in range(num_doors):
    door_code, lvl_change = input().split()
    lvl_change = int(lvl_change)

    if door_code == "t":
        player_lvl += lvl_change
        adventure_complete = player_lvl >= 5
        if adventure_complete:
            print("Aventura concluida")
            break

    elif door_code == "m":
        print("Combate iniciado")
        if player_lvl >= lvl_change:
            print("VITORIA")
            player_lvl += 1
            adventure_complete = player_lvl >= 5
            if adventure_complete:
                print("Aventura concluida")
                break
        else:
            print("Derrota! Fim da aventura")
            break

    elif door_code == "b":
        player_lvl -= lvl_change
        if player_lvl < 0:
            player_lvl = 0

    else:
        print()
