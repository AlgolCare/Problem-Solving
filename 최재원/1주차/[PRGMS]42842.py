def solution(brown, yellow):
    a = []
    if brown < 8 or yellow < 1:
        return
    
    if yellow == 1 :
        answer = [3, 3]
        return answer
    if yellow == 2 and brown > 9 :
        answer = [4, 3]
        return answer
    
    for i in range(1, yellow+1):
        n = yellow % i 
        if n == 0 :
            a.append(i)
    
    b = len(a)
    
    if b % 2 == 0:
        answer = [a[b//2] + 2, a[b//2-1] + 2]
    else:
        answer = [a[b//2] + 2, a[b//2] + 2]
        
        
    if yellow == ( answer[0] - 2 ) *( answer[1] - 2 ) and answer[0] >= answer[1] :
        if brown >= (yellow + 2) * 2 + 2 :
            answer = [yellow + 2, 3]
            return answer
        if brown >= (answer[0] + answer[1]) * 2 - 4:
                return answer
        
    
print(solution(24, 25))
