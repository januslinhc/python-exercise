import builtins
import unittest

import ex3_5


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        input_value = "1\n2\n1\n3\n2\n3"
        expected = "1/4"
        self.common_test(input_value, expected)

    def test_case_2(self):
        input_value = "3\n6\n1\n6\n4\n9"
        expected = "3/4"
        self.common_test(input_value, expected)

    def common_test(self, input_value, expected):
        original_input = builtins.input
        builtins.input = lambda: input_value
        actual = ex3_5.handle()
        self.assertEqual(expected, actual)
        builtins.input = original_input


if __name__ == '__main__':
    unittest.main()
