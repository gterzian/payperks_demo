import itertools
import string
import random



RANDOM_LETTERS = ''.join(random.sample(string.letters, len(string.letters)))


def short_string(already=None):
    if already is None:
        already = []
    for potential in itertools.permutations(RANDOM_LETTERS, 4):
        potential_string = ''.join(potential)
        if potential_string not in already:
            return potential_string
        