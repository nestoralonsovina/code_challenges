import string
alpha = string.ascii_lowercase
def print_rangoli(size):
    L = []
    for i in range(size):
        s = alpha[i:size]
        s = '-'.join(s[::-1] + s[1:])
        L.append(s)
    width = max([len(x) for x in L])
    L = list(map(lambda x: x.center(width, '-'), L))
    L.reverse()
    print(*L, sep='\n')
    L.reverse()
    L = L[1:]
    print(*L, sep='\n')
print_rangoli(26)
