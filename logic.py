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

    def infer(self, set):
        simple_set = self.simplify(set)
        return self.validate(set)

    def simplify(self, input_set):
        simple_set = set()
        while input_set:
            sentence = input_set.pop()
            print(sentence)

            if type(sentence) is (Atomic or Invert):
                simple_set.add(sentence)

            if type(sentence) is Conjunction:
                input_set.add(sentence.lchild)
                input_set.add(sentence.rchild)

            if type(sentence) is Disjunction:
                if (~sentence.lchild).validate(input_set | simple_set):
                    input_set.add(sentence.rchild)
                if (~sentence.rchild).validate(input_set | simple_set):
                    input_set.add(sentence.lchild)

        return simple_set


class BinarySentence(Sentence):

    def __init__(self, lchild, rchild):
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self):
        return '(' + str(self.lchild) + ' ' + \
               self.operator + \
               ' ' + str(self.rchild) +  ')'


class Atomic(Sentence):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def __hash__(self):
        return hash(self.name)

    def validate(self, set):
        return self in set


class Invert(Sentence):
    operator = '¬'

    def __init__(self, child):
        self.child = child

    def __str__(self):
        return self.operator + str(self.child)

    def __hash__(self):
        return hash(not self.child)

    def validate(self, set):
        return (not self.child) in set


class Conjunction(BinarySentence):
    operator = '∧'

    def __hash__(self):
        return hash(self.lchild and self.rchild)

    def validate(self, set):
        return self.lchild.validate(set) and self.rchild.validate(set)


class Disjunction(BinarySentence):
    operator = '∨'

    def __hash__(self):
        return hash(self.lchild or self.rchild)

    def validate(self, set):
        return self.lchild.validate(set) or self.rchild.validate(set)


class Implication(BinarySentence):
    operator = '→'

    def __hash__(self):
        return hash(not self.lchild or self.rchild)

    def validate(self, set):
        return not self.lchild.validate(set) or self.rchild.validate(set)


class Equality(BinarySentence):
    operator = '↔'

    def __hash__(self):
        return hash((self.lchild and self.rchild) or
                    (not self.lchild and not self.rchild))

    def validate(self, set):
        return self.lchild.validate(set) is self.rchild.validate(set)


def main():
    a = Atomic('a')
    b = Atomic('b')
    print(a.simplify({(a | b), ~a}))


if __name__ == '__main__':
    main()