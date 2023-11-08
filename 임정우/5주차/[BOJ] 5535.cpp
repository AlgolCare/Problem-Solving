#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int n, d;
int temp[201], min_temp[201], max_temp[201], att[201], dp[101][201];

// 재귀를 사용한 DP
int solve(int a, int day) {
    // d 날짜가 됐다면 return
    if (day == d)
        return 0;
    // 메모이제이션 활용
    if (dp[a][day] != -1)
        return dp[a][day];
    int ret = 0;
    // 전체 옷들을 순회한 후 가장 큰 값을 return 값으로 사용
    for (int i = 0; i < n; i++) {
        if (temp[day] < min_temp[i] || temp[day] > max_temp[i])
            continue;
        int temp_value = solve(att[i], day + 1) + abs(a - att[i]);
        ret = max(ret, temp_value);
    }
    return dp[a][day] = ret;
}

int main() {
    cin >> d >> n;
    for (int i = 0; i < d; i++) cin >> temp[i];
    for (int i = 0; i < n; i++) cin >> min_temp[i] >> max_temp[i] >> att[i];
    memset(dp, -1, sizeof(dp));
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (temp[0] < min_temp[i] || temp[0] > max_temp[i])
            continue;
        int temp_value = solve(att[i], 1);
        ans = max(ans, temp_value);
    }
    cout << ans;
    return 0;
}
