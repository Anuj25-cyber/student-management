# Student Management System - Flask + SQLite mini project
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "college-mini-project"
DATABASE = "students.db"


def get_db():
    """Open a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # access columns by name
    return conn


def init_db():
    """Create the students table if it does not exist."""
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT NOT NULL UNIQUE,
            course TEXT NOT NULL,
            semester INTEGER NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def read_form():
    """Collect student fields from the submitted form."""
    f = request.form
    return (f["name"].strip(), f["roll_no"].strip(), f["course"].strip(),
            f["semester"], f["email"].strip(), f["phone"].strip())


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/dashboard")
def dashboard():
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) FROM students").fetchone()[0]
    courses = conn.execute("SELECT COUNT(DISTINCT course) FROM students").fetchone()[0]
    students = conn.execute("SELECT * FROM students ORDER BY id DESC LIMIT 5").fetchall()
    conn.close()
    return render_template("dashboard.html", total=total, courses=courses, students=students)


@app.route("/students")
def view_students():
    query = request.args.get("q", "").strip()
    conn = get_db()
    if query:
        students = conn.execute(
            "SELECT * FROM students WHERE name LIKE ? OR roll_no LIKE ?",
            (f"%{query}%", f"%{query}%")).fetchall()
    else:
        students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return render_template("students.html", students=students, query=query)


@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        try:
            conn = get_db()
            conn.execute("INSERT INTO students (name, roll_no, course, semester, email, phone) "
                         "VALUES (?, ?, ?, ?, ?, ?)", read_form())
            conn.commit()
            conn.close()
            flash("Student added successfully.")
            return redirect(url_for("view_students"))
        except sqlite3.IntegrityError:
            flash("Roll number already exists.")
    return render_template("form.html", student=None, title="Add Student")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    conn = get_db()
    if request.method == "POST":
        try:
            conn.execute("UPDATE students SET name=?, roll_no=?, course=?, semester=?, email=?, phone=? "
                         "WHERE id=?", read_form() + (id,))
            conn.commit()
            conn.close()
            flash("Student updated successfully.")
            return redirect(url_for("view_students"))
        except sqlite3.IntegrityError:
            flash("Roll number already exists.")
    student = conn.execute("SELECT * FROM students WHERE id=?", (id,)).fetchone()
    conn.close()
    if student is None:
        flash("Student not found.")
        return redirect(url_for("view_students"))
    return render_template("form.html", student=student, title="Edit Student")


@app.route("/delete/<int:id>", methods=["POST"])
def delete_student(id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    flash("Student deleted.")
    return redirect(url_for("view_students"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
