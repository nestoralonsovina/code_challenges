
s = input().lower()

res = []

for i, c in enumerate(s):
	if c in "aeiou":
		continue
	else:
		res.append('.' + c)

print(''.join(res))