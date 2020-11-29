# https://github.com/alisoltanirad/Logic.git

class Sentence:

    def __invert__(self):
        return Inverse(self)

    def __and__(self, other):
        return Conjunction(self, other)

    def __or__(self, other):
        return Disjunction(self, other)

    def __gt__(self, other):
        return Implication(self, other)

    def __eq__(self, other):
        return Equality(self, other)


class Atomic(Sentence):
    pass


class Inverse(Sentence):
    pass


class Conjunction(Sentence):
    pass


class Disjunction(Sentence):
    pass


class Implication(Sentence):
    pass


class Equality(Sentence):
    pass


def main():
    pass


if __name__ == '__main__':
    main()