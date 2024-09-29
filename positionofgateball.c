#include<stdio.h>
#include< string.h >
void movingpoint(char orderingp[], int* n, int* m, int field[4][4]);
void printPosition(int n, int m);

int main() {
	//게이트볼 훈련장 배열 생성
	int field [4] [4] = { {1,2,3,4} ,{5,6,7,8},
		{9,10,11,12}, {13,14,15,16} };
	//초기 위치선정
	int n = 1, m = 1;
	//이동할 명령어 입력 받기
	char orderingp[100];
	printf("이동할 방향을 입력하시오");
	scanf("%s", orderingp);
	//명령어 출력
	printf("입력한 명령어: %s\n", orderingp);

	//실제로 이동하기
	movingpoint(orderingp, &n, &m, field);
	
	return 0;

}

void printPosition(int n, int m) {
	printf("현재 위치: (%d,%d)", n, m);

}

void movingpoint(char orderingp[], int* n, int* m, int field[4][4]) {//이동하는 함수 만들기
	int i; int len = strlen(orderingp);
	int hittingwall = 0;
	for (i = 0; i < len; i++) {
		if (orderingp[i] == 'L'&& * m > 1) { (*m)--; }
		if (orderingp[i] == 'R' && * m < 4) { (*m)++; }
		if (orderingp[i] == 'U' && * n > 1) { (*n)--; }
		if (orderingp[i] == 'D' && * n < 4) { (*n)++; }
		//벽에 부딪힌 횟수
		if (orderingp[i] == 'L' && * m < 1) { hittingwall++; }
		if (orderingp[i] == 'R' && * m > 4) { hittingwall++; }
		if (orderingp[i] == 'U' && * n < 1) { hittingwall++; }
		if (orderingp[i] == 'D' && * n > 4) { hittingwall++; }
		
		
		
	
	}
	printPosition(*n, *m);
	printf("스위한 횟수: %d", len - hittingwall);
}
