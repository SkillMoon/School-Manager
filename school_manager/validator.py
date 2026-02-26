from abc import ABC
BAN_CHARS_FOR_STR = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#',
             '$', '%', '^', '&', '*', '(', ')', '_', '-''+', '=', '[', ']',
             '{', '}', ';', ':', '\'', '\"', '|', '/', '\\', '?', '.', ',',
             '<', '>']
BAN_CHARS_FOR_INT = ['!', '@', '#',
             '$', '%', '^', '&', '*', '(', ')', '_', '-''+', '=', '[', ']',
             '{', '}', ';', ':', '\'', '\"', '|', '/', '\\', '?', '.', ',',
             '<', '>']
class UserBasicValidator(ABC):
    @staticmethod
    def validate_id(id, object_list, obj_type,is_required=False, is_key=True, type='id'):
        id = str(id).strip()
        if is_required:

            if not id:
                print('[ERROR] This field is required.')
                return None
            for i in id:
                if i.isalpha() or i in BAN_CHARS_FOR_INT:
                    print('[ERROR] ID must be a number.')
                    return None
            if is_key:
                if type == 'id':
                    if obj_type == 'student':
                        for student in object_list:
                            if student.student_id == id:
                                print('[ERROR] Student ID already exists.')
                                return None
                    elif obj_type == 'teacher':
                        for teacher in object_list:
                            if teacher.personnel_code == id:
                                print('[ERROR] Personnel Code already exists.')
                                return None
                    else:
                        print('[ERROR] Invalid object type.')
                        return None
            if type == 'national':
                if len(id) != 10:
                    print('[ERROR] National ID must be 10 digits.')
                    return None
            if type == 'id':
                id = int(id)
        else:
            if id:
                for i in id:
                    if i.isalpha() or i in BAN_CHARS_FOR_STR:
                        print('[ERROR] ID must be a number.')
                        return None
                if type == 'national':
                    if len(id) != 10:
                        print('[ERROR] National ID must be 10 digits.')
                        return None
                if is_key:
                    if type == 'id':
                        if obj_type == 'student':
                            for student in object_list:
                                if student.student_id == id:
                                    print('[ERROR] Student ID already exists.')
                                    return None
                        elif obj_type == 'teacher':
                            for teacher in object_list:
                                if teacher.personnel_code == id:
                                    print('[ERROR] Personnel Code already exists.')
                                    return None
                        else:
                            print('[ERROR] Invalid object type.')
                            return None
        return id

    @staticmethod
    def validate_name(name, is_required=False):
        name = str(name).strip()
        if is_required:
            if not name:
                print('[ERROR] This field is required.')
                return None
            for char in BAN_CHARS_FOR_STR:
                if char in name:
                    print("[ERROR] Can not use numbers and signs in name.")
                    return None
        else:
            if name:
                for char in BAN_CHARS_FOR_STR:
                    if char in name:
                        print("[ERROR] Can not use numbers and signs in name.")
                        return None
        return name

    @staticmethod
    def validate_age(age, min, max, is_required=False):
        age = str(age).strip()
        if is_required:
            if not age:
                print('[ERROR] This field is required.')
                return None
            for i in age:
                if i.isalpha() or i in BAN_CHARS_FOR_INT:
                    print('[ERROR] Age must be a number.')
                    return None
            age = int(age)
            if age not in range(min, max + 1):
                print(f'[ERROR] Age must be between {min} and {max}.')
                return None
        else:
            if age:
                for i in age:
                    if i.isalpha() or i in BAN_CHARS_FOR_INT:
                        print('[ERROR] Age must be a number.')
                        return None
                age = int(age)
                if age not in range(min, max + 1):
                    print(f'[ERROR] Age must be between {min} and {max}.')
                    return None
        return age

