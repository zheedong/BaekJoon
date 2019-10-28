#include <stdio.h>
#include <stdlib.h>
#pragma warning (disable : 4996)

int Reverse(char* pArr) {
	char temp = (pArr)[0];
	(pArr)[0] = (pArr)[2];
	(pArr)[2] = temp;
	return atoi(pArr);
}

int main() {
	int A = 0;
	int B = 0;
	char A_reverse[4];
	char B_reverse[4];

	scanf("%s %s", A_reverse, B_reverse);
	A = Reverse(A_reverse);
	B = Reverse(B_reverse);

	printf("%d\n", A > B ? A : B);
	return 0;
}
