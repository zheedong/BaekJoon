#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

struct Node {
	char data;
	struct Node *nextPtr;
};

typedef struct Node StackNode;

void push(StackNode **topPtr, char value) {
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

char pop(StackNode **topPtr) {
	StackNode *tempPtr;
	char popValue;

	if (*topPtr == NULL) {
		printf("ERROR\n");
		exit(1);
	}

	tempPtr = *topPtr;
	popValue = (*topPtr)->data;
	*topPtr = (*topPtr)->nextPtr;
	free(tempPtr);

	return popValue;
}

int checker(StackNode *topPtr) {

	int count = 0;

	while (topPtr != NULL) {
		char popV;
		popV = pop(&topPtr);

		if (popV == ')') {
			count++;
		}
		else {
			count--;
			if (count < 0) {
				return 0;
			}
		}
	}

	if (count == 0) {
		return 1;
	}
	else {
		return 0;
	}
}

int main() {
	unsigned int how_many = 0;
	scanf("%d", &how_many);

	while (how_many > 0) {
		char buffer[51] = { '\0', };
		scanf("%s", buffer);

		StackNode *StackPtr = NULL;
		for (int i = 0; buffer[i] != '\0'; i++) {
			push(&StackPtr, buffer[i]);
		}
		
		if (checker(StackPtr)) {
			printf("YES\n");
		}
		else {
			printf("NO\n");
		}

		how_many--;
	}

	return 0;
}