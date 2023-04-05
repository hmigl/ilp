argv = input().split()
flash_current_mass_kg = int(argv[0])
flash_speed_mps = int(argv[1])
energy = flash_current_mass_kg * flash_speed_mps**2

print(energy)
