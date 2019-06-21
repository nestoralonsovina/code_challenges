def dbl_linear(n: int) -> int:

    # lambda functions to calculate each
    calc_x = lambda x: (2 * x) + 1
    calc_y = lambda x: (3 * x) + 1
    x = 0
    y = 0
    u = [1]
    for i in range(n):
        nextX = calc_x(u[x])
        nextY = calc_y(u[y])
        if nextX <= nextY:
            u.append(nextX)
            x += 1
            if nextX == nextY:
                y += 1
        else:
            u.append(nextY)
            y += 1
    print(u)
    return u[n]
    
assert dbl_linear(10) == 22
assert dbl_linear(20) == 57
assert dbl_linear(30) == 91
assert dbl_linear(50) == 175
