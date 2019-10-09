#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning(disable:4996)

//Queue Basic

struct node {
	int data;
	struct node *nextPtr;
};

typedef struct node QueueNode;

void enqueue(QueueNode **headPPtr, QueueNode **tailPPtr, int value) {
	QueueNode *newPtr;
	newPtr = malloc(sizeof(QueueNode));

	if (newPtr != NULL) { //memory allocation success
		newPtr->data = value;
		newPtr->nextPtr = NULL; //newPtr will be the NEW tail of queue node. And the last of Queue node should indicate NULL.

		if (*headPPtr == NULL) { //If Queue Node is empty.
			*headPPtr = newPtr; //newPtr should be headPtr.
		}
		else {
			(*tailPPtr)->nextPtr = newPtr; //If Queue Node is NOT empty, previous tail should indicate newPtr. 
		}

		*tailPPtr = newPtr; //newPtr should be new tailPtr.
	}
	else { //memory allocation fail
		printf("ERROR\n");
		exit(1);
	}
}

int dequeue(QueueNode **headPPtr, QueueNode **tailPPtr) {
	if (*headPPtr == NULL) //If Queue Node is empty.
		return -1;

	QueueNode *tempPtr; //copy for *headPPtr in order to free()
	int value; //for return

	value = (*headPPtr)->data; //dequeue data from head node.
	tempPtr = *headPPtr; //copy *headPPtr.
	*headPPtr = (*headPPtr)->nextPtr; //headPtr changed.

	if (*headPPtr == NULL) //If Queue Node is empty.
		*tailPPtr = NULL; //TailPtr also should be NULL.

	free(tempPtr); //free memory space.

	return value;
}

int size(QueueNode *headPtr, QueueNode *tailPtr) { //Call by value.
	if (headPtr == NULL) {
		return 0;
	}
	else {
		int count = 1;
		QueueNode *tempPtr = headPtr;
		while (tempPtr != tailPtr) { //I think... It would be better if I used do...while.
			tempPtr = tempPtr->nextPtr; //count until end.
			count++;
		}
		return count;
	}
}

int main() {
	QueueNode *headPtr = NULL;
	QueueNode *tailPtr = NULL;
	int k = 0;
	int i = 0;

	scanf("%d", &i);

	for (int j = 1; j <= i; j++) {
		enqueue(&headPtr, &tailPtr, j);
	}
	
	while (size(headPtr, tailPtr) != 1) {
		if (k == 0) {
			dequeue(&headPtr, &tailPtr);
			k = 1;
		}
		else if (k == 1) {
			enqueue(&(headPtr->nextPtr), &tailPtr, dequeue(&headPtr, &tailPtr));
			k = 0;
		}
	}

	printf("%d\n", headPtr->data);
	return 0;
}