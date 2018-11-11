import unittest
import helpers.parsers as parsers

class TestConfiguration(unittest.TestCase):

    def test_parsers_target_list_single_net(self):
        self.assertEqual(['192.168.0.0/24'], parsers.target_list(['192.168.0.0/24']))

    def test_parsers_target_list_two_nets(self):
        self.assertEqual([
            '192.168.0.0/24',
            '192.168.1.0/24'
        ], 
        parsers.target_list(['192.168.0.0/23']))

    #def test_parsers_target_list_single_wrong_format(self):
    #    self.assertEqual(['192.168.0.1/32'], parsers.target_list(['192.168.0.1']))

if __name__ == '__main__':
    unittest.main()
