def teilbarkeit(x, y):
    if y == 0:
        print("Es ist nicht möglich durch 0 zu teilen!")
    elif x == y:
        print("x und y sind gleich")
    elif x % y == 0:
        print(f"{x} ist durch {y} teilbar")
    else:
        print(f"{x} ist nicht durch {y} teilbar")
teilbarkeit(10, 2)
teilbarkeit(2, 2)
teilbarkeit(10, 0)
teilbarkeit(0,5)
