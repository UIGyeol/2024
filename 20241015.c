#include<stdio.h>

void hanoi(int n, char start, char mid, char to); 

int main() {
    hanoi(3, 'A', 'B', 'C'); 
    getchar();
    return 0;
}

void hanoi(int n, char start, char mid, char to) {
    if (n == 1) {
        printf("%c에서 원반 %d를 %c로 옮김\n", start, n, to);
    }
    else {
        hanoi(n - 1, start, to, mid);
        printf("%c에서 원반 %d를 %c로 옮김\n", start, n, to);
        hanoi(n - 1, mid, start, to);
    }
}
