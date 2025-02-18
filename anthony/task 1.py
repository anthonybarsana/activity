class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.year} {self.brand} {self.model}")

    def is_classic(self):
        current_year = 2025
        if current_year - self.year >= 20:
            return True
        else:
            return False

# Create two car objects
car1 = Car("Ford", "Mustang", 1969)
car2 = Car("Tesla", "Model 3", 2022)

# Display their details
car1.display_info()
if car1.is_classic():
    print("This car is a classic!")
else:
    print("This car is not a classic.")

car2.display_info()
if car2.is_classic():
    print("This car is a classic!")
else:
    print("This car is not a classic.")
