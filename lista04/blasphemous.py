levels = int(input())
repr_of_each_level = list(map(int, input().split()))
player_hp = int(input())
max_hp = player_hp
can_win = True

for repr in repr_of_each_level:
    if repr == 1:
        player_hp = max_hp
    elif repr >= 2:
        player_hp -= repr
        if player_hp < 1:
            can_win = False
            break

print("Yes, you can") if can_win else print("You Died")
