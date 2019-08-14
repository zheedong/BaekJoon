#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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

int size(StackNode **topPtr) {
	int count = 0;
	if (topPtr == NULL) {
		printf("ERROR\n");
		exit(1);
	}
	StackNode *tempPtr = *topPtr;
	while (tempPtr != NULL) {
		count++;
		tempPtr = tempPtr->nextPtr;
	}

	return count;
}

int empty(StackNode **topPtr) {
	if (*topPtr == NULL) {
		return 1;
	}
	else {
		return 0;
	}
}

int top(StackNode **topPtr) {
	int popValue = -1;
	if (*topPtr == NULL) {
		return popValue;
	}
	popValue = (*topPtr)->data;
	
	return popValue;
}

int main() {
	int how_many = 0;
	char buffer[15];
	char Push[5] = "push";
	char Pop[4] = "pop";
	char Size[5] = "size";
	char Empty[6] = "empty";
	char Top[4] = "top";

	StackNode *StackPtr = NULL;
	
	scanf("%d", &how_many);
	getchar();
	for (int i = 0; i < how_many; i++) {
		gets(buffer);
		if (strcmp(buffer, Size) == 0) {
			printf("%d\n", size(&StackPtr));
		}
		else if (strcmp(buffer, Empty) == 0) {
			printf("%d\n", empty(&StackPtr));
		}
		else if (strcmp(buffer, Top) == 0) {
			printf("%d\n", top(&StackPtr));
		}
		else if (strcmp(buffer, Pop) == 0) {
			printf("%d\n", pop(&StackPtr));
		}
		else {
			char *ptr = strtok(buffer, " ");
			ptr = strtok(NULL, " ");
			push(&StackPtr, atoi(ptr));
		}
	}
	return 0;
}