class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self._height = height
        self._p_age = age
        self.growth = int(0)

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self.growth += new_height - self._height
        self._height = new_height

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._p_age = new_age

    def get_height(self) -> float:
        return self._height
    
    def get_age(self) -> float:
        return self._p_age
    
    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._p_age} days old")

    def show_growth(self):
        print(f"{self.name}: {self.growth:.1f}cm")

def set_height_name(plants, name, new_height) -> None:
    if new_height < 0:
        print(f"{name}: Error, height can't be negative")
        print("Age update rejected")
        return
    for plant in plants:
        if plant.name == name.capitalize():
            plant.set_height(new_height)
            print(f"Height updated: {new_height}cm")
            return
    print(f"No plant named {name} found.")

def set_age_name(plants, name, new_age) -> None:
    if new_age < 0:
        print(f"{name}: Error, age can't be negative")
        print("Age update rejected")
        return
    for plant in plants:
        if plant.name == name.capitalize():
            plant.set_age(new_age)
            print(f"Age updated: {new_age} days")
            return
    print(f"No plant named {name} found.")

if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120)
    	]

    for plant in plants:
        plant.show()
    print("")
    set_height_name(plants, "rose", 40)
    set_height_name(plants, "oak", 250)
    set_height_name(plants, "cactus", 15)
    set_age_name(plants, "rose", 35)
    print("")
    set_height_name(plants, "rose", -40)
    set_age_name(plants, "rose", -40)
    print("")
    for plant in plants:
        height = plant.get_height()
        age = plant.get_age()
        print(f"Current state: {plant.name}: {height:.1f}cm, {age} days old")