class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}") 
class engineer(employee):
    def __init__(self, name, age, salary, specialization):
        super().__init__(name, age, salary)
        self.specialization = specialization
    def show(self):
        super().show()
        print(f"Specialization: {self.specialization}")

e = engineer("Omkar", 24, 50000, "Software")
e.show()
print(isinstance(e, engineer))  # True
print(isinstance(e, employee))  # True  