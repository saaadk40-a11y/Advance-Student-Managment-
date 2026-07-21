from student_manager import StudentManager

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:
    COLOR_ENABLED = False


def color_text(text, color=None):
    if COLOR_ENABLED and color:
        return f"{color}{text}{Style.RESET_ALL}"
    return text


def print_success(text):
    print(color_text(text, Fore.GREEN if COLOR_ENABLED else None))


def print_error(text):
    print(color_text(text, Fore.RED if COLOR_ENABLED else None))


def print_info(text):
    print(color_text(text, Fore.CYAN if COLOR_ENABLED else None))


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print_error("This field cannot be empty.")


def get_valid_int(prompt, min_value=1, max_value=120):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and min_value <= int(value) <= max_value:
            return int(value)
        print_error(f"Please enter a valid whole number between {min_value} and {max_value}.")


def get_valid_marks(prompt, allow_blank=False):
    while True:
        value = input(prompt).strip()
        if allow_blank and value == "":
            return None
        try:
            marks = float(value)
            if 0 <= marks <= 100:
                return marks
        except ValueError:
            pass
        print_error("Please enter valid marks (a number between 0 and 100).")


def get_optional_int(prompt, min_value=1, max_value=120):
    while True:
        value = input(prompt).strip()
        if value == "":
            return None
        if value.isdigit() and min_value <= int(value) <= max_value:
            return int(value)
        print_error(f"Please enter a valid whole number between {min_value} and {max_value}, or leave blank.")


def print_student_table(students):
    if not students:
        print_info("No student records found.")
        return

    print(f"\n{'Roll No':<10}{'Name':<20}{'Age':<6}{'Department':<24}{'Marks':<8}")
    print("-" * 68)
    for s in students:
        print(f"{s.roll_number:<10}{s.name:<20}{str(s.age):<6}{s.department:<24}{s.marks:<8}")


def show_menu():
    print_info("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Generate Report")
    print("7. Exit")


def main():
    manager = StudentManager()

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            roll_number = get_non_empty("Roll Number: ")
            name = get_non_empty("Name: ")
            age = get_valid_int("Age: ", min_value=1, max_value=100)
            department = get_non_empty("Department: ")
            marks = get_valid_marks("Marks (0-100): ")
            success, message = manager.add_student(roll_number, name, age, department, marks)
            print_success(message) if success else print_error(message)

        elif choice == "2":
            sort_choice = input("Sort by (1) None (2) Marks (3) Name: ").strip()
            sort_by = {"2": "marks", "3": "name"}.get(sort_choice)
            print_student_table(manager.get_all_students(sort_by=sort_by))

        elif choice == "3":
            roll_number = get_non_empty("Enter Roll Number to search: ")
            student = manager.search_student(roll_number)
            if student:
                print_success(str(student))
            else:
                print_error("Student not found.")

        elif choice == "4":
            roll_number = get_non_empty("Enter Roll Number to update: ")
            if not manager.find_student(roll_number):
                print_error("Student not found.")
                continue
            print_info("Leave a field blank to keep it unchanged.")
            name = input("New name: ").strip()
            age = get_optional_int("New age: ")
            department = input("New department: ").strip()
            marks = get_valid_marks("New marks: ", allow_blank=True)
            success, message = manager.update_student(
                roll_number, name or None, age, department or None, marks
            )
            print_success(message) if success else print_error(message)

        elif choice == "5":
            roll_number = get_non_empty("Enter Roll Number to delete: ")
            success, message = manager.delete_student(roll_number)
            print_success(message) if success else print_error(message)

        elif choice == "6":
            report_text = manager.generate_report()
            print(report_text)
            print_success("\nReport saved to report.txt")

            top_students = manager.top_scorers(3)
            if top_students:
                print_info("\nTop 3 highest-scoring students:")
                for i, s in enumerate(top_students, start=1):
                    print(f"  {i}. {s.name} (Roll No: {s.roll_number}, Marks: {s.marks})")

        elif choice == "7":
            print_info("Goodbye!")
            break

        else:
            print_error("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
