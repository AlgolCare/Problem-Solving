def solution(brown, yellow):
    a = []
    if brown < 8 or yellow < 1:
        return
    
    if yellow == 1:
        return [3, 3]
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            a.append(i)
    b = len(a)
    
    if b % 2 == 1 and (a[b//2] + 2) * 2 + (a[b//2] * 2) == brown:
        return [a[b//2] + 2, a[b//2] + 2 ]
    elif ( yellow + 2 ) * 2 + 2 == brown:
        return [yellow + 2, 3]
    else:
        for i in range((b // 2)):
            if ((a[b - i - 1] + 2) * 2) + (a[i] * 2) == brown:
                return [a[b - i - 1] + 2, a[i] + 2]

print(solution(24, 16))
