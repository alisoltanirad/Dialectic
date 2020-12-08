import unittest

import dialectic
from dialectic import (
    parse_sentences, Atomic
)



class ParseTest(unittest.TestCase):
    a = Atomic('a')
    b = Atomic('b')
    c = Atomic('c')

    def test_atomic_parse(self):
        assert parse_sentences([self.a]) == {'a'}

    def test_invert_parse_2(self):
        assert parse_sentences([(~self.a)]) == {~self.a}

    def test_conjunction_parse(self):
        assert parse_sentences([(self.a & self.b)]) == {self.a, self.b}

    def test_disjunction_parse_1(self):
        assert parse_sentences([(self.a | self.b)]) == set()

    def test_disjunction_parse_2(self):
        assert parse_sentences([(self.a | self.b), self.a]) == {self.a}

    def test_disjunction_parse_3(self):
        assert parse_sentences([(self.a | self.b), (~self.a)]) == {(~self.a), self.b}

    def test_implication_parse_1(self):
        assert parse_sentences([(self.a > self.b)]) == set()

    def test_implication_parse_2(self):
        assert parse_sentences([(self.a > self.b), self.b]) == {self.b}

    def test_implication_parse_3(self):
        assert parse_sentences([(self.a > self.b), self.a]) == {self.a, self.b}

    def test_equality_parse_1(self):
        assert parse_sentences([(self.a == self.b)]) == set()

    def test_equality_parse_2(self):
        assert parse_sentences([(self.a == self.b), self.a]) == {self.a, self.b}

    def test_equality_parse_3(self):
        assert parse_sentences([(self.a == self.b), self.b]) == {self.a, self.b}

    def test_equality_parse_4(self):
        assert parse_sentences([(self.a == self.b), (~self.a)]) == {(~self.a), (~self.b)}

    def test_equality_parse_5(self):
        assert parse_sentences([(self.a == self.b), (~self.b)]) == {(~self.a), (~self.b)}


if __name__ == '__main__':
    unittest.main()