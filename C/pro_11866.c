#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)

//n,k - Josephus permutation

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

int empty(QueueNode **headPPtr, QueueNode **tailPPtr) {
	if (*headPPtr == NULL) {
		return 1;
	}
	else {
		return 0;
	} //simple!
}

int main() {
	QueueNode *headPtr = NULL;
	QueueNode *tailPtr = NULL;
	int N, K, count = 0;
	scanf("%d %d", &N, &K);

	int *arr = (int *)malloc(sizeof(int)*N); //Make an array space

	for (int i = 1; i <= N; i++) {
		enqueue(&headPtr, &tailPtr, i); //enqueue N numbers
	}

	while (empty(&headPtr, &tailPtr) == 0) {
		for (int l = 0; l < K - 1; l++)
			enqueue(&headPtr, &tailPtr, dequeue(&headPtr, &tailPtr)); //Pop from head, Push to tail
		*(arr + count) = dequeue(&headPtr, &tailPtr); //Pop from head, and save it in array
		count++;
	}

	printf("<");
	for (int j = 0; j < count - 1; j++) {
		printf("%d, ", *(arr + j)); //print N - 1 numbers
	}
	printf("%d>\n", *(arr + count - 1)); //print LAST number

	free(arr); //free malloc
	return 0;
}