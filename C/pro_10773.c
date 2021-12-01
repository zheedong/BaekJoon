#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

struct node {
	int data;
	struct node *nextPtr;
};

typedef struct node StackNode;

void push(StackNode **topPtr, int value) {
	StackNode *newPtr;
	newPtr = malloc(sizeof(StackNode));

	if (newPtr != NULL) {
		newPtr->data = value;
		newPtr->nextPtr = *topPtr;
		*topPtr = newPtr;
	}
	else {
		printf("ERROR\n");
		exit(1);
	}
}

int pop(StackNode **topPtr) {
	StackNode *tempPtr;
	int popValue;

	if (*topPtr == NULL) {
		return -1;
	}

	tempPtr = *topPtr;
	popValue = (*topPtr)->data;
	*topPtr = (*topPtr)->nextPtr;
	free(tempPtr);

	return popValue;
}

int StackSum(StackNode **topPtr) {
	int sum = 0;
	StackNode *temp;
	temp = *topPtr;

	while (temp != NULL) {
		sum += temp->data;
		temp = temp->nextPtr;
	}

	return sum;
}

int main() {
	unsigned int how_many = 0;
	StackNode *StackPtr = NULL;

	scanf("%d", &how_many);

	while (how_many > 0) {
		unsigned int n = 0;
		scanf("%d", &n);

		if (n != 0) {
			push(&StackPtr, n);
		}
		else {
			pop(&StackPtr);
		}
		how_many--;
	}

	printf("%d\n", StackSum(&StackPtr));
	
	return 0;
}