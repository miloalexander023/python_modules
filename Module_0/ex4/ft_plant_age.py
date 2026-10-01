def ft_plant_age() -> None:
    age: int = int(input("plant's age: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
