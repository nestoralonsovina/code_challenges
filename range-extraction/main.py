from sys import path
path.append("..")

from Test import Test
from typing import List

def solution(args: List) -> str:
    sol = ''
    prev = None
    r = iter(range(len(args) - 1))
    for i in r:
        if args[i] + 1 == args[i + 1]:
            if prev is None:
                prev = args[i]
            continue
        else:
            if prev == None:
                sol += str(args[i])
            elif prev + 1 == args[i]:
                sol += str(prev)
                sol += ','
                sol += str(args[i])
                prev = None
            else:
                sol += str(prev) + '-' + str(args[i])
                prev = None
            sol += ','

    sol += str(prev) + '-' + str(args[-1])
    return sol


Test.describe("Sample Test Cases")

Test.it("Simple Tests")
Test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
Test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
