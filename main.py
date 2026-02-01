from school_manager.managers import *

if __name__ == '__main__':
    std_manager = StudentManager()
    class_manager = ClassManager()
    teacher_manager = TeacherManager()
    lesson_manager = LessonManager()
    rc_manager = ReportCardManager()

    # rc_manager.delete()
    # lesson_manager.edit()
    # class_manager.show_students()
    std_manager.add()
    # teacher_manager.delete()