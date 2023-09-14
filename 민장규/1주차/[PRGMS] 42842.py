def solution(brown, yellow):
    r, c = 1, 1
    while not(r * c == brown + yellow and (r * 2) + ((c - 2) * 2) == brown) :
        c += 1
        r = (brown + yellow) // c
    return [r, c]