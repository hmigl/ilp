rows, cols = [int(n) for n in input().split()]
lab_analysis_slide = [[int(n) for n in input().split()] for _ in range(rows)]
x, y = 0, 0

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if (
            lab_analysis_slide[i][j] == 0
            and lab_analysis_slide[i - 1][j]
            == lab_analysis_slide[i + 1][j]
            == lab_analysis_slide[i][j - 1]
            == lab_analysis_slide[i][j + 1]
            == 1
        ):
            x, y = i, j
            break

print(f"{x} {y}")
