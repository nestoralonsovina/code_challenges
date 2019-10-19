n = int(input())

sol = 0

for i in range(n):
	arr = list(map(int, input().split()))
	if arr.count(1) >= 2:
		sol += 1

print (sol)