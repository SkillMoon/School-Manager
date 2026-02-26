from school_manager.validator import StudentValidator, TeacherValidator, ClassValidator, LessonValidator, RCValidator
from school_manager.storage_handler import *
from school_manager.models import *
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
    def set_to_reference(attr1, attr2, list1, list2):
        for obj in list1:
            value_of_attr1 = getattr(obj, attr1)
            for obj2 in list2:
                value_of_attr2 = getattr(obj2, attr2)
                if int(value_of_attr1) == int(value_of_attr2):
                    setattr(obj, attr1, obj2)

    @staticmethod
    def set_to_id(attr1, attr2, list1, list2):
        for obj in list1:
            value_of_attr1 = getattr(obj, attr1)
            for obj2 in list2:
                value_of_attr2 = getattr(obj2, attr2)
                if value_of_attr1.class_id == value_of_attr2:
                    setattr(obj, attr1, obj2.class_id)
class StudentManager(Manager):
    def __init__(self):
        self.class_list = []
        ClassFH.load_file(Class, self.class_list)
        self.student_list = []
        StudentFH.load_file(Student, self.student_list)
        Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)

    def add(self):
        print("--Add Student")
        student_id = input("-Enter Student ID: ")
        student_id = StudentValidator.validate_id(student_id, self.student_list, obj_type='student',is_required=True, is_key=True)
        if student_id is None:
            input('Press ENTER to continue...')
            return
        national_id = input("-Enter National ID: ")
        national_id = StudentValidator.validate_id(national_id, self.student_list, obj_type='student', is_required=False, type='national')
        if national_id is None:
            input('Press ENTER to continue...')
            return
        first_name = input("-Enter First Name: ")
        first_name = StudentValidator.validate_name(first_name, is_required=False)
        if first_name is None:
            input('Press ENTER to continue...')
            return
        last_name = input("-Enter Last Name: ")
        last_name = StudentValidator.validate_name(last_name, is_required=True)
        if last_name is None:
            input('Press ENTER to continue...')
            return
        age = input("-Enter Age: ")
        age = StudentValidator.validate_age(age, 10, 19, is_required=True)
        if age is None:
            input('Press ENTER to continue...')
            return
        grade_level = input("-Enter Grade Level: ")
        grade_level = StudentValidator.validate_gl(grade_level, is_required=True)
        if grade_level is None:
            input('Press ENTER to continue...')
            return
        class_id = input("-Enter Class ID: ")
        class_id = StudentValidator.validate_cid(class_id, [int(cls.class_id) for cls in self.class_list], is_required=True)
        if class_id is None:
            input('Press ENTER to continue...')
            return
        input('press ENTER to continue...')
        Manager.set_to_id('class_id', 'class_id', self.student_list, self.class_list)
        self.student_list.append(
            Student(
                student_id, national_id, first_name, last_name, age, grade_level,class_id
            )
        )
        StudentFH.save_to_file(self.student_list)
        Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)
        self.set_class(student_id)
        print('[SYSTEM] Student has been added successfully.')
        input('press ENTER to continue...')
        return

    def set_class(self, student_id):
        if '' in self.student_list[-1].class_id.students:
            self.student_list[-1].class_id.students.remove('')
        if student_id not in self.student_list[-1].class_id.students:
            self.student_list[-1].class_id.students.append(student_id)
        ClassFH.save_to_file(self.class_list)

    def edit(self):
        print("--Edit Student")
        Manager.set_to_id('class_id', 'class_id', self.student_list, self.class_list)
        student_id = input("-Enter Student ID: ")
        student_id = StudentValidator.validate_id(student_id, self.student_list, obj_type='student', is_required=True, is_key=False)
        if student_id is None:
            input('Press ENTER to continue...')
            return
        student = next((s for s in self.student_list if int(s.student_id) == student_id), None)
        if student:
            Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)
            print('-' * 20)
            print(student)
            Manager.set_to_id('class_id', 'class_id', self.student_list, self.class_list)
            print('*leave fields empty if you want current value*')
            national_id = StudentValidator.validate_id(input('-Enter National ID: '), self.student_list, obj_type='student', is_required=False, is_key=False, type='national')
            if national_id is None:
                input('Press ENTER to continue...')
                return
            first_name = StudentValidator.validate_name(input('-Enter First Name: '))
            if first_name is None:
                input('Press ENTER to continue...')
                return
            last_name = StudentValidator.validate_name(input('-Enter Last Name: '))
            if last_name is None:
                input('Press ENTER to continue...')
                return
            age = StudentValidator.validate_age(input('-Enter Age: '), 10, 19)
            if age is None:
                input('Press ENTER to continue...')
                return
            grade_level = StudentValidator.validate_gl(input('-Enter Grade Level: '))
            if grade_level is None:
                input('Press ENTER to continue...')
                return
            class_id = StudentValidator.validate_cid(input('-Enter Class ID: '), self.class_list)
            if class_id is None:
                input('Press ENTER to continue...')
                return
            fields = {
                'national_id' : national_id,
                'first_name' : first_name,
                'last_name' : last_name,
                'age' : age,
                'grade_level' : grade_level,
                'class_id' : class_id,
            }
            is_changed = False
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
                    is_changed = True

            if is_changed:
                print('[SYSTEM] Student has been edited.')
                input('press ENTER to continue...')
            else:
                print('[SYSTEM] Nothing has been changed.')
                input('press ENTER to continue...')

            StudentFH.save_to_file(self.student_list)
            Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)
        else:
            print('[SYSTEM] Student not found.')
            input('press ENTER to continue...')
        return

    def delete(self):
        print("--Delete Student")
        Manager.set_to_id('class_id', 'class_id', self.student_list, self.class_list)
        student_id = input("-Enter Student ID: ")
        student_id = StudentValidator.validate_id(student_id, self.student_list, obj_type='student', is_required=True, is_key=False)
        if student_id is None:
            input('Press ENTER to continue...')
            return
        student = next((s for s in self.student_list if s.student_id == student_id), None)
        if student:
            confirm = input(f'[SYSTEM] Are you sure to delete {student.first_name} {student.last_name} (Y/N): ').lower()
            if confirm == 'n':
                print('[SYSTEM] Canceled.')
                input('press ENTER to continue...')
            elif confirm == 'y':
                for cls in self.class_list:
                    if cls.class_id == student.class_id:
                        cls.students.remove(student.student_id)
                self.student_list.remove(student)
                ClassFH.save_to_file(self.class_list)
                StudentFH.save_to_file(self.student_list)
                print('[SYSTEM] Student has been deleted.')
                input('press ENTER to continue...')
            else:
                print('[ERROR] Invalid Input.')
                input('press ENTER to continue...')
        else:
            print('[SYSTEM] Student not found.')
            input('press ENTER to continue...')
        Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)
        return

    def search(self):
        print("--Search Student")
        get_fields = {
            'student_id': input('-Enter Student ID: '),
            'national_id': input('-Enter National ID: '),
            'first_name': input('-Enter First Name: '),
            'last_name': input('-Enter Last Name: '),
            'age_min': input('-Enter Minimum Age: '),
            'age_max': input('-Enter Maximum Age: '),
            'age': input('-Enter Age: '),
            'grade_level_min': input('-Enter Minimum Grade Level: '),
            'grade_level_max': input('-Enter Maximum Grade Level: '),
            'class_id': input('-Enter Class ID: '),
        }
        fields = {}
        for field, value in get_fields.items():
            if value:
                fields[field] = value

        Manager.set_to_id('class_id', 'class_id', self.student_list, self.class_list)
        students = deepcopy(self.student_list)
        for field, value in fields.items():
            if field.endswith('_min'):
                students = [s for s in students if float(getattr(s, field[:-4], None)) >= float(value)]
            elif field.endswith('_max'):
                students = [s for s in students if float(getattr(s, field[:-4], None)) <= float(value)]
            else:
                students = [s for s in students if getattr(s, field, None) == value]
        if students:
            Manager.set_to_reference('class_id', 'class_id', students, self.class_list)
            print('---Students' + '-'* 100)
            for student in students:
                print(student)
            print('-' * 100)
            input('press ENTER to continue...')

        else:
            print("[SYSTEM] No student found.")
            input('press ENTER to continue...')

        Manager.set_to_reference('class_id', 'class_id', self.student_list, self.class_list)
        return


    def show(self):
        print('---Students' + '-'* 100)
        for obj in self.student_list:
            print(obj)
        print('-' * 110)
        input('press ENTER to continue...')
        return 

