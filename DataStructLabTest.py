import Student
import Students
import string


def __main__():
    in_file = open("student.txt", encoding="utf-8")
    
    list = Students.Students(10)

    for line in in_file:
        if not line:
            break
        else:
            student_data = line.split()
        if student_data:
            number = int(student_data[0])
            name = str(student_data[1])
            gpa = float(student_data[2])

        new_student = Student.Student(number, gpa, name)
        added = list.add(new_student)
        if not added:
            print("Cannot add ", new_student.student_name, "| Unhandled collision or array full")

    print(list)

__main__()