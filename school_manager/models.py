from abc import ABC, abstractmethod

class BaseUser(ABC):
    def __init__(self, national_id, first_name, last_name, age):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
class BaseModel(ABC):

    @staticmethod
    def to_str(atr):
        out_put = str()
        if len(atr) > 1:
            for item in atr:
                out_put += f',{item}'
            return out_put[1:]
        elif len(atr) == 1:
            return atr[0]
        else:
            return ''

    @abstractmethod
    def to_dict(self):
        pass
class Student(BaseUser, BaseModel):
    def __init__(self, student_id, national_id,first_name, last_name, age, grade_level, class_name):
        self.student_id = student_id
        super().__init__(national_id,first_name,last_name,age)
        self.grade_level = grade_level
        self.class_name = class_name


    def to_dict(self):
        return self.__dict__

class Teacher(BaseUser, BaseModel):
    def __init__(self, personnel_code, national_id, first_name, last_name, age, lessons, classes):
        self.personnel_code = personnel_code
        super().__init__(national_id, first_name, last_name,age)
        self.lessons = lessons
        self.classes = classes

    def to_dict(self):
        return {
            'personnel_code': self.personnel_code,
            'national_id' : self.national_id,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'age' : self.age,
            'lessons' : Teacher.to_str(self.lessons),
            'classes' : Teacher.to_str(self.classes),
        }

class Class(BaseModel):
    def __init__(self, class_id, class_name, capacity, lessons=None, students=None, teachers=None):
        self.class_id = class_id
        self.class_name = class_name
        self.capacity = capacity
        if lessons is None:
            lessons = []
        self.lessons = lessons
        if students is None:
            students = []
        self.students = students
        if teachers is None:
            teachers = []
        self.teachers = teachers

    def to_dict(self):
        return {
            'class_id' : self.class_id,
            'class_name' : self.class_name,
            'capacity' : self.capacity,
            'lessons' : Class.to_str(self.lessons),
            'students' : Class.to_str(self.students),
            'teachers' : Class.to_str(self.teachers),
        }

class Lesson(BaseModel):
    def __init__(self, lesson_id, lesson_name, units):
        self.lesson_id = lesson_id
        self.lesson_name = lesson_name
        self.units = units

    def to_dict(self):
        return self.__dict__

class ReportCard(BaseModel):
    def __init__(self, student, grades):
        self.student = student
        self.grades = grades

    def to_dict(self):
        return self.__dict__


