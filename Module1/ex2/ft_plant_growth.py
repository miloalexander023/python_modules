class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.p_age = age
        self.growth = int(0)

    def grow(self):
        self.height += 0.8
        self.growth += 0.8

    def age(self):
        self.p_age += 1

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.p_age} days old")
    
    def show_growth(self):
        print(f"Growth this week: {self.growth:.1f}cm")
        
if __name__ == "__main__":
    week = 7
    print("=== Garden Plant Growth ===")
    p1 = Plant("Rose", 25, 30)
    p1.show()
    for day in range(1, week + 1):
        p1.grow()
        p1.age()
        print(f"=== Day {day} ===")
        p1.show()
    p1.show_growth()