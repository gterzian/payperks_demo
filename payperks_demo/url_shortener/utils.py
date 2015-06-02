import itertools
import string
import random

#not using o and 0 for easy typeability
LETTERS_AND_DIGITS = list(itertools.chain(string.letters.replace('o', ''), string.digits.replace('0', '')))
RANDOM_LETTERS = ''.join(random.sample(LETTERS_AND_DIGITS, len(LETTERS_AND_DIGITS)))

def short_string(length=4, already=None):
    if already is None:
        already = []
    for potential in itertools.permutations(RANDOM_LETTERS, length):
        potential_string = ''.join(potential)
        if potential_string not in already:
            return potential_string
        