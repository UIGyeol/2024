#include<stdio.h>

int main() {
	int N, M,i,j,k;
	
	//단어의 갯수를 입력받기
	printf("단어의 갯수를 입력");
	scanf("%d", &N);

	//단어 목록(단어를 저장할 배열) 선언
	char term[30][50];

	//단어 목록 입력
	printf("단어의 목록을 입력");
	for (i = 0; i < N; i++) {
		scanf("%s", term[i]);
	
	}
	
	printf("문서의 갯수를 입력");
	scanf("%d", &M);
	
	//단어 빈도에 대한 배열 선언 
	int freq[30][50];
	//TDM선언,N과 M의 최댓값으로 선언
	char TDM[30][50];
	printf("문서의 따른 각 단어의 빈도 수를 적으시오");
	for (j = 0; j < N; j++) {
		for (k = 0; k < M; k++) {
			scanf("%d", &freq[j][k]);
		}
		printf("\n");
	}
	//결과 TDM에 넣기
	int index = 0;
	for (j = 0; j < N; j++) {
		for (k = 0; k < M; k++) {
			if (freq[j][k] != 0) {
				sprintf(TDM[index], "%s 문서%d %d",term[j],k+1,freq[j][k]);
				//printf("%s 문서%d %d\n", term[j],k+1,freq[j][k]);
				index++;
			}
			
		}
		
	}
	//TDM출력
	for (i = 0; i < index; i++) {
		printf("%s\n", TDM[i]);
	}

	return 0;
}
