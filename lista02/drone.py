coordinates_for_delivery_x, coordinates_for_delivery_y = map(int, input().split())
current_coordinates_x, current_coordinates_y = map(int, input().split())

if (coordinates_for_delivery_x, coordinates_for_delivery_y) == (
    current_coordinates_x,
    current_coordinates_y,
):
    print("Soltar pacote")
else:
    print("Nao soltar pacote")
