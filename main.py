from tests.samples import *
from school_manager.storage_handler import *
if __name__ == '__main__':
    # teacher_list = [report_card, report_card2]
    teacher_list = []
    ReportCardFH.load_file(ReportCard,teacher_list)
    for teacher in teacher_list:
        print(teacher.student)
    # print(report_card.to_dict())
