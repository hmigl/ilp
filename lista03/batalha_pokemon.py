endurance_pts, damage_pts = map(int, input().split())
needed_attacks = 0

while damage_pts != 0:
    needed_attacks += 1
    endurance_pts -= damage_pts
    if endurance_pts <= 0:
        break
    damage_pts -= 1

if damage_pts == 0 and endurance_pts >= 0:
    print("F")
else:
    print(needed_attacks)
