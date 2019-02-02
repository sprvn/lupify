import unittest
import helpers.config as config

class TestConfiguration(unittest.TestCase):

    def test_config_default(self):
        self.assertEqual({'queue': 'local'}, config.default_config())


if __name__ == '__main__':
    unittest.main()
