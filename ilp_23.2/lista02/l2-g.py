dir_zagueiro, dir_goleiro = input().split()
dir1_atacante, dir2_atacante = input().split()

if dir1_atacante != dir_zagueiro:
    print("Bloqueado")
else:
    print("Driblado")
    if dir2_atacante != dir_goleiro:
        print("...e o goleiro pega")
    else:
        print("Gol")
