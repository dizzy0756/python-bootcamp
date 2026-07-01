import requests
from model.student import Student

url = "http://127.0.0.1:5000/students"

def add_student():
    name = input("Enter student name: ")
    id = int(input("Enter student id: "))
    course = input("Enter student course: ")
    age = int(input("Enter student age: "))
    student = Student(id,name,course,age)
    response = requests.post(url, json=student.to_dict())
    print(response.json())

def update_student(id):
    url1 = f"http://127.0.0.1:5000/students/{id}"
    name = input("Enter updated student name: ")
    course = input("Enter updated student course: ")
    age = int(input("Enter updated student age: "))
    student = Student(id,name,course,age)
    response = requests.put(url1, json=student.to_dict())
    print(response.status_code)

def delete_student(id):
    url1 = f"http://127.0.0.1:5000/students/{id}"
    response = requests.delete(url1)
    print(response.json())

def search_student(id):
    url1 = f"http://127.0.0.1:5000/students/{id}"
    response = requests.get(url1)
    print(response.json())

def view_students():
    response = requests.get(url)
    print(response.json())

if __name__ == "__main__":
    while True:
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. View Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            id = int(input("Enter student id to update: "))
            update_student(id)
        elif choice == "3":
            id = int(input("Enter student id to delete: "))
            delete_student(id)
        elif choice == "4":
            id = int(input("Enter student id to search: "))
            search_student(id)
        elif choice == "5":
            view_students()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")