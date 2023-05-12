boxes = int(input())
emeralds_codes = list(map(int, input().split()))
chaos_emerald_num = int(input())

print(chaos_emerald_num) if chaos_emerald_num in emeralds_codes else print(-1)
