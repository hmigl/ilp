LEVI_KILLS_PER_HOUR: int = 20
titans: int = int(input())

common_soldiers: int = (titans - LEVI_KILLS_PER_HOUR) // 5
print(common_soldiers)
