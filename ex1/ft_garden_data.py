class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


# ====================================================================#
# Plant is a class .
# show is a method because its a function inside a class
# self refers to the object that called the method.
# if __name__ == "__main__": it makes sure this file will run not else
# ====================================================================#
