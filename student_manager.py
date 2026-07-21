import os
import json
from datetime import datetime
from student import Student

DATA_FILE = "students.json"
REPORT_FILE = "report.txt"


class StudentManager:
    """Handles all CRUD operations, JSON persistence, and report generation."""

    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as f:
                json.dump([], f)

        try:
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.students = [Student(**item) for item in data]
        except (json.JSONDecodeError, TypeError):
            print("Warning: data file was invalid or empty. Starting with an empty list.")
            self.students = []

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump([s.to_dict() for s in self.students], f, indent=4)

    def find_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def add_student(self, roll_number, name, age, department, marks):
        if self.find_student(roll_number):
            return False, "A student with this Roll Number already exists."

        self.students.append(Student(roll_number, name, age, department, marks))
        self.save_data()
        return True, "Student added successfully."

    def get_all_students(self, sort_by=None):
        """Return all students, optionally sorted by 'marks' or 'name'."""
        if sort_by == "marks":
            return sorted(self.students, key=lambda s: s.marks, reverse=True)
        if sort_by == "name":
            return sorted(self.students, key=lambda s: s.name.lower())
        return self.students

    def search_student(self, roll_number):
        return self.find_student(roll_number)

    def update_student(self, roll_number, name=None, age=None, department=None, marks=None):
        student = self.find_student(roll_number)
        if not student:
            return False, "Student not found."

        if name:
            student.name = name
        if age is not None:
            student.age = age
        if department:
            student.department = department
        if marks is not None:
            student.marks = marks

        self.save_data()
        return True, "Student updated successfully."

    def delete_student(self, roll_number):
        student = self.find_student(roll_number)
        if not student:
            return False, "Student not found."

        self.students.remove(student)
        self.save_data()
        return True, "Student deleted successfully."

    def top_scorers(self, count=3):
        return sorted(self.students, key=lambda s: s.marks, reverse=True)[:count]

    def generate_report(self):
        """Build report data and save it to a .txt file. Returns the report text."""
        total = len(self.students)

        department_counts = {}
        for student in self.students:
            department_counts[student.department] = department_counts.get(student.department, 0) + 1

        top_student = max(self.students, key=lambda s: s.marks) if self.students else None

        lines = []
        lines.append("=" * 55)
        lines.append("STUDENT RECORD SYSTEM - SUMMARY REPORT")
        lines.append("=" * 55)
        lines.append(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"Total number of students: {total}")
        lines.append("-" * 55)
        lines.append("Students per department:")
        if department_counts:
            for dept, count in sorted(department_counts.items()):
                lines.append(f"  {dept:<20}: {count}")
        else:
            lines.append("  No records found.")
        lines.append("-" * 55)
        if top_student:
            lines.append(f"Highest scoring student: {top_student.name} "
                          f"(Roll No: {top_student.roll_number}, Marks: {top_student.marks})")
        else:
            lines.append("Highest scoring student: N/A")
        lines.append("=" * 55)

        report_text = "\n".join(lines)

        with open(REPORT_FILE, "w") as f:
            f.write(report_text + "\n")

        return report_text
