import itertools

n = int(input())


print(
	len(list(itertools.permutations(list(range(n)), n))) + 1
	)
