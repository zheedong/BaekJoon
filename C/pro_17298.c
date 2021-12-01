#include "Stack_General_LinkedList.h"
#include <stdio.h>
#include <stdlib.h>
#pragma warning (disable:4996)

int main() {
	int iSizeN;
	int iArr_Input[1000000] = { '\0', };
	int iArr_NGE[1000000] = { '\0', };

	scanf("%d", &iSizeN);

	for (int i = 0; i < iSizeN; i++) {
		scanf("%d", &iArr_Input[i]);
	}

	StackData* pStackData = NULL;
	Stack_Create(&pStackData);
	int iBottom = -1;
	Stack_Push(pStackData, &iBottom);

	for (int j = iSizeN - 1; j >= 0; j--) {
		if (*(int*)Stack_Top(pStackData) != -1) { //Not empty
			while (*(int*)Stack_Top(pStackData) != -1 && iArr_Input[j] >= *(int*)Stack_Top(pStackData))
				Stack_Pop(pStackData);

			iArr_NGE[j] = *(int*)Stack_Top(pStackData);
			Stack_Push(pStackData, &iArr_Input[j]);
		}
		else { //Empty
			iArr_NGE[j] = *(int*)Stack_Top(pStackData);
			Stack_Push(pStackData, &iArr_Input[j]);
		}
	}

	for (int i = 0; i <= iSizeN - 1; i++)
		printf("%d ", iArr_NGE[i]);

	return 0;
}