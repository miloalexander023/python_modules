class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 200)

    p1.show()
    p2.show()
    p3.show()

    print("\n=== End of Program ===")
    