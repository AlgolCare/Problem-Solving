def solution(triangle):
    if len(triangle) == 1 :
        return triangle[0][0]
    
    dp = [[triangle[0][0]]]
    for i, row in enumerate(triangle[1:]) :
        i += 2
        dp_ = [0 for _ in range(i)]
        for j in range(i) :
            if j == 0 :
                dp_[j] = dp[i-2][j] + triangle[i-1][j]
            elif j == i-1 :
                dp_[j] = dp[i-2][j-1] + triangle[i-1][j]
            else :
                dp_[j] = max(dp[i-2][j-1], dp[i-2][j]) + triangle[i-1][j]
        dp.append(dp_)
        
    return max(dp[-1])