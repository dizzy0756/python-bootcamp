# Student Management System (OOP Edition)


from student import Student

name = input("Enter name of the student : ")

roll_no = input("Enter the roll no. of the student : ")

subjects = []
for i in range(3):
    subject = input(f"Enter the name of subject {i} : ")
    subjects.append(subject)
marks = {}
for sub in subjects:
    while True:
        try:
            marks[sub] = int(input(f"Enter the marks obtained in {sub} : "))
            break
        except ValueError:
            print("Enter a valid natural number")
            
s1 = Student(name,roll_no,marks)

grade = s1.get_grade()
status = s1.is_pass()
s1.display_info()
print(f"Grade : {grade}")
print(f"Status : {status}")