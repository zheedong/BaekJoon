#include<stdio.h>
#define SIZE 10000
#pragma warning(disable : 4996)

int main() {
	char buffer[SIZE];

	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fgets(buffer, SIZE, stdin);
	fputs(buffer, stdout);

	return 0;
}