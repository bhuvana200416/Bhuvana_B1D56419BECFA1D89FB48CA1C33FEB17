class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students = [
    Student("Gayu", "A12", 8.8),
    Student("Nandhini", "A21", 8.5),
    Student("Stells", "A27", 7.0),
    Student("Abi", "A02", 8.2),
    Student("Gayathri", "A13", 7.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")