from school_manager.Validator import StudentValidator
from school_manager.storage_handler import *
from tests.samples import *
from copy import deepcopy

class Manager(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @staticmethod
    def set_to_reference(atrr1, atrr2, list1, list2):
        for obj in list1:
            value_of_atrr1 = getattr(obj, atrr1)
            for obj2 in list2:
                value_of_atrr2 = getattr(obj2, atrr2)
                if int(value_of_atrr1) == int(value_of_atrr2):
                    setattr(obj, atrr1, obj2)

    @staticmethod
    def set_to_id(atrr1, atrr2, list1, list2):
        for obj in list1:
            value_of_atrr1 = getattr(obj, atrr1)
            for obj2 in list2:
                value_of_atrr2 = getattr(obj2, atrr2)
                if value_of_atrr1.class_id == value_of_atrr2:
                    setattr(obj, atrr1, obj2.class_id)
class StudentManager(Manager):
    def __init__(self):
        self.class_list = []
        ClassFH.load_file(Class, self.class_list)
        self.student_list = []
        StudentFH.load_file(Student, self.student_list)
        Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)

    def add(self):
        student_id = input("Enter Student ID: ")
        # student_id = StudentValidator.validate_id(student_id, self.student_list, obj_type='student',is_required=True)
        if student_id is None:
            return
        national_id = input("Enter National ID: ")
        # national_id = StudentValidator.validate_id(national_id, self.student_list, obj_type='student', is_required=False, type='national')
        if national_id is None:
            return
        first_name = input("Enter First Name: ")
        # first_name = StudentValidator.validate_name(first_name, is_required=False)
        if first_name is None:
            return
        last_name = input("Enter Last Name: ")
        # last_name = StudentValidator.validate_name(last_name, is_required=True)
        if last_name is None:
            return
        age = input("Enter Age: ")
        # age = StudentValidator.validate_age(age, 10, 19, is_required=True)
        if age is None:
            return
        grade_level = input("Enter Grade Level: ")
        # grade_level = StudentValidator.validate_gl(grade_level, is_required=False)
        if grade_level is None:
            return
        class_id = input("Enter Class ID: ")
        class_id = StudentValidator.validate_cid(class_id, [int(cls.class_id) for cls in self.class_list], is_required=False)
        if class_id is None:
            return
        input('press any key to continue')
        Manager.set_to_id('class_id', 'class_id', self.student_list, self.class_list)
        self.student_list.append(
            Student(
                student_id, national_id, first_name, last_name, age, grade_level,class_id
            )
        )
        StudentFH.save_to_file(self.student_list)
        Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)
        self.set_class(student_id)

    def set_class(self, student_id):
        if '' in self.student_list[-1].class_id.students:
            self.student_list[-1].class_id.students.remove('')
        if student_id not in self.student_list[-1].class_id.students:
            self.student_list[-1].class_id.students.append(student_id)
        ClassFH.save_to_file(self.class_list)

    def edit(self):
        Manager.set_to_id('class_id', 'class_id', self.student_list, self.class_list)
        student_id = input("Enter Student ID: ")
        student = next((s for s in self.student_list if s.student_id == student_id), None)
        if student:
            print(student)
            print('*leave fields empty if you want current value*')
            fields = {
                'national_id' : input('Enter National ID: '),
                'first_name' : input('Enter First Name: '),
                'last_name' : input('Enter Last Name: '),
                'age' : input('Enter Age: '),
                'grade_level' : input('Enter Grade Level: '),
                'class_id' : input('Enter Class ID: '),
            }
            for field, value in fields.items():
                if value:
                    if field == 'class_id':
                        for cls in self.class_list:
                            if cls.class_id == student.class_id:
                                cls.students.remove(student.student_id)
                            if cls.class_id == value:
                                if '' in cls.students:
                                    cls.students.remove('')
                                cls.students.append(student.student_id)
                        ClassFH.save_to_file(self.class_list)
                    setattr(student, field, value)
            StudentFH.save_to_file(self.student_list)
            Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)

    def delete(self):
        Manager.set_to_id('class_id', 'class_id', self.student_list, self.class_list)
        student_id = input("Enter Student ID: ")
        student = next((s for s in self.student_list if s.student_id == student_id), None)
        if student:
            confirm = input(f'Are you sure to delete {student.first_name} {student.last_name} (Y/N): ').lower()
            if confirm == 'n':
                print('Canceled')
            elif confirm == 'y':
                for cls in self.class_list:
                    if cls.class_id == student.class_id:
                        cls.students.remove(student.student_id)
                self.student_list.remove(student)
                ClassFH.save_to_file(self.class_list)
                StudentFH.save_to_file(self.student_list)
                print('Student has been deleted')
            else:
                print('Invalid')
        else:
            print('Student not found')
        Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)
        return

    def search(self):
        get_fields = {
            'student_id': input('Enter Student ID: '),
            'national_id': input('Enter National ID: '),
            'first_name': input('Enter First Name: '),
            'last_name': input('Enter Last Name: '),
            'age_min': input('Enter Minimum Age: '),
            'age_max': input('Enter Maximum Age: '),
            'age': input('Enter Age: '),
            'grade_level_min': input('Enter Minimum Grade Level: '),
            'grade_level_max': input('Enter Maximum Grade Level: '),
            'class_id': input('Enter Class ID: '),
        }
        fields = {}
        for field, value in get_fields.items():
            if value:
                fields[field] = value

        Manager.set_to_id('class_id', 'class_id', self.student_list, self.class_list)
        students = deepcopy(self.student_list)
        for field, value in fields.items():
            if field.endswith('_min'):
                students = [s for s in students if int(getattr(s, field[:-4], None)) >= value]
            elif field.endswith('_max'):
                students = [s for s in students if float(getattr(s, field[:-4], None)) <= value]
            else:
                students = [s for s in students if getattr(s, field, None) == value]
        if students:
            Manager.set_to_reference('class_id', 'class_id', students, self.class_list)
            for student in students:
                print(student)
        else:
            print("No students found")
        Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)


    def show(self):
        for obj in self.student_list:
            print(obj)

