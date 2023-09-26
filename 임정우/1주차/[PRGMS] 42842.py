def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total + 1):
        if total % i == 0:
            y,x = i,total // i
            if (y - 2) * (x - 2) == yellow:
                answer.append(x)
                answer.append(y)
                break
    return answer