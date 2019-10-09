#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning (disable:4996)

struct node {
	int* matrixPtr;
	struct node *Ptr1;
	struct node *Ptr2;
	struct node *Ptr3;
	struct node *Ptr4;
};

void mk_matrix(int sizeN, int **arr) {
	arr = (int**)malloc(sizeof(int*) * sizeN);
	for (int i = 0; i < sizeN; i++) {
		*(arr + sizeof(int) * i) = (int*)malloc(sizeof(int) * sizeN);
	}
}

void rm_matrix(int sizeN, int** arr) {
	for (int i = 0; i < sizeN; i++) {
		free(arr[i]);
	}
	free(arr);
}

int main() {
	int sizeN;
	scanf("%d", &sizeN);

	int** matrix1; //2���� �迭�� ���� �Ҵ�
	mk_matrix(sizeN, matrix1);

	for (int row = 0; row < sizeN; row++) {
		for (int col = 0; col < sizeN; col++) {
			int w;
			scanf("%d", &w);
			matrix1[row][col] = w;
		}
	}
//�ؿ��� Test
	for (int row = 0; row < sizeN; row++) {
		for (int col = 0; col < sizeN; col++) {
			printf("%d ", matrix1[row][col]);
		}
		printf("\n");
	}
//Test ��

	rm_matrix(sizeN, matrix1);
	return 0;
}