class StudentValidator(UserBasicValidator):
    @staticmethod
    def validate_gl(grade_level, is_required=False):
        grade_level = str(grade_level).strip()
        if is_required:
            if not grade_level:
                print('[ERROR] This field is required.')
                return None
            for i in grade_level:
                if i.isalpha() or i in BAN_CHARS_FOR_INT:
                    print('[ERROR] Grade level must be a number.')
                    return None
            grade_level = int(grade_level)
            if grade_level not in range(10,13):
                print(f'[ERROR] Grade level must be between 10 and 12.')
                return None
        else:
            if grade_level:
                for i in grade_level:
                    if i.isalpha() or i in BAN_CHARS_FOR_INT:
                        print('[ERROR] Grade level must be a number.')
                        return None
                grade_level = int(grade_level)
                if grade_level not in range(10, 13):
                    print(f'[ERROR] Grade level must be between 10 and 12.')
                    return None
        return grade_level

    @staticmethod
    def validate_cid(class_id, class_list, is_required=False):
        class_id = str(class_id).strip()
        if is_required:
            if not class_id:
                print('[ERROR] This field is required.')
                return None
            for i in class_id:
                if i.isalpha() or i in BAN_CHARS_FOR_INT:
                    print('[ERROR] Class ID must be a number.')
                    return None
            class_id = int(class_id)
            if class_id not in class_list:
                print(f'[ERROR] Class ID {class_id} is not in the list of available classes.')
                return None
        else:
            if class_id:
                for i in class_id:
                    if i.isalpha() or i in BAN_CHARS_FOR_INT:
                        print('[ERROR] Class ID must be a number.')
                        return None
                class_id = int(class_id)
                if class_id not in class_list:
                    print(f'[ERROR] Class ID {class_id} is not in the list of available classes.')
                    return None
        return class_id
class TeacherValidator(UserBasicValidator):
    @staticmethod
    def validate_lid(lesson_id, lesson_list, is_required=False, is_key=True):
        lesson_id[0] = str(lesson_id[0].strip())
        if is_required:
            if not lesson_id[0]:
                print('[ERROR] This field is required.')
                return None
            for i in lesson_id[0]:
                if i.isalpha() or i in BAN_CHARS_FOR_INT:
                    print('[ERROR] Lesson ID must be a number.')
                    return None
            lesson_id[0] = int(lesson_id[0])
            if is_key:
                if lesson_id[0] not in lesson_list:
                    print('[ERROR] This lesson id does not belong to any lessons.')
                    return None
        else:
            if lesson_id[0]:
                for i in lesson_id[0]:
                    if i.isalpha() or i in BAN_CHARS_FOR_INT:
                        print('[ERROR] Lesson ID must be a number.')
                        return None
                if is_key:
                    if lesson_id[0] not in lesson_list:
                        print('[ERROR] This lesson id does not belong to any lessons.')
                        return None
        return lesson_id

    @staticmethod
    def validate_cid(class_id, class_list, is_required=False, is_key=True):
        class_id[0] = str(class_id[0].strip())
        if is_required:
            if not class_id[0]:
                print('[ERROR] This field is required.')
                return None
            for i in class_id[0]:
                if i.isalpha() or i in BAN_CHARS_FOR_INT:
                    print('[ERROR] Class ID must be a number.')
                    return None
            class_id[0] = int(class_id[0])
            if is_key:
                if class_id[0] not in class_list:
                    print(f'[ERROR] Class ID {class_id[0]} is not in the list of available classes.')
                    return None
        else:
            if class_id[0]:
                for i in class_id[0]:
                    if i.isalpha() or i in BAN_CHARS_FOR_INT:
                        print('[ERROR] Class ID must be a number.')
                        return None
                class_id[0] = int(class_id[0])
                if is_key:
                    if class_id[0] not in class_list:
                        print(f'[ERROR] Class ID {class_id[0]} is not in the list of available classes.')
                        return None
        return  class_id

