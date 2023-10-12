def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    left = 0
    right = len(people) - 1
    
    while left <= right :
        if people[left] + people[right] <= limit :
            right -= 1
        left += 1
        answer += 1
    
    return answer

'''
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    left = 0
    right = len(people) - 1
    
    while True :
        cnt = people[left]
        while True :
            if left == right or cnt + people[right] > limit :
                answer += 1
                break
            cnt += people[right]
            right -= 1
        if left == right :
            break
        left += 1
    
    return answer
'''