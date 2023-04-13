def_intended_dir, gk_intended_dir = input().split()
stkr_intended_dir1, stkr_intended_dir2 = input().split()

if stkr_intended_dir1 != def_intended_dir:
    print("Bloqueado")
else:
    print("Driblado")
    if stkr_intended_dir2 != gk_intended_dir:
        print("...e o goleiro pega")
    else:
        print("Gol")
