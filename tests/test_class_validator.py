from school_manager.validator import ClassValidator
from school_manager.models import Class
from school_manager.storage_handler import ClassFH

class TestClassValidator:

    def setup_method(self):
        self.class_list = []
        ClassFH.load_file(Class, self.class_list)

    def test_validate_id(self):
        '''
            if is_key is True can't enter repeated value
            is_key is set to True by default
        '''
        assert ClassValidator.validate_cid('   ', self.class_list, is_required=True) is None
        assert ClassValidator.validate_cid('   ', self.class_list, is_required=False) is not None
        assert ClassValidator.validate_cid('12s2', self.class_list, is_required=True) is None
        assert ClassValidator.validate_cid('101', self.class_list, is_required=True) is None
        assert ClassValidator.validate_cid('101', self.class_list, is_required=True, is_key=False) is not None

    def test_validate_name(self):
        assert ClassValidator.validate_cname('  ', is_required=True) is None
        assert ClassValidator.validate_cname('  ', is_required=False) is not None
        assert ClassValidator.validate_cname('nam1e', is_required=True) is None
        assert ClassValidator.validate_cname('nam1e', is_required=False) is None

    def test_validate_capacity(self):
        assert ClassValidator.validate_capacity('  ', is_required=True) is None
        assert ClassValidator.validate_capacity('  ', is_required=False) is not None
        assert ClassValidator.validate_capacity('12n1', is_required=True) is None
        assert ClassValidator.validate_capacity('12n1', is_required=False) is None
