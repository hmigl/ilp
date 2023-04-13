found_star_coins, found_mega_mushrooms, found_blue_koopa_shells = map(
    int, input().split()
)
max_star_coins_num = 30
max_mega_mushrooms_num = 6
max_blue_koopa_shells = 3

if found_star_coins != max_star_coins_num:
    print(
        f"{max_star_coins_num - found_star_coins} {max_mega_mushrooms_num - found_mega_mushrooms} {max_blue_koopa_shells - found_blue_koopa_shells}"
    )
else:
    print("PROXIMO MUNDO")
