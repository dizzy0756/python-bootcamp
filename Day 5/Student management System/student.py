# program : a class for main.py

class Student:
    school_name = "ABC Institute"

    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display_info(self):
        print(f"School : {self.school_name}")
        print(f"Student name : {self.name}")
        print(f"Roll no : {self.roll_no}")
        for subject, mark in self.marks.items():
            print(f"{subject:<10}{mark}")
    
    def calculate_average(self):
        average = 0
        for subject, mark in self.marks.items():
            average = average + mark
        return average/len(self.marks)
    
    def get_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "F"
        
    def is_pass(self):
        average = self.calculate_average()
        if average < 40:
            return "Fail"
        else:
            return "Pass"
        