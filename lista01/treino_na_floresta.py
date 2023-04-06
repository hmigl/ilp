track_len, intended_dist = map(int, input().split())
track_end_point = intended_dist % track_len

print(track_end_point)
