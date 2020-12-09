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

    def test_is_contradictory_true_1(self):
        assert Inference((self.a & (~self.a))).is_contradictory() == True

    def test_is_contradictory_true_2(self):
        assert Inference(((~self.a) & self.a)).is_contradictory() == True

    def test_is_contradictory_true_3(self):
        assert Inference((self.a & (~~~self.a))).is_contradictory() == True

    def test_is_contradictory_false_1(self):
        assert Inference((self.a)).is_contradictory() == False

    def test_is_contradictory_false_2(self):
        assert Inference((self.a | (~self.a))).is_contradictory() == False

    def test_contingent_true(self):
        assert Inference((self.a)).is_contingent() == True

    def test_contingent_false_1(self):
        assert Inference((self.a | (~self.a))).is_contingent() == False

    def test_contingent_false_2(self):
        assert Inference((self.a & (~self.a))).is_contingent() == False

    def test_is_contradictory_list(self):
        pass


if __name__ == '__main__':
    unittest.main()