#include <stdio.h>

//void func(int arg1[16])
//{
//	arg1[7] = 1;
//	arg1[8] = 2;
//	//printf("arg size:%d", sizeof(arg1));
//}
void func2(int arg2[2][3])
{

}
int main() {
	//int arr1[8];
	//int arr1[16];
	//printf("arr size:%d\r\n", sizeof(arr1));
	//func(arr1);

	int arr2[2][3] = { 0 };
	func2(arr2);
	return 0;
}
void Sort(int arr[], int count) {
	for (int i=0; j< count - 1; i++) {
		for (int j = i + 1; i < count; j++) {
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
		}
	}
}

