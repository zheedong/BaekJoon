#include "Stack_General_LinkedList.h"
#include <stdio.h>
#include <stdlib.h>
#pragma warning (disable : 4996)

void Print_Recursion(int size, StackData* pStackData) {
	if (size == 0) {
		return;
	}
	else {
		char temp = *(char*)Stack_Pop(pStackData);
		Print_Recursion(--size, pStackData);
		printf("%c\n", temp);
	}
}

int main() {
	StackData* pStackData = NULL;
	StackData* pOpera_Stack = NULL;
	int size;
	int* pArr_GOAL;
	int buffer = 0;

	scanf("%d", &size);
	pArr_GOAL = (int*)malloc(sizeof(int) * size);

	for (int i = 0; i < size; i++) {
		scanf("%d", &buffer);
		pArr_GOAL[i] = buffer;
	}

	Stack_Create(&pStackData);
	Stack_Create(&pOpera_Stack);
	char pOperation[2] = { '+', '-' };
	int Sequence_Index = 0;
	int* pIndex_Arr = (int*)malloc(sizeof(int) * size);

	for (int i = 1; i <= size; i++) {
		pIndex_Arr[i - 1] = i;
		if (i <= pArr_GOAL[Sequence_Index]) {
			Stack_Push(pStackData, &pIndex_Arr[i - 1]);
			Stack_Push(pOpera_Stack, &pOperation[0]);
		}
		else {
			do {
				Stack_Pop(pStackData);
				Stack_Push(pOpera_Stack, &pOperation[1]);
				++Sequence_Index;
				if (Stack_Empty(pStackData))
					break;
			} while (*(int*)Stack_Top(pStackData) == pArr_GOAL[Sequence_Index]);
			Stack_Push(pStackData, &pIndex_Arr[i - 1]);
			Stack_Push(pOpera_Stack, &pOperation[0]);
		}
	}
	while (Stack_Empty(pStackData) != 1) {
		if (*(int*)Stack_Top(pStackData) != pArr_GOAL[Sequence_Index]) {
			Stack_Destroy(pStackData);
			printf("NO\n");
			return 0;
		}
		else {
			Stack_Pop(pStackData);
			Stack_Push(pOpera_Stack, &pOperation[1]);
			++Sequence_Index;
		}
	}
	Print_Recursion(pOpera_Stack->size, pOpera_Stack);
	return 0;
}