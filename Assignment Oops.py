
# Exercise1
# Build a program to manage a university's course catalog.
# You want to define a base class Course that has the following properties
# course_code, course_name , credit_hours
# You also want to define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class.

#University's Course Catalog
class Course:

    def __init__(self,course_code,course_name,credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"{self.course_code} : {self.course_name}  ({self.credit_hours} Credit hours)"

class Corecourse(Course):
    def __init__(self,course_code,course_name, credit_hours,required_for_major):
        super().__init__(course_code,course_name,credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        return super().__str__()  +  f"Required_for_major:{self.required_for_major}"

class Elective_course(Course):
    def __init__(self,course_code , course_name , credit_hours , elective_type):
        super().__init__(course_code,course_name,credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return super().__str__()  +  f"elective type:{self.elective_type}"

course1 = Course("CS201","Calculus",2)
course2 = Corecourse("CS301","Introduction to computer science",3, True)
course3 = Elective_course("CS401","Data Structures",4 , "Technical")

print(course1)
print(course2)
print(course3)

# Exercise2
#  Create a Python module named employee that contains a class Employee with attributes name, salary and methods get_name() and get_salary().
#  Write a program to use this module to create an object of the Employee class and display its name and salary.
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary =salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

emp = Employee("John Doe",5000)

print(f"Name: {emp.get_name()}")
print(f"Salary: {emp.get_salary()}")