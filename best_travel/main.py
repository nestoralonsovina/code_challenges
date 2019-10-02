import sys
sys.path.append("..")

from Test import Test
from typing import List

import itertools

def choose_best_sum(t: int, k:int , ls: List[int]) -> int:
    best = 0
    for c in itertools.combinations(ls, k):
        if best < sum(c) <= t:
            best = sum(c)
    return best if best else None

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
ls = [50, 55, 57, 58, 60]

Test.assert_equals(choose_best_sum(174, 3, ls), 173)
Test.assert_equals(choose_best_sum(230, 4, xs), 230)
Test.assert_equals(choose_best_sum(430, 5, xs), 430)
Test.assert_equals(choose_best_sum(430, 8, xs), None)
