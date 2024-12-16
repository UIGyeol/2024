# include <stdio.h>

typedef struct NameTag {
	char* m;
}NameType;

int main() {
	struct NameTag s1;
	s1.m = "Mandu Park";
	NameType s2;
	s2.m = "Mandu JJin";
	printf("Hello. My name is %s.\n", s1.m);
	printf("Hello, there. I am %s.\n", s2.m);

	return 0;
}
