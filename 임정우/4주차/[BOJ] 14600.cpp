#include <iostream>
#include <algorithm>
using namespace std;

int sLen=0, hx=0, hy=0;
int map[4][4], vx[4]={0,3,3,0}, vy[4]={0,0,3,3}, moveY[4]={0,1,0,-1}, moveX[4]={1,0,-1,0};
void printMap(int sLen){
    if (sLen==2){
        for(int i=3; i>=0; i--){
            for(int j=0; j<4; j++){
                cout<<map[i][j]<<" ";
            }
            cout<<"\n";
        }
    }else{
        for(int i=1; i>=0; i--){
            for(int j=0; j<2; j++){
                cout<<map[i][j]<<" ";
            }
            cout<<"\n";
        }
    }
}
bool checkBound(int y, int x){
    return (y>=0 && y<4 && x>=0 && x<4);
}
int checkSite(int hy, int hx){
    if (hy > 2){
        if (hx > 2){
            return 4;
        } else return 3;
    } else {
        if (hx > 2){
            return 1;
        } else return 2;
    }
}
void fillAroundHoll(int hy, int hx, int site){
    if (site == 1){
        for(int i=0; i<2; i++){
            for(int j=2; j<4; j++){
                if (i == hy && j== hx) continue;
                else map[i][j] = 1;
            }
        }
    } else if (site == 2){
        for(int i=0; i<2; i++){
            for(int j=0; j<2; j++){
                if (i == hy && j== hx) continue;
                else map[i][j] = 1;
            }
        }
    } else if (site == 3){
        for(int i=2; i<4; i++){
            for(int j=0; j<2; j++){
                if (i == hy && j== hx) continue;
                else map[i][j] = 1;
            }
        }
    } else{
        for(int i=2; i<4; i++){
            for(int j=2; j<4; j++){
                if (i == hy && j== hx) continue;
                else map[i][j] = 1;
            }
        }
    }
    map[hy][hx] = -1;
}
void fillOutside(){
    int cnt = 1;
    for(int a=0; a<4; a++){
        int y = vy[a];
        int x = vx[a];
        if (map[y][x] == 0){
            map[y][x] = ++cnt;
            for(int d=0; d<4; d++){
                int ny = y+moveY[d];
                int nx = x+moveX[d];
                if (checkBound(ny, nx) && map[ny][nx] == 0){
                    map[ny][nx] = cnt;
                }
            }
        }
        
    }
}
void fillCenter(){
    for(int i=1; i<3; i++){
        for(int j=1; j<3; j++){
            if (map[i][j] == 0) map[i][j] = 5;
        }
    }
}
int main(){
    cin>>sLen>>hx>>hy;
    if (sLen == 1){
        fill(&map[0][0], &map[0][0]+sizeof(map)-4, 1);
        map[hy-1][hx-1] = -1;
    }else{
        fillAroundHoll(hy-1, hx-1, checkSite(hy, hx));
        fillOutside();
        fillCenter();
    }
    printMap(sLen);
}