class Student:
    """ 
        This is a Student. It has a name, student number, and GPA
    """
    def __init__(self, number, gpa, name):
        self.student_number = number;
        self.student_gpa = gpa
        self.student_name = name

    def setName(self, name):
        self.student_name = name

    def setGPA(self, gpa):
        self.student_gpa = gpa

    def setNumber(self, number):
        self.student_number = number

    def __str__(self):
        out = self.student_name + " - " + str(self.student_number) + " has GPA " + str(self.student_gpa)
        return out