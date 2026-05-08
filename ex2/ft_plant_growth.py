class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = 0.8

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    start_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    total_growth = round(rose.height - start_height, 1)
    print(f"Growth this week: {total_growth:.1f}cm")

# =======================================================================#
# __init__ Python automatically calls __init__ when the object is created.
# round is to get closer to the nearest decimal after '.'
# for day in range is going to loop for each day starting from 1 to 7
# =======================================================================#
