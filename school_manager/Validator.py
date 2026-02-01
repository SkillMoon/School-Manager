from abc import ABC, abstractmethod

class Validator(ABC):
    pass
class UserBasicValidator(Validator):
    @staticmethod
    def validate_id(id, object_list, obj_type,is_required=False, type='id'):
        if is_required:
            id = str(id).strip()
            if not id:
                print('This field is required')
                id = None
                return
            for i in id:
                if i.isalpha():
                    print('id must be a number')
                    return None
            if type == 'id':
                if obj_type == 'student':
                    for student in object_list:
                        if student.student_id == id:
                            print('Student ID already exists')
                            id = None
                            return
                elif obj_type == 'teacher':
                    for teacher in object_list:
                        if teacher.personnel_code == id:
                            print('Personnel Code already exists')
                            id = None
                            return
                else:
                    print('Invalid object type')
                    return
            if type == 'national':
                if len(id) != 10:
                    print('National ID must be 10 digits')
                    id = None
                    return
            if type == 'id':
                id = int(id)
        else:
            if id:
                for i in id:
                    if i.isalpha():
                        print('id must be a number')
                        return None
                    if type == 'national':
                        if len(id) != 10:
                            print('National ID must be 10 digits')
                            id = None
                            return
        return id

    @staticmethod
    def validate_name(name, is_required=False):
        ban_chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#',
                     '$', '%', '^', '&', '*', '(', ')', '_', '-''+', '=', '[', ']',
                     '{', '}', ';', ':', '\'', '\"', '|', '/', '\\', '?', '.', ',',
                     '<', '>']
        if is_required:
            name = str(name).strip()
            if not name:
                print("Name is required")
                name = None
                return
            for char in ban_chars:
                if char in name:
                    print("cant use numbers and signs in name")
                    name = None
                    return
        else:
            for char in ban_chars:
                if char in name:
                    print("cant use numbers and signs in name")
                    name = None
                    return
        return name

    @staticmethod
    def validate_age(age, min, max, is_required=False):
        if is_required:
            age = str(age).strip()
            if not age:
                print("Age is required")
                age = None
                return
            if age.isalpha():
                print('Age must be a number')
                age = None
                return
            age = int(age)
            if age < min or age > max:
                print(f'Age must be between {min} and {max}')
                age = None
                return
        else:
            if age:
                if age.isalpha():
                    print('Age must be a number')
                    age = None
                    return
                age = int(age)
                if age not in range(min, max + 1):
                    print(f'Age must be between {min} and {max}')
                    age = None
                    return
        return age

class StudentValidator(UserBasicValidator):
    @staticmethod
    def validate_gl(grade_level, is_required=False):
        if is_required:
            grade_level = str(grade_level).strip()
            if not grade_level:
                print("Grade level is required")
                grade_level = None
                return
            for i in grade_level:
                if i.isalpha():
                    print('Grade level must be a number')
                    grade_level = None
                    return
            grade_level = int(grade_level)
            if grade_level not in range(10,13):
                print(f'Grade level must be between 10 and 12')
                grade_level = None
                return
        else:
            if grade_level:
                grade_level = str(grade_level).strip()
                for i in grade_level:
                    if i.isalpha():
                        print('Grade level must be a number')
                        grade_level = None
                        return
                grade_level = int(grade_level)
                if grade_level not in range(10, 13):
                    print(f'Grade level must be between 10 and 12')
                    grade_level = None
                    return
        return grade_level

    @staticmethod
    def validate_cid(class_id, class_list, is_required=False):
        if is_required:
            class_id = str(class_id).strip()
            if not class_id:
                print("Class ID is required")
                class_id = None
                return
            for i in class_id:
                if i.isalpha():
                    print('Class ID must be a number')
                    class_id = None
                    return
            class_id = int(class_id)
            if class_id not in class_list:
                print(f'Class ID {class_id} is not in the list of available classes')
                class_id = None
                return
        else:
            if class_id:
                class_id = str(class_id).strip()
                for i in class_id:
                    if i.isalpha():
                        print('Class ID must be a number')
                        class_id = None
                        return
                class_id = int(class_id)
                if class_id not in class_list:
                    print(f'Class ID {class_id} is not in the list of available classes')
                    class_id = None
                    return
        return class_id