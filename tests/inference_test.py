import unittest

from dialectic import Inference, is_contradictory, Atomic


class InferenceTest(unittest.TestCase):
    a = Atomic('a')
    b = Atomic('b')

    def test_is_valid_argument(self):
        pass

    def test_is_tautology(self):
        pass

    def test_is_contradictory(self):
        pass

    def test_contingent(self):
        pass

    def test_is_contradictory_list(self):
        pass


if __name__ == '__main__':
    unittest.main()