class TeacherManager(Manager):
    def __init__(self):
        self.teacher_list = []
        self.class_list = []
        TeacherFH.load_file(Teacher, self.teacher_list)
        ClassFH.load_file(Class, self.class_list)

    def add(self):
        personnel_code = input("Enter Personnel Code: ")
        national_id = input("Enter National ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        age = input("Enter Age: ")
        lessons = input("Enter Lessons ID: ").split(',')
        classes = input("Enter Classes ID: ").split(',')
        self.teacher_list.append(
            Teacher(
                personnel_code, national_id, first_name, last_name, age, lessons, classes
            )
        )
        self.set_class(personnel_code)
        TeacherFH.save_to_file(self.teacher_list)

    def set_class(self, personnel_code):
        for id in self.teacher_list[-1].classes:
            for cls in self.class_list:
                if cls.class_id == id:
                    if '' in cls.teachers:
                        cls.teachers.remove('')
                    if personnel_code not in cls.teachers:
                        cls.teachers.append(personnel_code)
        ClassFH.save_to_file(self.class_list)



    def edit(self):
        personnel_code = input("Enter Personnel Code: ")
        teacher = next((t for t in self.teacher_list if personnel_code == t.personnel_code), None)
        if teacher:
            print(teacher)
            print('*leave fields empty if you want current value*')
            fields = {
                'national_id' : input('Enter National ID: '),
                'first_name' : input('Enter First Name: '),
                'last_name' : input('Enter Last Name: '),
                'age' : input('Enter Age: '),
                'lessons' : input('Enter Lessons ID: ').split(','),
                'classes' : input('Enter Classes ID: ').split(','),
            }
        for field, value in fields.items():
            if (field == 'lessons' or field == 'classes') and len(value) == 1 and value[0] == '':
                value = ''
            if value:
                if field == 'classes':
                    for cls in self.class_list:
                        for id in teacher.classes:
                            if cls.class_id == id:
                                cls.teachers.remove(personnel_code)
                        for id in value:
                            if cls.class_id == id:
                                if '' in cls.teachers:
                                    cls.teachers.remove('')
                                cls.teachers.append(personnel_code)
                        ClassFH.save_to_file(self.class_list)
                setattr(teacher, field, value)
        print(teacher)
        TeacherFH.save_to_file(self.teacher_list)

    def delete(self):
        personnel_code = input("Enter Personnel Code: ")
        teacher = next((t for t in self.teacher_list if personnel_code == t.personnel_code), None)
        if teacher:
            confirm = input(f'Are you sure to delete {teacher.first_name} {teacher.last_name} (Y/N): ').lower()
            if confirm == 'n':
                print('Canceled')
            elif confirm == 'y':
                for cls in self.class_list:
                    for id in teacher.classes:
                        if cls.class_id == id:
                            cls.teachers.remove(personnel_code)
                self.teacher_list.remove(teacher)
                ClassFH.save_to_file(self.class_list)
                TeacherFH.save_to_file(self.teacher_list)
                print('Teacher has been deleted')
            else:
                print('Invalid')
        else:
            print('Teacher not found')
        return

    def search(self):
        get_fields = {
            'personnel_code': input('Enter Personnel Code: '),
            'national_id': input('Enter National ID: '),
            'first_name': input('Enter First Name: '),
            'last_name': input('Enter Last Name: '),
            'age_min': input('Enter Minimum Age: '),
            'age_max': input('Enter Maximum Age: '),
            'age': input('Enter Age: '),
            'lessons': input('Enter Lessons ID: '),
            'classes': input('Enter Classes ID: '),
        }
        fields = {}
        for field, value in get_fields.items():
            if value:
                fields[field] = value
        teachers = deepcopy(self.teacher_list)
        for field, value in fields.items():
            if field.endswith('_min'):
                teachers = [t for t in teachers if float(getattr(t, field[:-4], None)) >= value]
            elif field.endswith('_max'):
                teachers = [t for t in teachers if float(getattr(t, field[:-4], None)) <= value]
            elif field == 'lessons' or field == 'classes':
                lists = []
                for t in teachers:
                    items = getattr(t, field)
                    found = False
                    for i in items:
                        if i == value:
                            found = True
                    if not found:
                        lists.append(t)
                for i in lists:
                    teachers.remove(i)
            else:
                teachers = [t for t in teachers if getattr(t, field, None) == value]
        if teachers:
            for teacher in teachers:
                print(teacher)
        else:
            print("No Teacher found")

    def show(self):
        for obj in self.teacher_list:
            print(obj)

class ClassManager(Manager):
    def __init__(self):
        self.class_list = []
        ClassFH.load_file(Class, self.class_list)
        self.set_students()
        self.set_teachers()
    def add(self):
        class_id = input("Enter Class ID: ")
        class_name = input("Enter Class Name: ")
        capacity = input("Enter Class Capacity: ")
        self.class_list.append(
            Class(
                class_id, class_name, capacity
            )
        )
        ClassFH.save_to_file(self.class_list)
    def set_students(self):
        students_list = []
        StudentFH.load_file(Student, students_list)
        Manager.set_to_reference('class_id', 'class_id', students_list, self.class_list)

        for student in students_list:
            for cls in self.class_list:
                if '' in cls.students:
                    cls.students.remove('')
                if cls.class_id == student.class_id.class_id:
                    if student.student_id not in cls.students:
                        cls.students.append(student.student_id)
        ClassFH.save_to_file(self.class_list)

    def set_teachers(self):
        teachers_list = []
        TeacherFH.load_file(Teacher, teachers_list)

        for teacher in teachers_list:
            for t in teacher.classes:
                for cls in self.class_list:
                    if '' in cls.teachers:
                        cls.teachers.remove('')
                    if cls.class_id == t:
                        if teacher.personnel_code not in cls.teachers:
                            cls.teachers.append(teacher.personnel_code)
        ClassFH.save_to_file(self.class_list)

    def edit(self):
        class_id = input("Enter Class ID: ")
        cls = next((c for c in self.class_list if class_id == c.class_id), None)
        if cls:
            print(cls)
            print('*leave fields empty if you want current value*')
            fields = {
                'class_name' : input('Enter Class Name: '),
                'capacity' : input('Enter Class Capacity: '),
            }
            for field, value in fields.items():
                if value:
                    setattr(cls, field, value)
                    ClassFH.save_to_file(self.class_list)
        else:
            print('No Class found')

    def delete(self):
        class_id = input("Enter Class ID: ")
        cls = next((c for c in self.class_list if class_id == c.class_id), None)

        if cls:
            confirm = input(f'Are you sure to delete {cls.class_name}  (Y/N): ').lower()
            if confirm == 'n':
                print('Canceled')
            elif confirm == 'y':
                self.class_list.remove(cls)
                ClassFH.save_to_file(self.class_list)
                print('Class has been deleted')
            else:
                print('Invalid input')
        else:
            print('No Class found')

    def search(self):
        get_fields = {
            'class_id' : input('Enter Class ID: '),
            'class_name' : input('Enter Class Name: '),
            'capacity_min' : input('Enter Minimum Capacity: '),
            'capacity_max' : input('Enter Maximum Capacity: '),
            'capacity' : input('Enter Capacity: '),
        }
        fields = {}
        for field, value in get_fields.items():
            if value:
                fields[field] = value
        classes = deepcopy(self.class_list)
        for field, value in fields.items():
            if field.endswith('_min'):
                classes = [c for c in classes if int(getattr(c, field[:-4], None)) >= value]
            elif field.endswith('_max'):
                classes = [c for c in classes if float(getattr(c, field[:-4], None)) <= value]
            else:
                classes = [c for c in classes if getattr(c, field, None) == value]
        if classes:
            for cls in classes:
                print(cls)
        else:
            print("No Class found")

    def show(self):
        for obj in self.class_list:
            print(obj)

    def show_students(self):
        class_id = input("Enter Class ID: ")
        cls = next((c for c in self.class_list if class_id == c.class_id), None)

        if cls:
            students_list = []
            StudentFH.load_file(Student, students_list)
            Manager.set_to_reference('class_id', 'class_id', students_list, self.class_list)
            have = False
            print('-' * 20)
            for student_id in cls.students:
                for std in students_list:
                    if student_id == std.student_id:
                        print(f'- {std.first_name} {std.last_name}')
                        have = True
            if not have:
                print('\tEmpty')
            print('-' * 20)
        else:
            print('No Class found')

    def show_teachers(self):
        class_id = input("Enter Class ID: ")
        cls = next((c for c in self.class_list if class_id == c.class_id), None)

        if cls:
            teachers_list = []
            TeacherFH.load_file(Teacher, teachers_list)
            have = False
            print('-' * 20)
            for personnel_code in cls.teachers:
                for teacher in teachers_list:
                    if teacher.personnel_code == personnel_code:
                        print(f'- {teacher.first_name} {teacher.last_name}')
                        have = True
            if not have:
                print('\tEmpty')
            print('-' * 20)
        else:
            print('No Class found')

class LessonManager(Manager):
    def __init__(self):
        self.lesson_list = []
        LessonFH.load_file(Lesson, self.lesson_list)

    def add(self):
        lesson_id = input("Enter Lesson ID: ")
        lesson_name = input("Enter Lesson Name: ")
        units = input("Enter Units: ")
        self.lesson_list.append(
            Lesson(lesson_id, lesson_name, units)
        )
        LessonFH.save_to_file(self.lesson_list)
    def edit(self):
        lesson_id = input("Enter Lesson ID: ")
        lesson = next((l for l in self.lesson_list if l.lesson_id == lesson_id), None)
        if lesson:
            print(lesson)
            print('*leave fields empty if you want current value*')
            fields = {
                'lesson_name' : input('Enter Lesson Name: '),
                'units' : input('Enter Units: ')
            }
            for field, value in fields.items():
                if value:
                    setattr(lesson, field, value)
                    LessonFH.save_to_file(self.lesson_list)
        else:
            print('No Lesson found')

    def delete(self):
        lesson_id = input("Enter Lesson ID: ")
        lesson = next((l for l in self.lesson_list if l.lesson_id == lesson_id), None)
        if lesson:
            confirm = input(f'Are you sure to delete {lesson.lesson_name}  (Y/N): ').lower()
            if confirm == 'n':
                print('Canceled')
            elif confirm == 'y':
                self.lesson_list.remove(lesson)
                LessonFH.save_to_file(self.lesson_list)
                print('Lesson has been deleted')
            else:
                print('Invalid input')
        else:
            print('No Lesson found')

    def search(self):
        get_fields = {
            'lesson_id' : input('Enter Lesson ID: '),
            'lesson_name' : input('Enter Lesson Name: '),
            'units_min' : input('Enter Minimum Units: '),
            'units_max' : input('Enter Maximum Units: '),
            'units' : input('Enter Units: ')
        }
        fields = {}
        for field, value in get_fields.items():
            if value:
                fields[field] = value
        lessons = deepcopy(self.lesson_list)
        for field, value in fields.items():
            if field.endswith('_min'):
                classes = [l for l in lessons if float(getattr(l, field[:-4], None)) >= value]
            elif field.endswith('_max'):
                classes = [l for l in lessons if float(getattr(l, field[:-4], None)) <= value]
            else:
                classes = [l for l in lessons if getattr(l, field, None) == value]
        if lessons:
            for lesson in lessons:
                print(lesson)
        else:
            print("No Lesson found")

    def show(self):
        for obj in self.lesson_list:
            print(obj)

class ReportCardManager(Manager):
    def __init__(self):
        self.rc_list = []
        self._students_list = []
        self._class_list = []
        self._teachers_list = []
        self._lessons_list = []
        # Manager.set_to_id('class_id', 'class_id', self._students_list, self._class_list)
        ReportCardFH.load_file(ReportCard, self.rc_list)
        StudentFH.load_file(Student, self._students_list)
        ClassFH.load_file(Class, self._class_list)
        TeacherFH.load_file(Teacher, self._teachers_list)
        LessonFH.load_file(Lesson, self._lessons_list)

    def add(self):
        student_id = input("Enter Student ID: ")
        student = next((s for s in self._students_list if s.student_id == student_id), None)
        if student:
            lessons_id = []
            lessons = []
            grades = []
            students_class = next((c for c in self._class_list if student.class_id == c.class_id), None)
            for personnel_code in students_class.teachers:
                for teacher in self._teachers_list:
                    if teacher.personnel_code == personnel_code:
                        lessons_id.append(teacher.lessons[0])
            if lessons_id:
                for lesson_id in lessons_id:
                    for lesson in self._lessons_list:
                        if lesson.lesson_id == lesson_id:
                            lessons.append(lesson)
            for lesson in lessons:
                grade = input(f"Enter {lesson.lesson_name}'s Grade: ")
                grades.append(grade)

            self.rc_list.append(
                ReportCard(
                    student_id,grades
                )
            )
            ReportCardFH.save_to_file(self.rc_list)

    def edit(self):
        pass

    def delete(self):
        student_id = input("Enter Student ID: ")
        student = next((s for s in self._students_list if s.student_id == student_id), None)
        rc = next((rc for rc in self.rc_list if rc.student == student_id), None)
        if student and rc:
            confirm = input(f'Are you sure to delete {student.first_name} {student.last_name}\'s Report Card  (Y/N): ').lower()
            if confirm == 'n':
                print('Canceled')
            elif confirm == 'y':
                self.rc_list.remove(rc)
                ReportCardFH.save_to_file(self.rc_list)
                print('Report Card has been deleted')
            else:
                print('Invalid input')
        else:
            print('No Report Card found')

    def search(self):
        pass

    def show(self):
        student_id = input("Enter Student ID: ")
        student = next((s for s in self._students_list if s.student_id == student_id), None)
        if student:
            lessons_id = []
            lessons = []
            grades = []
            students_class = next((c for c in self._class_list if student.class_id == c.class_id), None)
            for personnel_code in students_class.teachers:
                for teacher in self._teachers_list:
                    if teacher.personnel_code == personnel_code:
                        lessons_id.append(teacher.lessons[0])
            if lessons_id:
                for lesson_id in lessons_id:
                    for lesson in self._lessons_list:
                        if lesson.lesson_id == lesson_id:
                            lessons.append(lesson)
            for rc in self.rc_list:
                if rc.student == student_id:
                    grades = rc.grades
            for lesson,grade in zip(lessons, grades):
                print(f"{lesson.lesson_name}'s Grade: {grade}")