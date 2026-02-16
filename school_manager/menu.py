from school_manager.managers import StudentManager, ClassManager, TeacherManager, LessonManager,ReportCardManager

class CLI:

    def __init__(self):
        self.student_menu = StudentMenu(StudentManager(), self)
        self.teacher_menu = TeacherMenu(TeacherManager(), self)
        self.class_manu = ClassMenu(ClassManager(), self)
        self.lesson_menu = LessonMenu(LessonManager(), self)
        self.rc_menu = RCMenu(ReportCardManager(), self)
        self.OPTIONS_FUNCTIONS = {
            1 : self.student_menu.run, 2 : self.teacher_menu.run,
            3 : self.class_manu.run, 4 : self.lesson_menu.run,
            5 : self.rc_menu.run, 6 : exit
        }
        self.OPTIONS = {
            1: '  1. Manage Students', 2: '  2. Manage Teachers',
            3: '  3. Manage Classes', 4: '  4. Manage Lessons',
            5: '  5. Manage Grades', 6: '  6. Exit'
        }

    def run(self):
        print('--Main Menu')
        for key, option in self.OPTIONS.items():
            print(option)
        user_input  = input('-Enter your choice: ')
        if any(char.isalpha() for char in user_input):
            print('[ERROR] Invalid Input')
            input('Press ENTER to continue...')
            self.run()
        user_input = int(user_input)
        if user_input not in self.OPTIONS_FUNCTIONS.keys():
            print('[ERROR] Invalid Input')
            input('press ENTER to continue...')
            self.run()
        op = self.OPTIONS_FUNCTIONS.get(user_input)
        if op:
            op()

class StudentMenu:
    def __init__(self, manager, main_menu):
        self._manager = manager

        self.OPTIONS = {
            1 : '  1. Add Student', 2 : '  2. Edit Student', 3 : '  3. Delete Student',
            4 : '  4. Search Student', 5 : '  5. Show All Students', 6 : '  6. Back'
        }
        self.OPTIONS_FUNCTIONS = {
            1 : self._manager.add, 2 : self._manager.edit, 3 : self._manager.delete,
            4 : self._manager.search, 5 : self._manager.show, 6 : main_menu.run
        }

    def run(self):
        print('--Student Menu')
        for key, option in self.OPTIONS.items():
            print(option)
        user_input  = input('-Enter your choice: ')
        if any(char.isalpha() for char in user_input):
            print('[ERROR] Invalid Input')
            input('Press ENTER to continue...')
            self.run()
        user_input = int(user_input)
        if user_input not in self.OPTIONS_FUNCTIONS.keys():
            print('[ERROR] Invalid Input')
            input('press ENTER to continue...')
            self.run()
        op = self.OPTIONS_FUNCTIONS.get(user_input)
        if op:
            op()
            self.run()


class TeacherMenu:
    def __init__(self, manager, main_menu):
        self._manager = manager
        self.OPTIONS = {
            1 : '  1. Add Teacher', 2 : '  2. Edit Teacher', 3 : '  3. Delete Teacher',
            4 : '  4. Search Teacher', 5 : '  5. Show All Teachers', 6 : '  6. Back'
        }
        self.OPTIONS_FUNCTIONS = {
            1 : self._manager.add, 2 : self._manager.edit, 3 : self._manager.delete,
            4 : self._manager.search, 5 : self._manager.show, 6 : main_menu.run
        }

    def run(self):
        print('--Teacher Menu')
        for key, option in self.OPTIONS.items():
            print(option)
        user_input = input('-Enter your choice: ')
        if any(char.isalpha() for char in user_input):
            print('[ERROR] Invalid Input')
            input('Press ENTER to continue...')
            self.run()
        user_input = int(user_input)
        if user_input not in self.OPTIONS_FUNCTIONS.keys():
            print('[ERROR] Invalid Input')
            input('press ENTER to continue...')
            self.run()
        op = self.OPTIONS_FUNCTIONS.get(user_input)
        if op:
            op()
            self.run()

class ClassMenu:
    def __init__(self, manager, main_menu):
        self._manager = manager
        self.OPTIONS = {
            1 : '  1. Add Class', 2 : '  2. Edit Class', 3 : '  3. Delete Class',
            4 : '  4. Search Class', 5 : '  5. Show All Classes', 6 : '  6. Show Students',
            7 : '  7. Show Teachers', 8 : '  8. Back'
        }
        self.OPTIONS_FUNCTIONS = {
            1 : self._manager.add, 2 : self._manager.edit, 3 : self._manager.delete,
            4 : self._manager.search, 5 : self._manager.show, 6 : self._manager.show_students,
            7 : self._manager.show_teachers, 8 : main_menu.run
        }


    def run(self):
        print('--Class Menu')
        for key, option in self.OPTIONS.items():
            print(option)
        user_input = input('-Enter your choice: ')
        if any(char.isalpha() for char in user_input):
            print('[ERROR] Invalid Input')
            input('Press ENTER to continue...')
            self.run()
        user_input = int(user_input)
        if user_input not in self.OPTIONS_FUNCTIONS.keys():
            print('[ERROR] Invalid Input')
            input('press ENTER to continue...')
            self.run()
        op = self.OPTIONS_FUNCTIONS.get(user_input)
        if op:
            op()
            self.run()

class LessonMenu:
    def __init__(self, manager, main_menu):
        self._manager = manager
        self.OPTIONS = {
            1 : '  1. Add Lesson', 2 : '  2. Edit Lesson', 3 : '  3. Delete Lesson',
            4 : '  4. Search Lesson', 5 : '  5. Show All Lessons', 6 : '  6. Back'
        }
        self.OPTIONS_FUNCTIONS = {
            1 : self._manager.add, 2 : self._manager.edit, 3 : self._manager.delete,
            4 : self._manager.search, 5 : self._manager.show, 6 : main_menu.run
        }

    def run(self):
        print('--Lesson Menu')
        for key, option in self.OPTIONS.items():
            print(option)
        user_input = input('-Enter your choice: ')
        if any(char.isalpha() for char in user_input):
            print('[ERROR] Invalid Input')
            input('Press ENTER to continue...')
            self.run()
        user_input = int(user_input)
        if user_input not in self.OPTIONS_FUNCTIONS.keys():
            print('[ERROR] Invalid Input')
            input('press ENTER to continue...')
            self.run()
        op = self.OPTIONS_FUNCTIONS.get(user_input)
        if op:
            op()
            self.run()

class RCMenu:
    def __init__(self, manager, main_menu):
        self._manager = manager
        self.OPTIONS = {
            1 : '  1. Add Grade', 2 : '  3. Delete Report Card', 3 : '  3. Show Report Card',
            4 : '  4. Back'
        }
        self.OPTIONS_FUNCTIONS = {
            1 : self._manager.add, 2 : self._manager.delete, 3 : self._manager.show,
            4 : main_menu.run
        }


    def run(self):
        print('--Grades Menu')
        for key, option in self.OPTIONS.items():
            print(option)
        user_input = input('-Enter your choice: ')
        if any(char.isalpha() for char in user_input):
            print('[ERROR] Invalid Input')
            input('Press ENTER to continue...')
            self.run()
        user_input = int(user_input)
        if user_input not in self.OPTIONS_FUNCTIONS.keys():
            print('[ERROR] Invalid Input')
            input('press ENTER to continue...')
            self.run()
        op = self.OPTIONS_FUNCTIONS.get(user_input)
        if op:
            op()
            self.run()

