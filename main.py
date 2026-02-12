from school_manager.managers import *

if __name__ == '__main__':
    std_manager = StudentManager()
    class_manager = ClassManager()
    teacher_manager = TeacherManager()
    lesson_manager = LessonManager()
    rc_manager = ReportCardManager()

    rc_manager.show()
    # lesson_manager.delete()
    # class_manager.show_teachers()
    # std_manager.search()
    # teacher_manager.edit()


