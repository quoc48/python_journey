class Employee:
    """Colect employee name"""
    def __init__(self, first_name, last_name, salary=0):
        self.first = first_name
        self.last = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount
