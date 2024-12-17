# include <stdio.h>


int main() {
	char ch;
	unsigned char j; 
	char k;

	ch = 200;
	j = 200;
	k = 'a';
	printf("문자열 변수 ch의 값은 %d\n", ch);
	printf("문자열 변수 j의 값은 %d\n", j);
	printf("문자열 변수 k의 값은 %d\n", k);

	int i;
	unsigned int j;
	int k;
	i = 2000000000;
	j = 4000000000;
	k = 'b';
	printf("정수형 변수 i의 값은 %d\n", i);
	printf("정수형 변수 j의 값은 %u\n", j);
	printf("정수형 변수 k의 값은 %d\n", k);

  float d;
	double dl;
	double d2;
	d = 3.141592;
	dl = 1234567890;
	d2 = 'c';
	printf("실수형 변수 d의 값은 %E\n", d);
	printf("실수형 변수 dl의 값은 %E\n", dl);
	printf("실수형 변수 d2의 값은 %E\n", d2);

	char str[]="대한민국";
	char* j = "I love Korea";
	printf("문자열형 변수 str의 값은 %s\n", str);
	printf("문자열형 변수 j의 값은 %s\n", j);

	return 0;
}
