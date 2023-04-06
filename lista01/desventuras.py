colected_eggs = list(map(int, input().split()))
poisoned_eggs = list(map(int, input().split()))
leftover_eggs = 0

for i, egg in enumerate(poisoned_eggs):
    colected_eggs[i] -= poisoned_eggs[i] * 3
    leftover_eggs += colected_eggs[i]

print(leftover_eggs)
