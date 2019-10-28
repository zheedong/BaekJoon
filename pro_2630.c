#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning (disable:4996)
#define WHITE 0
#define BLUE 1

typedef int COLOR;
int WHITE_COUNTER = 0;
int BLUE_COUNTER = 0;

int** Make_Matrix(int size) {
	int** new_Matrix;
	new_Matrix = (int**)malloc(sizeof(int*) * size);
	for (int Col = 0; Col < size; Col++) {
		new_Matrix[Col] = (int*)malloc(sizeof(int) * size);
	}
	return new_Matrix;
}

void free_matrix(int** ppArr, int size) {
	for (int i = 0; i < size; i++) {
		free(ppArr[i]);
	}
	free(ppArr);
}

void checker(int N_N, int** ppArr) {
	COLOR initial = ppArr[0][0];
	for (int Row = 0; Row < N_N; Row++) {
		for (int Col = 0; Col < N_N; Col++) {
			if (ppArr[Row][Col] != initial) {
				int** ppMatrix1 = Make_Matrix(N_N / 2);
				for (int i = 0; i < N_N / 2; i++) {
					for (int j = 0; j < N_N / 2; j++) {
						ppMatrix1[i][j] = ppArr[i][j];
					}
				}
				int** ppMatrix2 = Make_Matrix(N_N / 2);
				for (int i = 0; i < N_N / 2; i++) {
					for (int j = N_N / 2; j < N_N; j++) {
						ppMatrix2[i][j - N_N / 2] = ppArr[i][j];
					}
				}
				int** ppMatrix3 = Make_Matrix(N_N / 2);
				for (int i = N_N / 2; i < N_N; i++) {
					for (int j = 0; j < N_N / 2; j++) {
						ppMatrix3[i - N_N / 2][j] = ppArr[i][j];
					}
				}
				int** ppMatrix4 = Make_Matrix(N_N / 2);
				for (int i = N_N / 2; i < N_N; i++) {
					for (int j = N_N / 2; j < N_N; j++) {
						ppMatrix4[i - N_N / 2][j - N_N / 2] = ppArr[i][j];
					}
				}

				checker(N_N / 2, ppMatrix1);
				checker(N_N / 2, ppMatrix2);
				checker(N_N / 2, ppMatrix3);
				checker(N_N / 2, ppMatrix4);
				return;
			}
		}
	}

	free_matrix(ppArr, N_N);
	if (initial == WHITE)
		WHITE_COUNTER++;
	else
		BLUE_COUNTER++;
}

int main() {
	int size = 0;
	scanf("%d", &size);
	int** ppArr = Make_Matrix(size);

	for (int Row = 0; Row < size; Row++) {
		for (int Col = 0; Col < size; Col++) {
			int buffer = 0;
			scanf("%d", &buffer);
			ppArr[Row][Col] = buffer;
		}
	}

	checker(size, ppArr);
	printf("%d\n%d", WHITE_COUNTER, BLUE_COUNTER);
	free_matrix(ppArr, size);
	return 0;
}
