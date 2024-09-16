#include<stdio.h>
int main() 
{
    char username1[50];
    char* pC = username1;

    printf("someone: open your eyes.\n");
    getchar();

    printf("you: wait... what?\n");
    getchar();

    printf("someone: who are you? why are you sleeping in the street?\n");

    printf(">> please write your name. <<\n");

    scanf_s("%s", pC, sizeof(username1));
    printf("someone: %s? I've never heard of that name in this town....\n", pC);




    return 0;
}
