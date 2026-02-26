from school_manager.validator import StudentValidator
from school_manager.models import Student, Class
from school_manager.storage_handler import StudentFH, ClassFH

class TestStudentValidator:
    
    def setup_method(self):
        self.student_list = []
        self.class_list = []
        StudentFH.load_file(Student, self.student_list)
        ClassFH.load_file(Class, self.class_list)
        
    def test_validate_id(self):
        '''
            all type ids must be a number
            student id must be a number and when the is_key is True student id can't be repeated
            if type=national it validates national ids
            national id must be 10 digits
        '''
        assert StudentValidator.validate_id('10001', self.student_list, obj_type='student', is_required=True, is_key=True) is None
        assert StudentValidator.validate_id('10001', self.student_list, obj_type='student', is_required=True, is_key=False) is not None
        assert StudentValidator.validate_id('10a001', self.student_list, obj_type='student', is_required=True, is_key=True) is None
        assert StudentValidator.validate_id('', self.student_list, obj_type='student', is_required=True, is_key=True) is None
        assert StudentValidator.validate_id('', self.student_list, obj_type='student', is_required=False, is_key=True) is not None
        assert StudentValidator.validate_id('100023', self.student_list, obj_type='student', is_required=True, is_key=True) == 100023
        assert type(StudentValidator.validate_id('100023', self.student_list, obj_type='student', is_required=True, is_key=True)) == int
        assert StudentValidator.validate_id('', self.student_list, obj_type='student', is_required=True, is_key=True, type='national') is None
        assert StudentValidator.validate_id('', self.student_list, obj_type='student', is_required=False, is_key=True, type='national') is not None
        assert StudentValidator.validate_id('123s13', self.student_list, obj_type='student', is_required=True, is_key=True, type='national') is None
        assert StudentValidator.validate_id('123456789', self.student_list, obj_type='student', is_required=True, is_key=True, type='national') is None
        assert StudentValidator.validate_id('1234567890', self.student_list, obj_type='student', is_required=True, is_key=True, type='national') is not None
    
    
    def test_validate_name(self):
        assert StudentValidator.validate_name('mat1n', is_required=True) is None
        assert StudentValidator.validate_name('', is_required=True) is None
        assert StudentValidator.validate_name('', is_required=False) is not None
        assert StudentValidator.validate_name('matin', is_required=True) == 'matin'
    
    def test_validate_age(self):
        '''
            age must be between min and max
            age must be a number
        '''
        assert StudentValidator.validate_age('19', min=10, max=18) is None
        assert StudentValidator.validate_age('9', min=10, max=18) is None
        assert StudentValidator.validate_age('12', min=10, max=18) is not None
        assert StudentValidator.validate_age('12', min=10, max=18) == 12
        assert StudentValidator.validate_age('', min=10, max=18) == ''
        assert StudentValidator.validate_age('', min=10, max=18, is_required=True) is None
    
    def test_validate_gl(self):
        # grade level must be a number and must be between 10 and 12
        assert StudentValidator.validate_gl('a11', is_required=True) is None
        assert StudentValidator.validate_gl('5', is_required=True) is None
        assert StudentValidator.validate_gl('13', is_required=True) is None
        assert StudentValidator.validate_gl('', is_required=True) is None
        assert StudentValidator.validate_gl('', is_required=False) is not None
        assert StudentValidator.validate_gl('11', is_required=True) is not None
        assert StudentValidator.validate_gl('11', is_required=True) == 11
        assert StudentValidator.validate_gl('11', is_required=False) == 11
        assert type(StudentValidator.validate_gl('11', is_required=True)) == int
        assert type(StudentValidator.validate_gl('11', is_required=False)) == int
        
    def test_validate_cid(self):
        '''
            class id must exist in classes list
            class id must be number
        '''
        assert StudentValidator.validate_cid('   ', [int(cls.class_id) for cls in self.class_list], is_required=True) is None
        assert StudentValidator.validate_cid(' ', [int(cls.class_id) for cls in self.class_list], is_required=False) is  not None
        assert StudentValidator.validate_cid('1s123', [int(cls.class_id) for cls in self.class_list], is_required=True) is None
        assert StudentValidator.validate_cid('101', [int(cls.class_id) for cls in self.class_list], is_required=True) is not None
        assert StudentValidator.validate_cid('101', [int(cls.class_id) for cls in self.class_list], is_required=False) is not None
