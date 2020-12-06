import unittest

from dialectic import (
    Atomic, Invert, Conjunction, Disjunction, Implication, Equality, SentenceSet
)



class ParseTest(unittest.TestCase):
    a = Atomic('a')
    b = Atomic('b')
    c = Atomic('c')

    def test_atomic_parse(self):
        assert SentenceSet({self.a}).parse() == {'a'}

    def test_invert_parse(self):
        assert SentenceSet({(~self.a)}).parse() == {~self.a}

    def test_conjunction_parse(self):
        assert SentenceSet({(self.a & self.b)}).parse() == {'a', 'b'}

    def test_disjunction_parse_1(self):
        assert SentenceSet({(self.a | self.b)}).parse() == {}

    def test_disjunction_parse_2(self):
        assert SentenceSet({(self.a | self.b), self.a}).parse() == {'a'}

    def test_disjunction_parse_3(self):
        assert SentenceSet({(self.a | self.b), (~self.a)}).parse() == {'b'}

    def test_implication_parse_1(self):
        assert SentenceSet({(self.a > self.b)}).parse() == {}

    def test_implication_parse_2(self):
        assert SentenceSet({(self.a > self.b), self.b}).parse() == {'b'}

    def test_implication_parse_3(self):
        assert SentenceSet({(self.a > self.b), self.a}).parse() == {'a', 'b'}

    def test_equality_parse_1(self):
        assert SentenceSet({(self.a == self.b)}).parse() == {}

    def test_equality_parse_2(self):
        assert SentenceSet({(self.a == self.b), self.a}).parse() == {'a', 'b'}

    def test_equality_parse_3(self):
        assert SentenceSet({(self.a == self.b), self.b}).parse() == {'a', 'b'}

    def test_equality_parse_4(self):
        assert SentenceSet({(self.a == self.b), (~self.a)}).parse() == {}

    def test_equality_parse_5(self):
        assert SentenceSet({(self.a == self.b), (~self.b)}).parse() == {}


if __name__ == '__main__':
    unittest.main()