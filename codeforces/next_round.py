n, k = map(int, input().split())

arr = list(map(int, input().split()))

k = arr[k - 1]

requirements = lambda x: x > 0 and x >= k;

print(len(list(filter(requirements, arr))))
