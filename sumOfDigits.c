#include <stdio.h>

int sumOfDigits(int number) {
    int sum = 0;
    while(number != 0) {
        sum += number % 10;
        number /= 10;
    }
    return sum;
}

int readInt(char* text) {
    int value;
    do {
        printf(text);
        fflush(stdin);
    } while(scanf("%d", &value) == 0);
    return value;
}

int main() {
    int number = readInt("write number: ");
    printf("%d", sumOfDigits(number));
    return 0;
}
