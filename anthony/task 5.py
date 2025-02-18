import random

class Employee:
    def __init__(self, name, position, salary, department):
        self.name = name
        self.position = position
        self.salary = salary
        self.department = department
        self.employee_id = self.generate_employee_id()
        self.performance_score = 0
        self.promotion_eligible = False

    def generate_employee_id(self):
        """Generate a unique employee ID."""
        return f"EMP{random.randint(1000, 9999)}"

    def set_performance_score(self, score):
        """Set performance score and check if the employee is eligible for promotion."""
        if 0 <= score <= 100:
            self.performance_score = score
            if score >= 85:
                self.promotion_eligible = True
        else:
            raise ValueError("Performance score must be between 0 and 100.")

    def give_raise(self, amount):
        """Increase the salary by a fixed amount based on the performance score."""
        if amount < 0:
            raise ValueError("Raise amount must be positive.")
        raise_multiplier = 1 + (self.performance_score / 100)
        self.salary += amount * raise_multiplier

    def promote(self):
        """Promote the employee if they are eligible."""
        if self.promotion_eligible:
            if self.position == "Junior Developer":
                self.position = "Senior Developer"
            elif self.position == "Senior Developer":
                self.position = "Lead Developer"
            self.salary *= 1.2  # Salary increase with promotion
            print(f"{self.name} has been promoted to {self.position}.")
        else:
            print(f"{self.name} is not eligible for promotion.")

    def calculate_bonus(self):
        """Calculate a bonus based on salary and performance score."""
        bonus_percentage = 0.05 if self.performance_score >= 85 else 0.02
        bonus = self.salary * bonus_percentage
        return bonus

    def display_employee(self):
        """Display the details of the employee."""
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Performance Score: {self.performance_score}")
        print(f"Promotion Eligible: {self.promotion_eligible}")
        print(f"Bonus: ${self.calculate_bonus():.2f}")

# Create an employee instance
employee1 = Employee("Anthony Barsana", "Junior Developer", 70000, "IT Department")

# Set performance score (0 to 100)
employee1.set_performance_score(90)

# Give the employee a raise
employee1.give_raise(5000)

# Promote the employee if eligible
employee1.promote()

# Display the employee's details
employee1.display_employee()
