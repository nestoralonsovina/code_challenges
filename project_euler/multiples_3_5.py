import sys

def sum_factors_of_n_below_k(k, n):
    m = (k-1) // n
    return n * m * (m+1) // 2

def solution_01():
    return (sum_factors_of_n_below_k(1000, 3) +
            sum_factors_of_n_below_k(1000, 5) -
            sum_factors_of_n_below_k(1000, 15))
t = int(input().strip())
for _ in range(t):
    end = int(input())
    print(sum_factors_of_n_below_k(end, 3) +
            sum_factors_of_n_below_k(end, 5) -
            sum_factors_of_n_below_k(end, 15))
