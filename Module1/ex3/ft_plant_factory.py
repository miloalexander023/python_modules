class Plant:
    def __init__(self, name, height, age):
        self.name = name.capitalize()
        self.height = height
        self.p_age = age
        self.growth = 0
        
    def grow(self):
        if self.name == "Rose":
            self.height += 0.8
            self.growth += 0.8
        elif self.name == "Oak":
            self.height += 0.3
            self.growth += 0.3
        elif self.name == "Cactus":
            self.height += 0.1
            self.growth += 0.1
        elif self.name == "Sunflower":
            self.height += 2.5
            self.growth += 2.5
        elif self.name == "Fern":
            self.height += 0.2
            self.growth += 0.2
    def age(self):
        self.p_age += 1

    def show(self):
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.p_age} days old")

    def show_growth(self):
        print(f"{self.name}: {self.growth:.1f}cm")

if __name__ == "__main__":
    week = 7
    print("=== Plant Factory Output ===")

    plants = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120)
	]
    for day in range(1, week + 1):
        print(f"=== Day {day} ===")
        for plant in plants:
            plant.show()
            plant.grow()
            plant.age()
    print("=== Total Grwoth This Week ===")
    for plant in plants:
        plant.show_growth()