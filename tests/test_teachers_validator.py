from school_manager.validator import TeacherValidator
from school_manager.models import Teacher, Class, Lesson
from school_manager.storage_handler import TeacherFH, ClassFH, LessonFH


class TestTeacherValidator:

    def setup_method(self):
        self.teacher_list = []
        self.class_list = []
        self.lesson_list = []
        TeacherFH.load_file(Teacher, self.teacher_list)
        ClassFH.load_file(Class, self.class_list)
        LessonFH.load_file(Lesson, self.lesson_list)

    def test_validate_id(self):
        assert TeacherValidator.validate_id('5001', self.teacher_list, obj_type='teacher', is_required=True, is_key=True) is None
        assert TeacherValidator.validate_id('5009', self.teacher_list, obj_type='teacher', is_required=True, is_key=True) is not None
        assert TeacherValidator.validate_id('5001', self.teacher_list, obj_type='teacher', is_required=True, is_key=False) is not None

    def test_validate_lid(self):
        '''
            if is_key=True then have to enter exist lesson id
            is_key is set to True by default
        '''
        assert TeacherValidator.validate_lid(['   '], [int(lsn.lesson_id) for lsn in self.lesson_list], is_required=True) is None
        assert TeacherValidator.validate_lid(['   '], [int(lsn.lesson_id) for lsn in self.lesson_list], is_required=False) is not None
        assert TeacherValidator.validate_lid(['12s1'], [int(lsn.lesson_id) for lsn in self.lesson_list], is_required=True) is None
        assert TeacherValidator.validate_lid(['208'], [int(lsn.lesson_id) for lsn in self.lesson_list], is_required=True) is None
        assert TeacherValidator.validate_lid(['208'], [int(lsn.lesson_id) for lsn in self.lesson_list], is_required=True, is_key=False) is not None

    def test_validate_cid(self):
        '''
            if is_key=True then have to enter exist class id
            is_key is set to True by default
        '''
        assert TeacherValidator.validate_cid(['   '], [int(cls.class_id) for cls in self.class_list], is_required=True) is None
        assert TeacherValidator.validate_cid(['   '], [int(cls.class_id) for cls in self.class_list], is_required=False) is not None
        assert TeacherValidator.validate_cid(['12s1'], [int(cls.class_id) for cls in self.class_list], is_required=True) is None
        assert TeacherValidator.validate_cid(['106'], [int(cls.class_id) for cls in self.class_list], is_required=True) is None
        assert TeacherValidator.validate_cid(['106'], [int(cls.class_id) for cls in self.class_list], is_required=True, is_key=False) is not None
