def borrow_power_from_ajacent_units(troop, code, i, j):
    borrowed_power = 0
    if i > 0 and troop[i - 1][j] in [code, "m"]:
        borrowed_power += 1
    if i < battlefield_size - 1 and troop[i + 1][j] in [code, "m"]:
        borrowed_power += 1
    if j > 0 and troop[i][j - 1] in [code, "m"]:
        borrowed_power += 1
    if j < troop_battlefield_size - 1 and troop[i][j + 1] in [code, "m"]:
        borrowed_power += 1
    return borrowed_power


def upgrade_troop_power(troop, code, troop_power):
    for i in range(battlefield_size):
        for j in range(troop_battlefield_size):
            if troop[i][j] in [code, "m"]:
                troop_power += borrow_power_from_ajacent_units(troop, code, i, j)
    return troop_power


def compute_troop_power(troop, code, has_wizard):
    troop_power = sum(units.count(code) for units in troop)
    troop_power += sum(units.count("m") for units in troop)
    if has_wizard:
        troop_power = upgrade_troop_power(troop, code, troop_power)
    return troop_power


def has_wizard(troop):
    return any("m" in units for units in troop)


battlefield_size = 10
troop_battlefield_size = battlefield_size // 2
battlefield = [input().split() for _ in range(battlefield_size)]

orc_troop = [units[:5] for units in battlefield]
orc_troop_power = compute_troop_power(
    orc_troop,
    "o",
    has_wizard(orc_troop),
)

human_troop = [units[5:] for units in battlefield]
human_troop_power = compute_troop_power(
    human_troop,
    "h",
    has_wizard(human_troop),
)

if orc_troop_power > human_troop_power:
    print("Loktar Ogar!!!")
elif human_troop_power > orc_troop_power:
    print("Pela Alianca!")
else:
    print("Batalha lendaria!")
