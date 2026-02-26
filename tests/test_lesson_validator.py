from school_manager.validator import LessonValidator
from school_manager.models import Lesson
from school_manager.storage_handler import LessonFH

class TestLessonValidator:

    def setup_method(self):
        self.lesson_list = []
        LessonFH.load_file(Lesson, self.lesson_list)

    def test_validate_id(self):
        '''
            if is_key is True can't enter repeated value
            is_key is set to True by default
        '''
        assert LessonValidator.validate_lid('  ', self.lesson_list, is_required=True, is_key=True) is None
        assert LessonValidator.validate_lid('  ', self.lesson_list, is_required=False, is_key=True) is not None
        assert LessonValidator.validate_lid('12n1', self.lesson_list, is_required=True, is_key=True) is None
        assert LessonValidator.validate_lid('12n1', self.lesson_list, is_required=False, is_key=True) is None
        assert LessonValidator.validate_lid('201', self.lesson_list, is_required=True, is_key=True) is None
        assert LessonValidator.validate_lid('201', self.lesson_list, is_required=True, is_key=False) is not None

    def test_validate_name(self):
        assert LessonValidator.validate_lname('  ', is_required=True) is None
        assert LessonValidator.validate_lname('  ', is_required=False) is not None
        assert LessonValidator.validate_lname('na1me', is_required=True) is None
        assert LessonValidator.validate_lname('na1me', is_required=False) is None

    def test_validate_units(self):
        '''
            units must be number
            units must be between 1 and 8
        '''
        assert LessonValidator.validate_units('  ', is_required=True) is None
        assert LessonValidator.validate_units('  ', is_required=False) is not None
        assert LessonValidator.validate_units('1s1', is_required=True) is None
        assert LessonValidator.validate_units('0', is_required=True) is None
        assert LessonValidator.validate_units('9', is_required=True) is None
        assert LessonValidator.validate_units('8', is_required=True) is not None
        assert LessonValidator.validate_units('1', is_required=True) is not None
