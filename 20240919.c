#include <stdio.h>
#include <string.h>
//reviewing def
//int Sum(int from, int to)
//{
//	int sum = 0;
//	int i;
//	for ( i = from; i <= to; i++)
//		sum += i;
//		if (i == to) printf("complete!");
//		
//
//	return sum;
//	
//}
//
//int main()
//{
//	int result = Sum(1, 100);
//	printf("Sum: %d", result);
//}

//making my own def
char* Callfriend(int num);

char *Callfriend(int num)
{
	char* friendlist[] = { "Amy", "Max", "Janny", "Linda", "Chris", "Jun" };
	num -= 1;
	if (num >= 0 && num <= 6)
		return friendlist[num];
	else
		return "error";

}


int main() {
	printf("%s", Callfriend(3));
	return 0;
}
