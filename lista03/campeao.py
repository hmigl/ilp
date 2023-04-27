favorite_champions = int(input())
greatest_power_level = -1

for i in range(favorite_champions):
    greatest_power_level = max(greatest_power_level, int(input()))

print(greatest_power_level)