class TeacherManager(Manager):
    def __init__(self):
        self.teacher_list = []
        self.class_list = []
        self.lesson_list = []
        TeacherFH.load_file(Teacher, self.teacher_list)
        ClassFH.load_file(Class, self.class_list)
        LessonFH.load_file(Lesson, self.lesson_list)

    def add(self):
        print("--Add Teacher")
        personnel_code = input("-Enter Personnel Code: ")
        personnel_code = TeacherValidator.validate_id(personnel_code, self.teacher_list, 'teacher', is_required=True, is_key=True)
        if personnel_code is None:
            input('Press ENTER to continue...')
            return
        national_id = input("-Enter National ID: ")
        national_id = TeacherValidator.validate_id(national_id, self.teacher_list, 'teacher', is_required=True, type='national')
        if national_id is None:
            input('Press ENTER to continue...')
            return
        first_name = input("-Enter First Name: ")
        first_name = TeacherValidator.validate_name(first_name, is_required=True)
        if first_name is None:
            input('Press ENTER to continue...')
            return
        last_name = input("-Enter Last Name: ")
        last_name = TeacherValidator.validate_name(last_name, is_required=True)
        if last_name is None:
            input('Press ENTER to continue...')
            return
        age = input("-Enter Age: ")
        age = TeacherValidator.validate_age(age, 25, 50, is_required=True)
        if age is None:
            input('Press ENTER to continue...')
            return
        lessons = input("-Enter Lessons ID: ").split(',')
        lessons = TeacherValidator.validate_lid(lessons, [int(lsn.lesson_id) for lsn in self.lesson_list], is_required=True)
        if lessons is None:
            input('Press ENTER to continue...')
            return
        classes = input("-Enter Classes ID: ").split(',')
        classes = TeacherValidator.validate_cid(classes, [int(cls.class_id) for cls in self.class_list], is_required=True)
        if classes is None:
            input('Press ENTER to continue...')
            return
        self.teacher_list.append(
            Teacher(
                personnel_code, national_id, first_name, last_name, age, lessons, classes
            )
        )
        self.set_class(personnel_code)
        TeacherFH.save_to_file(self.teacher_list)
        print('[SYSTEM] Teacher has been added successfully.')
        input('press ENTER to continue...')

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
        print("--Edit Teacher")
        personnel_code = input("-Enter Personnel Code: ")
        personnel_code = TeacherValidator.validate_id(personnel_code, self.teacher_list, 'teacher', is_required=True, is_key=False)
        if personnel_code is None:
            input('Press ENTER to continue...')
            return
        teacher = next((t for t in self.teacher_list if personnel_code == int(t.personnel_code)), None)
        if teacher:
            print('-' * 20)
            print(teacher)
            print('*leave fields empty if you want current value*')
            national_id = input("-Enter National ID: ")
            national_id = TeacherValidator.validate_id(national_id, self.teacher_list, 'teacher', is_required=False, type='national')
            if national_id is None:
                input('Press ENTER to continue...')
                return
            first_name = input("-Enter First Name: ")
            first_name = TeacherValidator.validate_name(first_name, is_required=False)
            if first_name is None:
                input('Press ENTER to continue...')
                return
            last_name = input("-Enter Last Name: ")
            last_name = TeacherValidator.validate_name(last_name, is_required=False)
            if last_name is None:
                input('Press ENTER to continue...')
                return
            age = input("-Enter Age: ")
            age = TeacherValidator.validate_age(age, 25, 50, is_required=False)
            if age is None:
                input('Press ENTER to continue...')
                return
            lessons = input("-Enter Lessons ID: ").split(',')
            lessons = TeacherValidator.validate_lid(lessons, [int(lsn.lesson_id) for lsn in self.lesson_list], is_required=False)
            if lessons is None:
                input('Press ENTER to continue...')
                return
            classes = input("-Enter Classes ID: ").split(',')
            classes = TeacherValidator.validate_cid(classes, [int(cls.class_id) for cls in self.class_list], is_required=False)
            if classes is None:
                input('Press ENTER to continue...')
                return
            fields = {
                'national_id' : national_id,
                'first_name' : first_name,
                'last_name' : last_name,
                'age' : age,
                'lessons' : lessons,
                'classes' : classes,
            }
            is_changed = False
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
                    is_changed = True
            TeacherFH.save_to_file(self.teacher_list)
            if is_changed:
                print('[SYSTEM] Teacher has been edited.')
                input('press ENTER to continue...')
            else:
                print('[SYSTEM] Nothing has been changed.')
                input('press ENTER to continue...')
        else:
            print('[SYSTEM] Teacher not found')
            input('press ENTER to continue...')
        return

    def delete(self):
        print("--Delete Teacher")
        personnel_code = input("-Enter Personnel Code: ")
        personnel_code = TeacherValidator.validate_id(personnel_code, self.teacher_list, 'teacher', is_required=True, is_key=False)
        if personnel_code is None:
            input('Press ENTER to continue...')
            return
        teacher = next((t for t in self.teacher_list if personnel_code == int(t.personnel_code)), None)
        if teacher:
            confirm = input(f'[SYSTEM] Are you sure to delete {teacher.first_name} {teacher.last_name} (Y/N): ').lower()
            if confirm == 'n':
                print('[SYSTEM] Canceled.')
                input('press ENTER to continue...')
            elif confirm == 'y':
                for cls in self.class_list:
                    for id in teacher.classes:
                        if cls.class_id == id:
                            cls.teachers.remove(personnel_code)
                self.teacher_list.remove(teacher)
                ClassFH.save_to_file(self.class_list)
                TeacherFH.save_to_file(self.teacher_list)
                print('[SYSTEM] Teacher has been deleted.')
                input('press ENTER to continue...')
            else:
                print('[ERROR] Invalid Input.')
                input('press ENTER to continue...')
        else:
            print('T[SYSTEM] Teacher not found')
            input('press ENTER to continue...')
        return

    def search(self):
        print("--Search Teacher")
        get_fields = {
            'personnel_code': input('-Enter Personnel Code: '),
            'national_id': input('-Enter National ID: '),
            'first_name': input('-Enter First Name: '),
            'last_name': input('-Enter Last Name: '),
            'age_min': input('-Enter Minimum Age: '),
            'age_max': input('-Enter Maximum Age: '),
            'age': input('-Enter Age: '),
            'lessons': input('-Enter Lessons ID: '),
            'classes': input('-Enter Classes ID: '),
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
            print('---Teachers' + '-'* 100)
            for teacher in teachers:
                print(teacher)
            print('-' * 110)
            input('press ENTER to continue...')
        else:
            print("[SYSTEM] No Teacher found")
            input('press ENTER to continue...')

    def show(self):
        print('---Teachers' + '-' * 100)
        for obj in self.teacher_list:
            print(obj)
        print('-' * 110)
        input('press ENTER to continue...')
        return

class ClassManager(Manager):
    def __init__(self):
        self.class_list = []
        ClassFH.load_file(Class, self.class_list)
        self.set_students()
        self.set_teachers()
    def add(self):
        print('--Add Class')
        class_id = input("-Enter Class ID: ")
        class_id = ClassValidator.validate_cid(class_id, self.class_list, is_required=True)
        if class_id is None:
            input('Press ENTER to continue...')
            return
        class_name = input("-Enter Class Name: ")
        class_name = ClassValidator.validate_cname(class_name, is_required=True)
        if class_name is None:
            input('Press ENTER to continue...')
            return
        capacity = input("-Enter Class Capacity: ")
        capacity = ClassValidator.validate_capacity(capacity, is_required=True)
        if capacity is None:
            input('Press ENTER to continue...')
            return
        self.class_list.append(
            Class(
                class_id, class_name, capacity
            )
        )
        ClassFH.save_to_file(self.class_list)
        print('[SYSTEM] Class has been added successfully.')
        input('press ENTER to continue...')

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
        print('--Edit Class')
        class_id = input("-Enter Class ID: ")
        class_id = ClassValidator.validate_cid(class_id, self.class_list, is_required=True, is_key=False)
        if class_id is None:
            input('Press ENTER to continue...')
            return
        cls = next((c for c in self.class_list if class_id == int(c.class_id)), None)
        if cls:
            print('-' * 20)
            print(cls)
            print('*leave fields empty if you want current value*')
            class_name = ClassValidator.validate_cname(input('-Enter Class Name: '))
            if class_name is None:
                input('Press ENTER to continue...')
                return
            capacity = ClassValidator.validate_capacity(input('-Enter Class Capacity: '))
            if capacity is None:
                input('Press ENTER to continue...')
                return
            fields = {
                'class_name' : class_name,
                'capacity' : capacity,
            }
            is_changed = False
            for field, value in fields.items():
                if value:
                    setattr(cls, field, value)
                    ClassFH.save_to_file(self.class_list)
                    is_changed = True
            print('[SYSTEM] Class has been edited.')
            input('press ENTER to continue...')
            if not is_changed:
                print('[SYSTEM] Nothing has been changed.')
                input('press ENTER to continue...')
        else:
            print('[SYSTEM] Class not found')
        return

    def delete(self):
        print('--Delete Class')
        class_id = input("-Enter Class ID: ")
        class_id = ClassValidator.validate_cid(class_id, self.class_list, is_required=True, is_key=False)
        if class_id is None:
            input('Press ENTER to continue...')
            return
        cls = next((c for c in self.class_list if class_id == int(c.class_id)), None)
        if cls:
            confirm = input(f'[SYSTEM] Are you sure to delete {cls.class_name}  (Y/N): ').lower()
            if confirm == 'n':
                print('[SYSTEM] Canceled.')
                input('press ENTER to continue...')
            elif confirm == 'y':
                self.class_list.remove(cls)
                ClassFH.save_to_file(self.class_list)
                print('[SYSTEM] Class has been deleted')
                input('press ENTER to continue...')
            else:
                print('[ERROR] Invalid input.')
                input('press ENTER to continue...')
        else:
            print('[SYSTEM] No Class found')
            input('press ENTER to continue...')

    def search(self):
        print('--Search Class')
        get_fields = {
            'class_id' : input('-Enter Class ID: '),
            'class_name' : input('-Enter Class Name: '),
            'capacity_min' : input('-Enter Minimum Capacity: '),
            'capacity_max' : input('-Enter Maximum Capacity: '),
            'capacity' : input('-Enter Capacity: '),
        }
        fields = {}
        for field, value in get_fields.items():
            if value:
                fields[field] = value
        classes = deepcopy(self.class_list)
        for field, value in fields.items():
            if field.endswith('_min'):
                classes = [c for c in classes if float(getattr(c, field[:-4], None)) >= float(value)]
            elif field.endswith('_max'):
                classes = [c for c in classes if float(getattr(c, field[:-4], None)) <= float(value)]
            else:
                classes = [c for c in classes if getattr(c, field, None) == value]
        if classes:
            print('---Classes' + '-' * 100)
            for cls in classes:
                print(cls)
            print('-' * 110)
            input('press ENTER to continue...')
        else:
            print("[SYSTEM] No Class found")
            input('press ENTER to continue...')

    def show(self):
        print('---Classes' + '-' * 100)
        for obj in self.class_list:
            print(obj)
            print('-' * 110)
            input('press ENTER to continue...')

    def show_students(self):
        print('--Show Students')
        class_id = input("-Enter Class ID: ")
        class_id = ClassValidator.validate_cid(class_id, self.class_list, is_required=True, is_key=False)
        if class_id is None:
            input('Press ENTER to continue...')
            return
        cls = next((c for c in self.class_list if class_id == int(c.class_id)), None)
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
            input('press ENTER to continue...')
        else:
            print('[SYSTEM] No Class found')


    def show_teachers(self):
        print('--Show Teachers')
        class_id = input("-Enter Class ID: ")
        class_id = ClassValidator.validate_cid(class_id, self.class_list, is_required=True, is_key=False)
        if class_id is None:
            input('Press ENTER to continue...')
            return
        cls = next((c for c in self.class_list if class_id == int(c.class_id)), None)
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
            input('press ENTER to continue...')
        else:
            print('[SYSTEM] No Class found')
            input('press ENTER to continue...')
        return

class LessonManager(Manager):
    def __init__(self):
        self.lesson_list = []
        LessonFH.load_file(Lesson, self.lesson_list)

    def add(self):
        print('--Add Lesson')
        lesson_id = input("-Enter Lesson ID: ")
        lesson_id = LessonValidator.validate_lid(lesson_id, self.lesson_list, is_required=True, is_key=True)
        if lesson_id is None:
            input('Press ENTER to continue...')
            return
        lesson_name = input("-Enter Lesson Name: ")
        lesson_name = LessonValidator.validate_lname(lesson_name, is_required=True)
        if lesson_name is None:
            input('Press ENTER to continue...')
            return
        units = input("-Enter Units: ")
        units = LessonValidator.validate_units(units, is_required=True)
        if units is None:
            input('Press ENTER to continue...')
            return
        self.lesson_list.append(
            Lesson(lesson_id, lesson_name, units)
        )
        LessonFH.save_to_file(self.lesson_list)
        print('[SYSTEM] Lesson has been added successfully.')
        input('press ENTER to continue...')

    def edit(self):
        print('--Edit Lesson')
        lesson_id = input("-Enter Lesson ID: ")
        lesson_id = LessonValidator.validate_lid(lesson_id, self.lesson_list, is_required=True, is_key=False)
        if lesson_id is None:
            input('Press ENTER to continue...')
            return
        lesson = next((l for l in self.lesson_list if int(l.lesson_id) == lesson_id), None)
        if lesson:
            print('-' * 20)
            print(lesson)
            print('*leave fields empty if you want current value*')
            lesson_name = LessonValidator.validate_lname(input('-Enter Lesson Name: '))
            if lesson_name is None:
                input('Press ENTER to continue...')
                return
            units = LessonValidator.validate_units(input('-Enter Units: '))
            if units is None:
                input('Press ENTER to continue...')
                return
            fields = {
                'lesson_name' : lesson_name,
                'units' : units
            }
            is_changed = False
            for field, value in fields.items():
                if value:
                    setattr(lesson, field, value)
                    LessonFH.save_to_file(self.lesson_list)
                    is_changed = True
            if is_changed:
                print('[SYSTEM] Lesson has been edited.')
                input('press ENTER to continue...')
            else:
                print('[SYSTEM] Nothing has been changed.')
                input('press ENTER to continue...')
        else:
            print('[SYSTEM] No Lesson found.')
            input('press ENTER to continue...')
        return

    def delete(self):
        print('--Delete Lesson')
        lesson_id = input("-Enter Lesson ID: ")
        lesson_id = LessonValidator.validate_lid(lesson_id, self.lesson_list, is_required=True, is_key=False)
        if lesson_id is None:
            input('Press ENTER to continue...')
            return
        lesson = next((l for l in self.lesson_list if int(l.lesson_id) == lesson_id), None)
        if lesson:
            confirm = input(f'[SYSTEM] Are you sure to delete {lesson.lesson_name}  (Y/N): ').lower()
            if confirm == 'n':
                print('[SYSTEM] Canceled.')
                input('press ENTER to continue...')
            elif confirm == 'y':
                self.lesson_list.remove(lesson)
                LessonFH.save_to_file(self.lesson_list)
                print('[SYSTEM] Lesson has been deleted')
                input('press ENTER to continue...')
            else:
                print('[ERROR] Invalid input')
                input('press ENTER to continue...')
        else:
            print('[SYSTEM] No Lesson found')
            input('press ENTER to continue...')
        return

    def search(self):
        get_fields = {
            'lesson_id' : input('-Enter Lesson ID: '),
            'lesson_name' : input('-Enter Lesson Name: '),
            'units_min' : input('-Enter Minimum Units: '),
            'units_max' : input('-Enter Maximum Units: '),
            'units' : input('-Enter Units: ')
        }
        fields = {}
        for field, value in get_fields.items():
            if value:
                fields[field] = value
        lessons = deepcopy(self.lesson_list)
        for field, value in fields.items():
            if field.endswith('_min'):
                classes = [l for l in lessons if float(getattr(l, field[:-4], None)) >= float(value)]
            elif field.endswith('_max'):
                classes = [l for l in lessons if float(getattr(l, field[:-4], None)) <= float(value)]
            else:
                classes = [l for l in lessons if getattr(l, field, None) == value]
        if lessons:
            print('--Lessons' + '-' * 100)
            for lesson in lessons:
                print(lesson)
            print('-' * 110)
            input('press ENTER to continue...')
        else:
            print("[SYSTEM] No Lesson found")
            input('press ENTER to continue...')
        return

    def show(self):
        print('--Lessons' + '-' * 100)
        for obj in self.lesson_list:
            print(obj)
        print('-' * 110)
        input('press ENTER to continue...')
        return

class ReportCardManager(Manager):
    def __init__(self):
        self.rc_list = []
        self._students_list = []
        self._class_list = []
        self._teachers_list = []
        self._lessons_list = []
        ReportCardFH.load_file(ReportCard, self.rc_list)
        StudentFH.load_file(Student, self._students_list)
        ClassFH.load_file(Class, self._class_list)
        TeacherFH.load_file(Teacher, self._teachers_list)
        LessonFH.load_file(Lesson, self._lessons_list)

    def add(self):
        print('-- Add Grade')
        student_id = input("-Enter Student ID: ")
        student_id = RCValidator.validate_sid(student_id)
        if student_id is None:
            input('Press ENTER to continue...')
            return
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
            print('-' * 20)
            for lesson in lessons:
                grade = input(f"-Enter {lesson.lesson_name}'s Grade: ")
                grade = RCValidator.validate_grade(grade)
                if grade is None:
                    input('Press ENTER to continue...')
                    return
                grades.append(grade)

            self.rc_list.append(
                ReportCard(
                    student_id,grades
                )
            )
            ReportCardFH.save_to_file(self.rc_list)
            print('[SYSTEM] Grades has been added successfully.')
            input('press ENTER to continue...')
        else:
            print('[SYSTEM] Student not found.')
            input('press ENTER to continue...')
        return

    def edit(self):
        pass

    def delete(self):
        print('-- Delete ReportCard')
        student_id = input("-Enter Student ID: ")
        student_id = StudentValidator.validate_id(student_id, self._students_list, obj_type='student', is_required=True,is_key=False)
        if student_id is None:
            input('Press ENTER to continue...')
            return
        student = next((s for s in self._students_list if int(s.student_id) == student_id), None)
        rc = next((rc for rc in self.rc_list if int(rc.student) == student_id), None)
        if student and rc:
            confirm = input(f'[SYSTEM] Are you sure to delete {student.first_name} {student.last_name}\'s Report Card  (Y/N): ').lower()
            if confirm == 'n':
                print('[SYSTEM] Canceled.')
            elif confirm == 'y':
                self.rc_list.remove(rc)
                ReportCardFH.save_to_file(self.rc_list)
                print('[SYSTEM] Report Card has been deleted.')
                input('press ENTER to continue...')
            else:
                print('[ERROR] Invalid input.')
                input('press ENTER to continue...')
        else:
            print('[SYSTEM] No Report Card found.')
            input('press ENTER to continue...')
        return

    def search(self):
        pass

    def show(self):
        print('--Show Grades')
        student_id = input("-Enter Student ID: ")
        student_id = StudentValidator.validate_id(student_id, self._students_list, obj_type='student', is_required=True,is_key=False)
        if student_id is None:
            input('Press ENTER to continue...')
            return
        student = next((s for s in self._students_list if int(s.student_id) == student_id), None)
        if student:
            lessons_id = []
            lessons = []
            grades = []
            students_class = next((c for c in self._class_list if int(student.class_id) == int(c.class_id)), None)
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
                if int(rc.student) == int(student_id):
                    grades = rc.grades
            print(f'----{student.first_name} {student.last_name}\'s Grades' + '----' )
            for lesson,grade in zip(lessons, grades):
                print(f"{lesson.lesson_name}'s Grade: {grade}")
            print('-' * 20)
            input('press ENTER to continue...')
        else:
            print('[SYSTEM] Student not found')
            input('press ENTER to continue...')