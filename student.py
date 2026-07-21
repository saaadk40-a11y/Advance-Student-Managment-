class Student:
    """Represents a single student record."""

    def __init__(self, roll_number, name, age, department, marks):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.department = department
        self.marks = marks

    def to_dict(self):
        return {
            "roll_number": self.roll_number,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "marks": self.marks,
        }

    def __str__(self):
        return (f"Roll No: {self.roll_number} | Name: {self.name} | Age: {self.age} | "
                f"Department: {self.department} | Marks: {self.marks}")
