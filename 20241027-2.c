#include <stdio.h>

void func(int* p1) {
	*p1 = 1;
}

void round(int* p2)
{
	*p2 = (*p2 + 5) / 10 * 10;
}

int main() {
	char name[16]="Kim Man Du\n";
	printf("%s\r\n", name);

	char* pName = "Jin Man Du\n";
	printf("%s", pName);

	int arr[2] = { 1,2 };

	int* p = &arr;
	printf("%d,%d\r\n", p[0], p[1]);

	int(*parr)[2] = arr;
	printf("%d,%d\r\n", (*parr)[0], (*parr)[1]);
	int a = 0;
	func(&a);
	printf("a: %d", a);

	int a2 = 7;
	printf("\n%d 반올림", a2);
	round(&a);
	printf("\n반올림된 값: %d\n", a2);


	return 0;
}

int mystrlen(const char* str) {
	for (int i = 0; ; i++) {
		if(str[i] == '\0')
			return i;
	}
}

