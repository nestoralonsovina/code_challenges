import sys
sys.path.append("..")

from Test import Test
from typing import List
from itertools import combinations

def maxProduct_v1(words: List[str]) -> int:
    max_length = 0
    comb = combinations(words, 2)
    for pair in comb:
        rep = map(lambda x: x in pair[1], pair[0])
        if any(rep) == False:
            max_length = max(max_length, len(pair[1]) * len(pair[0]))
    return max_length

def maxProduct_v2(words: List[str]) -> int:
    iterations = 0
    max_length = 0
    s = set()
    for w1 in words:
        for w2 in words:
            if w1 is w2 or (w1, w2) in s or (w2, w1) in s:
                continue
            iterations += 1
            rep = map(lambda x: x in w2, w1)
            if any(rep) == False:
                max_length = max(max_length, len(w1) * len(w2))
            s.add((w1, w2))
    return max_length

def maxProduct_v3(words: List[str]) -> int:
    pass



Test.assert_equals(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]), 16)
Test.assert_equals(maxProduct(["a","ab","abc","d","cd","bcd","abcd"]), 4)
Test.assert_equals(maxProduct(["a","aa","aaa","aaaa"]), 0)