class ClassValidator:

    @staticmethod
    def validate_cid(cid, class_list, is_required=False, is_key=True):
        cid = str(cid).strip()
        if is_required:
            if not cid:
                print('[ERROR] This field is required.')
                return None
            for i in cid:
                if i.isalpha() or i in BAN_CHARS_FOR_INT:
                    print('[ERROR] Class ID must be a number.')
                    return None
            cid = int(cid)
            if is_key:
                for cls in class_list:
                    if int(cls.class_id) == cid:
                        print('[ERROR] This ID already exists.')
                        return None
        else:
            if cid:
                for i in cid:
                    if i.isalpha() or i in BAN_CHARS_FOR_INT:
                        print('[ERROR] Class ID must be a number.')
                        return None
                cid = int(cid)
                if is_key:
                    for cls in class_list:
                        if int(cls.class_id) == cid:
                            print('[ERROR] This ID already exists.')
                            return None
        return cid

    @staticmethod
    def validate_cname(class_name, is_required=False):
        class_name = str(class_name).strip()
        if is_required:
            if not class_name:
                print('[ERROR] This field is required.')
                return None
            for char in class_name:
                if char in BAN_CHARS_FOR_STR:
                    print("[ERROR] Can not use numbers and signs in name.")
                    return None
        else:
            if class_name:
                for char in class_name:
                    if char in BAN_CHARS_FOR_STR:
                        print("[ERROR] Can not use numbers and signs in name.")
                        return None
        return class_name

    @staticmethod
    def validate_capacity(capacity, is_required=False):
        capacity = str(capacity).strip()
        if is_required:
            if not capacity:
                print('[ERROR] This field is required.')
                return None
            for i in capacity:
                if i.isalpha() or i in BAN_CHARS_FOR_INT:
                    print('[ERROR] Capacity must be a number.')
                    return None
            capacity = int(capacity)
        else:
            if capacity:
                for i in capacity:
                    if i.isalpha():
                        print('[ERROR] Capacity must be a number.')
                        return None
                capacity = int(capacity)
        return capacity

class LessonValidator:
    @staticmethod
    def validate_lid(lid, lessons_list,is_required=False, is_key=True):
        lid = str(lid).strip()
        if is_required:
            if not lid:
                print('[ERROR] This field is required.')
                return None
            for i in lid:
                if i.isalpha() or i in BAN_CHARS_FOR_INT:
                    print('[ERROR] Lesson ID must be a number.')
                    return None
            lid = int(lid)
            if is_key:
                for lesson in lessons_list:
                    if int(lesson.lesson_id) == lid:
                        print('[ERROR] Lesson ID already exists.')
                        return None
        else:
            if lid:
                for i in lid:
                    if i.isalpha() or i in BAN_CHARS_FOR_INT:
                        print('[ERROR] Lesson ID must be a number.')
                        return None
                lid = int(lid)
                if is_key:
                    for lesson in lessons_list:
                        if int(lesson.lesson_id) == lid:
                            print('[ERROR] Lesson ID already exists.')
                            return None
        return lid
    @staticmethod
    def validate_lname(lesson_name, is_required=False):
        lesson_name = str(lesson_name).strip()
        if is_required:
            if not lesson_name:
                print('[ERROR] This field is required.')
                return None
            for char in lesson_name:
                if char in BAN_CHARS_FOR_STR:
                    print("[ERROR] Can not use numbers and signs in name.")
                    return None
        else:
            for char in lesson_name:
                if char in BAN_CHARS_FOR_STR:
                    print("[ERROR] Can not use numbers and signs in name.")
                    return None
        return lesson_name

    @staticmethod
    def validate_units(units, is_required=False):
        units = str(units).strip()
        if is_required:
            if not units:
                print('[ERROR] This field is required.')
                return None
            for i in units:
                if i.isalpha() or i in BAN_CHARS_FOR_INT:
                    print('[ERROR] Units must be a number.')
                    return None
            units = int(units)
            if units not in range(1, 9):
                print('[ERROR] Units must be between 1 and 8.')
                return None
        else:
            if units:
                for i in units:
                    if i.isalpha() or i in BAN_CHARS_FOR_INT:
                        print('[ERROR] Units must be a number.')
                        return None
                units = int(units)
                if units not in range(1, 9):
                    print('[ERROR] Units must be between 1 and 8.')
                    return None
        return units

class RCValidator:
    @staticmethod
    def validate_sid(student_id):
        student_id = str(student_id).strip()
        if not student_id:
            print('[ERROR] This field is required.')
            return None
        for i in student_id:
            if i.isalpha() or i in BAN_CHARS_FOR_INT:
                print('[ERROR] Student ID must be a number.')
                return None
        return student_id

    @staticmethod
    def validate_grade(grade):
        grade = str(grade).strip()
        if not grade:
            print('[ERROR] This field is required.')
            return None
        for i in grade:
            if i.isalpha() or i in BAN_CHARS_FOR_INT:
                print('[ERROR] Grade must be a number.')
                return None
        grade = float(grade)
        if grade <= -0.9 or grade >= 20.1:
            print('[ERROR] Grade must be between 0 and 20.')
            return None
        return grade