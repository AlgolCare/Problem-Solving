#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

int days=0, clothes=0, result=0;
int temperture[201], attribute[201], dp[201][201];

int main(){
    cin>>days>>clothes;
    for(int i = 0; i <= days; i++) {
        for(int j = 0; j <= clothes; j++) {
            dp[i][j] = -1;
        }
    }
    for(int i=1; i<=days; i++){
        cin>>temperture[i];
    }
    for(int i=1; i<=clothes; i++){
        int from=0, to=0, att=0;
        cin>>from>>to>>att;
        for(int j=1; j<=days; j++){
            if (from <= temperture[j] && to >= temperture[j]){
                dp[j][i] = 0;
            }
        }
    }

    for(int y=2; y<=days; y++){
        for(int x=1; x<=clothes; x++){
            if (dp[y][x] == -1) continue;
            
        }
    }

}