import sqlite3
from model.student import Student

with sqlite3.connect("student_collection.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   course TEXT NOT NULL,
                   age INT NOT NULL
                   )
    """)

def add(student):
    with sqlite3.connect("student_collection.db") as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students(id, name, course, age) VALUES(?, ?, ?, ?)",
                       student.to_tuple(),
                       )

def update(student):
    with sqlite3.connect("student_collection.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
                       UPDATE students
                       SET name = ?,
                       course = ?,
                       age = ?
                       WHERE id = ?
                       """,
                       (student.name, student.course, student.age, student.id)
                       )
        return cursor.rowcount
        
def delete(id):
    with sqlite3.connect("student_collection.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?",
                       (id,)
                       )
        return cursor.rowcount
        
def search(id):
    with sqlite3.connect("student_collection.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?",
                       (id,)
                       )
        result = cursor.fetchone()
        return result
        
def view():
    with sqlite3.connect("student_collection.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        return rows

if __name__ == "__main__":
    print("Database testing....")
    # name = "Jonita"
    # id = 2
    # course = "Bakery"
    # age = 19
    # student = Student(id,name,course,age)
    # add(student)
    rows = view()
    print(rows)