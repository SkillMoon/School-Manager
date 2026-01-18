from abc import ABC, abstractmethod
from csv import DictWriter, DictReader




class FileHandler(ABC):

    @staticmethod
    @abstractmethod
    def load_file():
        pass

    @staticmethod
    @abstractmethod
    def save_to_file():
        pass
class StudentFH(FileHandler):

    @staticmethod
    def load_file(cls, student_list):
        with open('data/students.csv', newline='') as file:
            reader = DictReader(file)
            for row in reader:
                student_list.append(
                cls(
                    row['student_id'],
                    row['national_id'],
                    row['first_name'],
                    row['last_name'],
                    row['age'],
                    row['grade_level'],
                    row['class_id'],
                    )
                )

    @staticmethod
    def save_to_file(student_list):
        with open('data/students.csv', 'w', newline='') as file:
            headers = ['student_id', 'national_id', 'first_name','last_name', 'age', 'grade_level', 'class_id']
            writer = DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for student in student_list:
                writer.writerow(student.__dict__)

class TeacherFH(FileHandler):

    @staticmethod
    def load_file(cls, teacher_list):
        with open('data/teachers.csv', newline='') as file:
            reader = DictReader(file)
            for row in reader:
                teacher_list.append(
                cls(
                    row['personnel_code'],
                    row['national_id'],
                    row['first_name'],
                    row['last_name'],
                    row['age'],
                    row['lessons'].split(','),
                    row['classes'].split(','),
                    )
                )

    @staticmethod
    def save_to_file(teacher_list):
        with open('data/teachers.csv', 'w', newline='') as file:
            headers = ['personnel_code', 'national_id', 'first_name','last_name', 'age', 'lessons', 'classes']
            writer = DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for teacher in teacher_list:
                writer.writerow(teacher.to_dict())

class ClassFH(FileHandler):

    @staticmethod
    def load_file(cls, class_list):
        with open('data/classes.csv', newline='') as file:
            reader = DictReader(file)
            for row in reader:
                class_list.append(
                cls(
                    row['class_id'],
                    row['class_name'],
                    row['capacity'],
                    row['students'].split(','),
                    row['teachers'].split(',')
                    )
                )

    @staticmethod
    def save_to_file(class_list):
        with open('data/classes.csv', 'w', newline='') as file:
            headers = ['class_id', 'class_name', 'capacity', 'students', 'teachers']
            writer = DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for item in class_list:
                writer.writerow(item.to_dict())

class LessonFH(FileHandler):
    @staticmethod
    def load_file(cls, lesson_list):
        with open('data/lessons.csv', newline='') as file:
            reader = DictReader(file)
            for row in reader:
                lesson_list.append(
                cls(
                    row['lesson_id'],
                    row['lesson_name'],
                    row['units'],
                    )
                )

    @staticmethod
    def save_to_file(lesson_list):
        with open('data/lessons.csv', 'w', newline='') as file:
            headers = ['lesson_id', 'lesson_name', 'units']
            writer = DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for item in lesson_list:
                writer.writerow(item.to_dict())

class ReportCardFH(FileHandler):
    @staticmethod
    def load_file(cls, rc_list):
        with open('data/report_card.csv', newline='') as file:
            reader = DictReader(file)
            for row in reader:
                rc_list.append(
                cls(
                    row['student'],
                    row['grades'].split(','),
                    )
                )

    @staticmethod
    def save_to_file(rc_list):
        with open('data/report_card.csv', 'w', newline='') as file:
            headers = ['student', 'grades']
            writer = DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for rc in rc_list:
                writer.writerow(rc.to_dict())