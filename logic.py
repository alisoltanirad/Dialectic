# https://github.com/alisoltanirad/Logic.git

class Sentence:

    def __invert__(self):
        return Invert(self)

    def __and__(self, other):
        return Conjunction(self, other)

    def __or__(self, other):
        return Disjunction(self, other)

    def __gt__(self, other):
        return Implication(self, other)

    def __eq__(self, other):
        return Equality(self, other)


class BinarySentence(Sentence):

    def __init__(self, lchild, rchild):
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self):
        return '(' + self.lchild + ' ' + self.operator + ' ' + self.rchild +  ')'


class Atomic(Sentence):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def validate(self, set):
        return self in set


class Invert(Sentence):
    operator = '¬'

    def __init__(self, child):
        self.child = child

    def __str__(self):
        return self.operator + str(self.child)

    def validate(self, set):
        return not self.child.validate(set)


class Conjunction(BinarySentence):
    operator = '∧'

    def validate(self, set):
        return self.lchild.validate(set) and self.rchild.validate(set)


class Disjunction(BinarySentence):
    operator = '∨'

    def validate(self, set):
        return self.lchild.validate(set) or self.rchild.validate(set)


class Implication(BinarySentence):
    operator = '→'

    def validate(self, set):
        return not self.lchild.validate(set) or self.rchild.validate(set)


class Equality(BinarySentence):
    operator = '↔'

    def validate(self, set):
        return self.lchild.validate(set) is self.rchild.validate(set)


def main():
    pass


if __name__ == '__main__':
    main()