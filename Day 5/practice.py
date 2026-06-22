# this is a program that creates an object of class Student which takes 3 subject names and marks as parameter and the class has a method to calculate the average marks.


class Student:
    def __init__(self,subject_names,marks):
        self.subject_names = subject_names
        self.marks = marks
    def avg(self):
        return sum(self.marks)/3

def get_sub_names():
    sub_name = []
    for i in range(3):
        s_name = input(f"Enter of the name of subject {i+1} : ")
        sub_name.append(s_name)
    return sub_name

def get_marks():
    marks = []
    for i in range(3):
        mark = int(input(f"Enter the marks obtained in subject {i+1} : "))
        marks.append(mark)
    return marks

sub_name = get_sub_names()
marks = get_marks()

s1 = Student(sub_name,marks)
print(s1.avg())