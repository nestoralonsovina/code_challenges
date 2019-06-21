def compareTriplets(a, b):
    res = [0, 0]
    for _ in zip(a, b):
        if a > b:
            res[0] += 1
        elif b > a:
            res[1] += 1
    return res
