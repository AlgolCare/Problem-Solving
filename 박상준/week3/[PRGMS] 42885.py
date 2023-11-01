def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    rear = len(people) - 1 
    
    for i in range(len(people)):
        if i >= rear:
            if i == rear:
                answer += 1
            break
        if people[i] + people[rear] <= limit:
            rear -= 1
        answer += 1
    
    return answer