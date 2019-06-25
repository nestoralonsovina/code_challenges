import sys
sys.path.append("..")

from Test import Test
import math

K = math.pi * math.sqrt(2/3)

def exp_sum(n):
    arr = [0 for i in range(n + 1)]
    arr[0] = 1
    k = 1
    while k <= n:
        i = 0
        while i + k <= n:
            arr[i + k] += arr[i]
            i += 1
        k += 1
    return arr[n]



Test.assert_equals(exp_sum(1), 1)
Test.assert_equals(exp_sum(2), 2)
Test.assert_equals(exp_sum(3), 3)
Test.assert_equals(exp_sum(4), 5)
Test.assert_equals(exp_sum(5), 7)
Test.assert_equals(exp_sum(10), 42)
