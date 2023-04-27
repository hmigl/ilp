vulcan_pressure_limit = int(input())
internal_pressure = -1
alert = False

while True:
    internal_pressure = int(input())
    if internal_pressure == 0:
        break
    elif internal_pressure > vulcan_pressure_limit:
        alert = True

print("ALARME") if alert else print("O Havai pode dormir tranquilo")
