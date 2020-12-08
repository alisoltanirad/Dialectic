import unittest

from dialectic import Inference, is_contradictory, Atomic


class InferenceTest(unittest.TestCase):
    a = Atomic('a')
    b = Atomic('b')

    def test_is_valid_argument(self):
        pass

    def test_is_tautology_true_1(self):
        assert Inference((self.a | (~self.a))).is_tautology() == True

    def test_is_tautology_true_2(self):
        assert Inference(((~self.a) | self.a)).is_tautology() == True

    def test_is_tautology_false_1(self):
        assert Inference((self.a | self.b)).is_tautology() == False

    def test_is_tautology_false_2(self):
        assert Inference((self.a | (~self.b))).is_tautology() == False

    def test_is_tautology_false_3(self):
        assert Inference((self.a & (~self.a))).is_tautology() == False

    def test_is_contradictory(self):
        pass

    def test_contingent(self):
        pass

    def test_is_contradictory_list(self):
        pass


if __name__ == '__main__':
    unittest.main()