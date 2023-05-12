dwarves = int(input())
sum = 0

for i in range(dwarves):
    name, weight = input().split()
    weight = int(weight)
    if name == "Bilbo":
        continue
    sum += weight

total_capacity = int(input())
print("Vamos todos encontrar a montanha!") if sum <= total_capacity else print(
    "Vamos virar almoço de aranhas gigantes!"
)
