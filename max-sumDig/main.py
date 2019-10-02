import sys
sys.path.append("..")

from Test import Test as test

def max_sumDig(nMax, maxSum):
    for nbr in range(1000, nMax):
        nbr = str(nbr)
        



test.describe("Example tests")
test.it("nMax = " + str(2000))
test.it("maxSum = " + str(3))
test.assert_equals(max_sumDig(2000, 3), [11, 1110, 12555])
test.it("nMax = " + str(2000))
test.it("maxSum = " + str(4))
test.assert_equals(max_sumDig(2000, 4), [21, 1120, 23665])
test.it("nMax = " + str(2000))
test.it("maxSum = " + str(7))
test.assert_equals(max_sumDig(2000, 7), [85, 1200, 99986])
test.it("nMax = " + str(3000))
test.it("maxSum = " + str(7))
test.assert_equals(max_sumDig(3000, 7), [141, 1600, 220756])
test.it("nMax = " + str(4000))
test.it("maxSum = " + str(4))
test.assert_equals(max_sumDig(4000, 4), [35, 2000, 58331])

