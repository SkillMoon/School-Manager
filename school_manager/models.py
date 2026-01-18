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
    def __init__(self, student_id, national_id,first_name, last_name, age, grade_level, class_id):
        self.student_id = student_id
        super().__init__(national_id,first_name,last_name,age)
        self.grade_level = grade_level
        self.class_id = class_id


    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return (f'- Student : {self.student_id}\n Name : {self.first_name} {self.last_name}  |  '
                f'National ID : {self.national_id}  |  Age : {self.age}  |  Grade Level : {self.grade_level}  |  Class : {self.class_id.class_name}')

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

    def __str__(self):
        return (f'- Teacher : {self.personnel_code}\n Name : {self.first_name} {self.last_name}  |  '
                f'National ID : {self.national_id}  |  Age : {self.age}  |  Lessons : {Teacher.to_str(self.lessons)}  |  Class : {Teacher.to_str(self.classes)}')

class Class(BaseModel):
    def __init__(self, class_id, class_name, capacity, students=None, teachers=None):
        self.class_id = class_id
        self.class_name = class_name
        self.capacity = capacity
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
            'students' : Class.to_str(self.students),
            'teachers' : Class.to_str(self.teachers),
        }

    def __str__(self):
        return f'- Class : {self.class_id}\n Name : {self.class_name}  |  Capacity : {self.capacity}  | Students : {len(self.students)} | Teachers : {len(self.teachers)}'

class Lesson(BaseModel):
    def __init__(self, lesson_id, lesson_name, units):
        self.lesson_id = lesson_id
        self.lesson_name = lesson_name
        self.units = units

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f'- Lesson {self.lesson_id}\n Name : {self.lesson_name}  |  Units : {self.units}'

class ReportCard(BaseModel):
    def __init__(self, student, grades):
        self.student = student
        self.grades = grades

    def to_dict(self):
        return {
            'student' : self.student,
            'grades' : ReportCard.to_str(self.grades),
        }


