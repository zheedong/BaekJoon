#include <stdio.h>
#include <stdlib.h>
#pragma warning (disable:4996)

struct node {
	int priority;
	int index;
	int marking;
	struct node *nextPtr;
};

typedef struct node QueueNode;

void enqueue(QueueNode **headPPtr, QueueNode **tailPPtr, int priority, int index) {
	QueueNode *newPtr;
	newPtr = (QueueNode *)malloc(sizeof(QueueNode));

	if (newPtr != NULL) { //memory allocation success
		newPtr->priority = priority; //value is priority.
		newPtr->index = index; //give the index from global variation
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

int dequeue(QueueNode **headPPtr, QueueNode **tailPPtr) { //return index. 
	if (*headPPtr == NULL) //If Queue Node is empty.
		return -1;

	QueueNode *tempPtr; //copy for *headPPtr in order to free()
	int value; //for return

	value = (*headPPtr)->index; //dequeue data from head node.
	tempPtr = *headPPtr; //copy *headPPtr.
	*headPPtr = (*headPPtr)->nextPtr; //headPtr changed.

	if (*headPPtr == NULL) //If Queue Node is empty.
		*tailPPtr = NULL; //TailPtr also should be NULL.

	free(tempPtr); //free memory space.

	return value;
}

int main() {
	int how_many = 0;
	scanf("%d", &how_many);
	while (how_many > 0) {
		QueueNode *headPtr = NULL;
		QueueNode *tailPtr = NULL;

		int N_papers = 0;
		int M_curious = 0;
		int priority_buffer = 0;
		
		scanf("%d %d", &N_papers, &M_curious);
		for (int i = 0; i < N_papers; i++) {
			scanf("%d", &priority_buffer);
			enqueue(&headPtr, &tailPtr, priority_buffer, i);
			if (i == M_curious) {
				tailPtr->marking = 1; //check M'st QueueNode
			}
			else {
				tailPtr->marking = 0;
			}
		}

		int real_count = 0;
		QueueNode *tempPtr = NULL;

		while (headPtr != NULL) {
			tempPtr = headPtr->nextPtr;

			while (tempPtr != NULL) {

				if (tempPtr->priority <= headPtr->priority) {
					tempPtr = tempPtr->nextPtr;
				}
				else {
					QueueNode *copyPtr = headPtr->nextPtr;
					tailPtr->nextPtr = headPtr;
					tailPtr = tailPtr->nextPtr;
					tailPtr->nextPtr = NULL;
					headPtr = copyPtr;

					tempPtr = headPtr->nextPtr;
				}
			}
		
			real_count++;

			if (headPtr->marking == 1) {
				printf("%d\n", real_count);
				break;
			}

			dequeue(&headPtr, &tailPtr);
		}

		how_many--;
	}
	return 0;
}