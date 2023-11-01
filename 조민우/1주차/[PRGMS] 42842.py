def solution(brown, yellow):
    answer = []
    root = int(yellow**(1/2))
    num = 1
    for i in range(1, root+1):
        if (yellow%i == 0):
            num = yellow // i
            if ((num+2) * (i + 2) - yellow == brown):
                answer.append(num+2)
                answer.append(i+2)
                return answer