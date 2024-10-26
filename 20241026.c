#include <stdio.h>
#include <string.h> 
void* Swap(int* p11, int* p22);

int main() {
    int i = 0;
    int a, b, c;
    void* p = &i;

    a = (int*)p + 1;
    printf("%d\n", a); 

    b = ((int*)p)++;
    printf("%d\n", b); 

    c = ((int*)p)[0];
    printf("%d\n", c); 
    int arr[4]; 
    memset(arr, -1, sizeof(arr)); 
    for (i = 0; i < 4; i++) {
        printf("%d ", arr[i]); 
    }

    int a1=1;
    int* p1 = &a1;
    printf("\n%d\n", ((* p1)+1));

    char* pC1 = NULL;
    int* pI1 = NULL;
    double* pD1 = NULL;

    printf("%p\r\n", pC1 + 1);
    printf("%p\r\n", pI1 + 1);
    printf("%p\r\n", pD1 + 1);
    
    int tmpnum1 = 1;
    int* p11 = &tmpnum1;
    int tmpnum2 = 2;
    int* p22 = &tmpnum2;
    Swap(p11, p22); 
    return 0;
}

void* Swap(int* p11, int* p22) {
    printf("이전 배열: %d %d\n", *p11, *p22);
    int temp1=*p11;
    *p11 = *p22;
    *p22 = temp1;
    printf("이후 배열: %d %d\n", *p11, *p22);
}
int* *MaxAddress(int* p111, int* p222) {
    return (p111 > p222) ? p111 : p222;
}
