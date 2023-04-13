tracks, people_per_track, students = map(int, input().split())
can_everyone_play = tracks * people_per_track >= students + 1

if can_everyone_play:
    print("S")
else:
    print("N")
