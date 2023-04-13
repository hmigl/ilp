performance_evaluation = sum(list(map(int, input().split())))
ranking_ranges = {
    (250, 301): "S+",
    (200, 250): "S",
    (180, 200): "S-",
    (150, 180): "A+",
    (100, 150): "A",
    (80, 100): "A-",
    (60, 80): "B+",
    (40, 60): "B",
    (0, 40): "B-",
}

for k, v in ranking_ranges.items():
    if performance_evaluation >= k[0] and performance_evaluation < k[1]:
        print(v)
        break
