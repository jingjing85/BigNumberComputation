import unittest
import Computation


class TestComputation(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Computation.addition('10', '5'), '15')


if __name__ == '__main__':
    unittest.main()
