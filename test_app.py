# test_app.py
import unittest

class TestApp(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)

    def test_case_2(self):
        self.assertEqual(2 * 2, 4)

    def test_case_3(self):
        self.assertTrue('Hello' in 'Hello, World!')

    def test_case_4(self):
        self.assertEqual(3 / 0, 1)  # This will fail

    def test_case_5(self):
        self.assertTrue(False)  # This will also fail

if __name__ == '__main__':
    unittest.main()
