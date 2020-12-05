import unittest

from dialectic import (
    Atomic, Invert, Conjunction, Disjunction, Implication, Equality
)



class ParseTest(unittest.TestCase):
    a = Atomic('a')
    b = Atomic('b')
    c = Atomic('c')

    def test_atomic_parse(self):
        assert self.a.parse() == {'a'}
