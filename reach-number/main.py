import sys
sys.path.append("..")

from Test import Test
from collections import deque

def reachNumber(target: int) -> int:
    if target == 0:
        return target

    nb_steps = 1
    q = deque()
    q.append(0)
    while True:
        nq = deque()
        while len(q) != 0:
            e = q.popleft()
            if e + nb_steps == target or e - nb_steps == target:
                return nb_steps
            else:
                nq.append(e + nb_steps)
                nq.append(e - nb_steps)
        q = nq
        nb_steps += 1



Test.assert_equals(reachNumber(3), 2)
Test.assert_equals(reachNumber(2), 3)

