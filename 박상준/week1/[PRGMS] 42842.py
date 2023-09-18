from math import sqrt, floor

def solution(brown, yellow):
    answer = []
    xy = []
    for i in range(1, int(yellow**(1/2)) + 1):
        if yellow % i == 0:
            xy.append([yellow // i, i])
            
    for item in xy:
        if brown == 2 * item[0] + 2 * item[1] + 4:
            answer = [item[0] + 2, item[1] + 2]
    
    return answer