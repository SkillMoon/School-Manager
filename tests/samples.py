from school_manager.models import *


lesson1 = Lesson(10, 'math', 2)
lesson2 = Lesson(11, 'english', 2)
lesson3 = Lesson(12, 'physics', 3)
report_card = ReportCard(1, 20)
report_card2 = ReportCard(1, 20)
class1 = Class(1, 'b1', 22,
                   [10, 11])
class2 = Class(2, 'b2', 23,
                   [10,11,12])
teacher1 = Teacher(20, 'n', 'ali',
                       'mohhammadi', 32, ['10'], [1])
teacher2 = Teacher(21, 'n', 'hossein',
                      'hosseini', 30, ['11','12'],
                       [2])
student1 = Student(30, 'n', 'matin',
                     ' salesi', 19, 'fifth', 1)
student2 = Student(31, 'n', 'mehdi',
                  'moradi', 18, 'fifth', 2)


