if __name__ == "__main__":
    t = int(input().strip())
    series = [int((((1 + 5**0.5) / 2)**n - ((1 - 5**0.5) / 2)**n) / 5**0.5) for n in range(1, 1000)]
    lst = []
    for a0 in range(t):
        n = int(input().strip())
        lst += [sum([i for i in series if i < n and i % 2 == 0])]
    print(*lst, sep='\n')
