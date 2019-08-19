#include <stdio.h>
#include <stdlib.h>

struct Node {
	int data;
	struct Node *nextPtr;
};

typedef struct Node QueueNode; 

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

int main() {
	int N, K;
	scanf("%d %d", &N, &K);

	printf("< ");
	
