# StudentRecordSystem

## Project Overview
An advanced Python application to manage student records using file handling and JSON storage, built with Object-Oriented Programming principles. Supports full CRUD operations, input validation, sorting, and automated report generation.

## Features
- Add a new student record (Roll Number, Name, Age, Department, Marks)
- View all student records, with optional sorting by marks or name
- Search for a student by Roll Number
- Update an existing student's information (leave a field blank to keep it unchanged)
- Delete a student record
- Stores all records permanently in `students.json` (auto-created if missing)
- Generates `report.txt` containing:
  - Total number of students
  - Number of students in each department
  - Student with the highest marks
  - Timestamp of report generation
- Validates input: rejects duplicate Roll Numbers, invalid ages, and marks outside 0–100
- Displays the top 3 highest-scoring students after generating a report
- Colored terminal output (via `colorama`) for success, error, and info messages

## Technologies Used
- Python 3
- `json` — data persistence
- `datetime` — report timestamps
- `colorama` — colored terminal output (optional; falls back to plain text if not installed)

## How to Run
```bash
pip install colorama
python main.py
```

Menu options:
```
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Generate Report
7. Exit
```

## Folder Structure
```
StudentRecordSystem/
│── main.py             # menu-driven CLI, entry point
│── student.py           # Student class
│── student_manager.py   # StudentManager class (CRUD, JSON, report logic)
│── students.json         # student data (auto-created, sample data included)
│── report.txt            # generated summary report
│── README.md
```

## Git & GitHub
```bash
git init
git add .
git commit -m "Add Student Record System: OOP-based CRUD app with reporting"
git branch -M main
git remote add origin https://github.com/<your-username>/StudentRecordSystem.git
git push -u origin main
```
