#include <stdio.h>

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

	tempPtr = *topPtr;
	popValue = (*topPtr)->data;
	*topPtr = (*topPtr)->nextPtr;
	free(tempPtr);
	
	return popValue;
}

int size(StackNode **topPtr) {
	int count = 0;
	StackNode *tempPtr = *topPtr;
	while (tempPtr != NULL) {
		count++;
		tempPtr = tempPtr->nextPtr;
	}

	return count;
}

int empty(StackNode **topPtr) {
	if ((*topPtr)->data == NULL) {
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
	int 
}