import unittest

import dialectic
from dialectic import (
    parse, Atomic, Invert, Conjunction, Disjunction, Implication, Equality
)



class ParseTest(unittest.TestCase):
    a = Atomic('a')
    b = Atomic('b')
    c = Atomic('c')

    def test_atomic_parse(self):
        assert parse([self.a]) == {'a'}

    def test_invert_parse_2(self):
        assert parse([(~self.a)]) == {~self.a}

    def test_conjunction_parse(self):
        assert parse([(self.a & self.b)]) == {'a', 'b'}

    def test_disjunction_parse_1(self):
        assert parse([(self.a | self.b)]) == set()

    def test_disjunction_parse_2(self):
        assert parse([(self.a | self.b), self.a]) == {'a'}

    def test_disjunction_parse_3(self):
        assert parse([(self.a | self.b), (~self.a)]) == {'b'}

    def test_implication_parse_1(self):
        assert parse([(self.a > self.b)]) == set()

    def test_implication_parse_2(self):
        assert parse([(self.a > self.b), self.b]) == {'b'}

    def test_implication_parse_3(self):
        assert parse([(self.a > self.b), self.a]) == {'a', 'b'}

    def test_equality_parse_1(self):
        assert parse([(self.a == self.b)]) == set()

    def test_equality_parse_2(self):
        assert parse([(self.a == self.b), self.a]) == {'a', 'b'}

    def test_equality_parse_3(self):
        assert parse([(self.a == self.b), self.b]) == {'a', 'b'}

    def test_equality_parse_4(self):
        assert parse([(self.a == self.b), (~self.a)]) == set()

    def test_equality_parse_5(self):
        assert parse([(self.a == self.b), (~self.b)]) == set()


if __name__ == '__main__':
    unittest.main()