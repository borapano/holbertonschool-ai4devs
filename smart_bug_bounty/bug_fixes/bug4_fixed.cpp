#include <iostream>
using namespace std;

int main() {
    int numbers[6] = {5, 10, 15, 20, 25, 30};
    int max = numbers[0];

    for (int i = 1; i < 6; i++) {   // <-- FIXED
        if (numbers[i] > max) {
            max = numbers[i];
        }
    }

    cout << "Maximum value: " << max << endl;

    cout << "All numbers:" << endl;
    for (int i = 0; i < 6; i++) {
        cout << numbers[i] << " ";
    }

    return 0;
}