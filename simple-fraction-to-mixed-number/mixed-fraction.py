def largest_common_factor(numer: int, denom: int) -> int:
    for i in range(min(abs(numer), abs(denom)), 1, -1):
        if numer % i == 0 and denom % i == 0:
            return i
    return 0

def mixed_fractions(number: str) -> str:
    up, down = map(int, number.split('/'))
    negative = 0
    full_parts = 0

    if up % down == 0:
        return str(up // down)

    if up < 0:
        up = abs(up)
        negative = 1 
    if down < 0:
        down = abs(down)
        negative += 1

    if negative == 2:
        negative = 0

    while up / down > 1:
        full_parts += 1
        up -= down

    factor = largest_common_factor(up, down)
    if factor != 0:
        up //= factor
        down //= factor

    if negative != 0:
        full_parts *= -1

    if full_parts == 0:
        return str(up) + "/" + str(down)


    return str(full_parts) + " " + str(up) + "/" + str(down)


assert mixed_fractions('42/9') == '4 2/3'
assert mixed_fractions('6/3') == '2'
assert mixed_fractions('0/18891') == '0'
assert mixed_fractions('4/6') == '2/3'
assert mixed_fractions('-10/7') ==  '-1 3/7'
assert mixed_fractions('-22/-7') == '3 1/7'
