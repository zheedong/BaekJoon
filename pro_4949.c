#include <stdio.h>
#include <stdlib.h>
#pragma warning (disable:4996)

struct node {
	char data;
	struct node* nextPtr;
};

typedef struct node StackNode;

void push(StackNode **ppStack, char data) {
	StackNode* newNodePtr = (StackNode*)malloc(sizeof(StackNode));
	if (newNodePtr == NULL)
		return;
	else {
		newNodePtr->data = data;
		if (*ppStack == NULL) { //empty stack
			newNodePtr->nextPtr = NULL;
		}
		else { //not empty stack
			newNodePtr->nextPtr = *ppStack;
		}
		*ppStack = newNodePtr;
	}
}

char pop(StackNode **ppStack) {
	char popValue;
	if (*ppStack == NULL)
		return;
	else {
		StackNode* temp = *ppStack;
		popValue = (*ppStack)->data;
		*ppStack = (*ppStack)->nextPtr;
		free(temp);
		return popValue;
	}
}

char top(StackNode** ppStack) {
	return (*ppStack)->data;
}

int isEmpty(StackNode** ppStack) { //return 0 isEmpty, return 1 is NOT empty
	if (*ppStack == NULL)
		return 0;
	else
		return 1;
}

void Destroy(StackNode* pStack) {
	while (isEmpty(&pStack) != 0) {
		pop(&pStack);
	}
	free(pStack);
}

int brace_checker(char *buffer) { //return 1 yes, return 0 no
	int i = 0;
	int ret = 1;
	StackNode* pBrace = NULL;

	while (buffer[i] != '\0') {
		if (buffer[i] == '(')
			push(&pBrace, '(');
		else if (buffer[i] == ')') {
			if (isEmpty(&pBrace) == 0) {
				ret = 0;
				break;
			}
			else if (top(&pBrace) == '[') {
				ret = 0;
				break;
			}
			else {
				pop(&pBrace);
			}
		}
		else if (buffer[i] == '[')
			push(&pBrace, '[');
		else if (buffer[i] == ']') {
			if (isEmpty(&pBrace) == 0) {
				ret = 0;
				break;
			}
			else if (top(&pBrace) == '(') {
				ret = 0;
				break;
			}
			else
				pop(&pBrace);
		}
		i++;
	}
	if (isEmpty(&pBrace) == 1)
		ret = 0;
	if (isEmpty(&pBrace) == 1)
		Destroy(pBrace);
	return ret;
}

int main() {
	char buffer[105] = { '\0', };
	do {
		gets(buffer);
		if (buffer[0] == '.')
			break;

		if (brace_checker(buffer) == 1)
			printf("yes\n");
		else if (brace_checker(buffer) == 0)
			printf("no\n");
	} while (1);
	return 0;
}