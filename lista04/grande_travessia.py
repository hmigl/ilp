frogs, stones = map(int, input().split())
steped_stones = [0] * stones

for frog in range(frogs):
    jump_size = int(input())
    steped_stones = [
        1 if i % jump_size == 0 else val for i, val in enumerate(steped_stones)
    ]

print(" ".join(str(n) for n in steped_stones))
