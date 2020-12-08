from .sentence import Sentence
from .parse import parse_sentences


class Inference:

    def __init__(self, conclusion: Sentence, premises: list):
        self.conclusion = conclusion
        self.premises = parse_sentences(premises)

    def is_valid_argument(self):
        self.conclusion.validate(set(self.premises))
