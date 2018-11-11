import unittest
import helpers.config as config

class TestConfiguration(unittest.TestCase):

    def test_config_default(self):
        self.assertEqual({'queue': 'local'}, config.default_config())

    def test_config_parse_targets_normal(self):
        self.assertEqual(['127.0.0.1', 
                          '172.24.1.1/16', 
                          '192.168.1.1/24'
                         ], 
                         config.parse_targets(
                             "127.0.0.1\n172.24.1.1/16\n192.168.1.1/24"
                             ))

    def test_config_parse_targets_extra_characters(self):
        self.assertEqual(['127.0.0.1', 
                          '172.24.1.1/16', 
                          '192.168.1.1/24'
                         ], 
                         config.parse_targets(
                             "127.0.0.*1\n17sdf2.24.1.1/16\n192.ld168.1.1/24"
                             ))

    def test_config_validate_targets(self):
        self.assertEqual(['127.0.0.1', '172.24.1.1/16'], 
                         config.validate_targets(['127.0.0.1', '172.24.1.1/16']))

    def test_config_validate_targets_mask_one(self):
        self.assertRaises(ValueError, config.validate_targets, ['172.24.1.1/33'])

    def test_config_validate_targets_mask_two(self):
        self.assertRaises(ValueError, config.validate_targets, ['172.24.1.1/7'])

if __name__ == '__main__':
    unittest.main()
