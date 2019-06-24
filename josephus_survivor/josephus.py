import sys
sys.path.append("..")

from Test import Test

from collections import deque

def josephus(item, k):
    dead = []
    q = deque(item)
    i = 1
    while len(q) >= 1:
        if i % k == 0:
            dead.append(q.popleft())
        else:
            q.rotate(-1)
        i += 1
    return dead




Test.assert_equals(josephus([1,2,3,4,5,6,7,8,9,10],1),[1,2,3,4,5,6,7,8,9,10])
Test.assert_equals(josephus([1,2,3,4,5,6,7,8,9,10],2),[2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
Test.assert_equals(josephus(["C","o","d","e","W","a","r","s"],4),['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])
Test.assert_equals(josephus([1,2,3,4,5,6,7],3),[3, 6, 2, 7, 5, 1, 4])
Test.assert_equals(josephus([],3),[])

