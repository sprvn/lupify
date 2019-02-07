import unittest
import helpers.validators as validators

class TestConfiguration(unittest.TestCase):

    def test_string_validation_with_valid_string(self):
        self.assertEqual('astring', validators.string('astring'))

    def test_string_validation_with_non_valid_string(self):
        self.assertEqual(False, validators.string('astring123'))

    def test_string_validation_with_special_characters(self):
        self.assertEqual(False, validators.string('!"#¤%&/()=?*"^'))

    def test_integer_with_number(self):
        self.assertEqual(12345, validators.integer('12345'))

    def test_integer_with_float(self):
        self.assertEqual(False, validators.integer('123.5'))

    def test_integer_with_string(self):
        self.assertEqual(False, validators.integer('astring'))

    def test_integer_with_special_characters(self):
        self.assertEqual(False, validators.integer('!"#¤%&/()=?*"^'))

    def test_user_with_string(self):
        self.assertEqual('username', validators.username('username'))

    def test_user_with_underscore(self):
        self.assertEqual('user_name', validators.username('user_name'))

    def test_user_with_special_characters(self):
        self.assertEqual(False, validators.username('user_name!"#¤%&/()=?*"^'))

    def test_ip_with_ipv4(self):
        self.assertEqual('192.168.1.1', validators.ip('192.168.1.1'))

    def test_ip_with_string(self):
        self.assertEqual(False, validators.ip('a string'))

    def test_ip_with_integer(self):
        self.assertEqual(False, validators.ip(12345))

    def test_target_with_ip(self):
        self.assertEqual('127.0.0.1', validators.target('127.0.0.1'))

    def test_target_with_cidr(self):
        self.assertEqual('127.0.0.1/32', validators.target('127.0.0.1/32'))

    def test_target_with_invalid_cidr(self):
        self.assertEqual(False, validators.target('127.0.0.1/33'))

    def test_target_with_special_characters(self):
        self.assertEqual(False, validators.target('!"#¤%&/()=?*"^'))

if __name__ == '__main__':
    unittest.main()
