# Check if a word is a pangram or not. Pangram are sentences that 
# contains every word of alphabet at least once

import string
from unittest import result


def pangram(sentence, alphabet=string.ascii_lowercase):
    return set(sentence.replace(' ', '').lower()) == set(alphabet)

result1 = pangram('The quick brown fox jumps over the lazy dog')
print(result1)