from school_manager.validator import RCValidator

class TestRCValidator:

    def test_validate_sid(self):
        assert RCValidator.validate_sid('  ') is None
        assert RCValidator.validate_sid('5001') is not None

    def test_validate_grade(self):
        '''
            grade must be between 0 and 20.
            grade always required
        '''
        assert RCValidator.validate_grade('  ') is None
        assert RCValidator.validate_grade('1i9') is None
        assert RCValidator.validate_grade(-1) is None
        assert RCValidator.validate_grade(21) is None
        assert RCValidator.validate_grade(1) is not None
        assert RCValidator.validate_grade(20) is not None
