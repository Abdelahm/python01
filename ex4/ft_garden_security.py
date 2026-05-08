class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0
        self.set_height(height)
        self.set_age(age_days)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age_days: int) -> bool:
        if age_days < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age_days = age_days
        return True

    def grow(self) -> None:
        self.set_height(round(self._height + 0.8, 1))

    def age(self) -> None:
        self.set_age(self._age_days + 1)

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age_days} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    if rose.set_height(25):
        print("Height updated: 25cm")
    else:
        print("Height update rejected")

    if rose.set_age(30):
        print("Age updated: 30 days")
    else:
        print("Age update rejected")

    print()

    if rose.set_height(-5):
        print("Height updated: -5cm")
    else:
        print("Height update rejected")

    if rose.set_age(-10):
        print("Age updated: -10 days")
    else:
        print("Age update rejected")

    print()

    print("Current state: ", end="")
    rose.show()

# ====================================================#
# Encapsulation like _height  you can make properties
# private by using a double underscore __ prefix It
# means keeping data (properties) and methods together
# in a class, while controlling how the data can be
# accessed from outside the class.
# Getters function such     def get_height(self)
# A getter is a method used to safely read a value
# from inside a class.
# ===================================================#
