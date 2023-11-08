#include <iostream>
using namespace std;

int arr1[31] = {0, 1, 0}, arr2[31] = {0, 0, 1}, day = 0, snack = 0, first = 0, second = 0, finish = 0;

int main() {
    cin >> day >> snack;
    for (int i = 3; i <= 30; i++) {
        arr1[i] = arr1[i - 1] + arr1[i - 2];
        arr2[i] = arr2[i - 1] + arr2[i - 2];
    }
    first = arr1[day];
    second = arr2[day];
    for (int a = 1; a <= snack; a++) {
        if (finish > 0)
            break;
        for (int b = a; b <= snack; b++) {
            if (first * a + second * b == snack) {
                cout << a << endl << b;
                finish++;
                break;
            } else if (first * a + second * b > snack)
                break;
        }
    }
    return 0;
}
