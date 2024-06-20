# Model
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

# View
class StudentView:
    def display_student_details(self, student):
        print("Student Details:")
        print(f"Name: {student.name}")
        print(f"Roll Number: {student.roll_number}")

# Controller
class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_student_name(self, name):
        self.model.name = name

    def get_student_name(self):
        return self.model.name

    def set_student_roll_number(self, roll_number):
        self.model.roll_number = roll_number

    def get_student_roll_number(self):
        return self.model.roll_number

    def update_view(self):
        self.view.display_student_details(self.model)

# Usage
if __name__ == "__main__":
    # Create Model
    student = Student("John Doe", "12345")

    # Create View
    view = StudentView()

    # Create Controller
    controller = StudentController(student, view)

    # Update Model data
    controller.set_student_name("Jane Smith")
    controller.set_student_roll_number("54321")

    # Update View
    controller.update_view()
