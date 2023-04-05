from statistics import mean

argv = list(map(int, input().split()))
athlete_registration_num = argv[0]
scores = argv[1:]
mean_score = "{:.1f}".format(mean(scores))

print(athlete_registration_num, mean_score)
