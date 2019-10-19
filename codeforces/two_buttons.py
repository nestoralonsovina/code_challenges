
# we are going to go from m to n, instead of the reverse

n,m  = map(int, input().split())

cnt = 0
while n < m:
	if m % 2 != 0: 
		m += 1
	else:
		m = m // 2
	cnt += 1


print (cnt + n - m)