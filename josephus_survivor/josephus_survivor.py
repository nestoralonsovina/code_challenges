import sys
sys.path.append("..")

from Test import Test

from collections import deque

def josephus_survivor(n,k):
    item = range(1, n + 1)
    k_range = range(1, k)
    q = deque(item)
    while len(q) > 1:
        for i in k_range:
            q.rotate(-1)
        q.popleft()
    return q.pop()

Test.assert_equals(josephus_survivor(7,3),4)
Test.assert_equals(josephus_survivor(11,19),10)
Test.assert_equals(josephus_survivor(1,300),1)
Test.assert_equals(josephus_survivor(14,2),13)
Test.assert_equals(josephus_survivor(100,1),100)
