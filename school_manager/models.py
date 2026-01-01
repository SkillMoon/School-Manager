from abc import ABC

class BaseUser(ABC):
    def __init__(self, national_id, first_name, last_name, age):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Student(BaseUser):
    def __init__(self, student_id, national_id,first_name, last_name, age, grade_level, class_name, report_card):
        self.student_id = student_id
        super().__init__(national_id,first_name,last_name,age)
        self.grade_level = grade_level
        self.class_name = class_name
        self.report_card = report_card

class Teacher(BaseUser):
    def __init__(self, personnel_code, national_id, first_name, last_name, age, lessons, classes):
        self.personnel_code = personnel_code
        super().__init__(national_id, first_name, last_name,age)
        self.lessons = lessons
        self.classes = classes

class Class:
    def __init__(self, class_id, class_name, capacity, students, lessons, teachers):
        self.class_id = class_id
        self.class_name = class_name
        self.capacity = capacity
        self.students = students
        self.lessons = lessons
        self.teachers = teachers

class Lesson:
    def __init__(self, lesson_id, lesson_name, units, teachers):
        self.lesson_id = lesson_id
        self.lesson_name = lesson_name
        self.units = units

class ReportCard:
    def __init__(self, student, grades):
        self.student = student
        self.grades = grades