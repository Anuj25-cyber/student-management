# Student Management System

## Introduction
The Student Management System is a simple web application developed as a college mini project. It helps manage student records such as name, roll number, course, semester, email and phone number.

## Objective
- To store student details in a database instead of paper registers.
- To perform basic CRUD operations (Create, Read, Update, Delete).
- To learn web development using Python, Flask and SQLite.

## Features
- Home page with navigation menu
- Add a new student
- View all students in a table
- Edit student details
- Delete a student (with confirmation)
- Search students by name or roll number
- Dashboard showing total students, total courses and recent students
- Responsive layout

## Technologies Used
| Part | Technology |
|------|------------|
| Language | Python 3 |
| Backend | Flask |
| Database | SQLite |
| Frontend | HTML, CSS (Jinja2 templates) |

## Folder Structure
```
student_management_system/
├── app.py              # Flask application (routes + database code)
├── requirements.txt    # Python dependencies
├── students.db         # SQLite database (created automatically)
├── static/
│   └── style.css       # Stylesheet
└── templates/
    ├── base.html       # Common layout (header, menu, footer)
    ├── home.html       # Home page
    ├── dashboard.html  # Dashboard
    ├── students.html   # Student list + search
    └── form.html       # Add / Edit form
```

## Database Details
Database file: `students.db` — Table: `students`

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER (Primary Key, Auto Increment) | Unique ID |
| name | TEXT | Student name |
| roll_no | TEXT (Unique) | Roll number |
| course | TEXT | Course name |
| semester | INTEGER | Semester |
| email | TEXT | Email address |
| phone | TEXT | Phone number |

## Installation Steps
1. Install Python 3 from https://www.python.org
2. Open a terminal in the project folder.
3. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux / Mac
   ```
4. Install Flask:
   ```
   pip install -r requirements.txt
   ```

## How to Run the Project
```
python app.py
```
Open your browser at **http://127.0.0.1:5000**. The database is created automatically on first run.

## Routes Summary
| URL | Purpose |
|-----|---------|
| `/` | Home |
| `/dashboard` | Dashboard |
| `/add` | Add student |
| `/students` | View / search students |
| `/edit/<id>` | Edit student |
| `/delete/<id>` | Delete student (POST) |

## Future Scope
- Admin login and authentication
- Attendance and marks management
- Export student list to PDF / Excel
- Pagination for large records
- Student photo upload
