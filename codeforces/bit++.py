
value = 0

n = int(input())

for i in range(n):
	s = input()
	if "++" in s:
		value += 1
	elif "--" in s:
		value -= 1

print(value)