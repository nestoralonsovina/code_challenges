import math

n, m, a = map(float, input().split())

print ( math.ceil(m / a) * math.ceil(n / a))