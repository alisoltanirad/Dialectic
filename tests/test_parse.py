import pytest

from dialectic import (
    Atomic, Invert, Conjunction, Disjunction, Implication, Equality
)


def test_atomic_parse():
    assert Atomic('a').parse() == {'a'}