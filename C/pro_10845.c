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

int empty(QueueNode **headPPtr, QueueNode **tailPPtr) {
	if (*headPPtr == NULL) {
		return 1;
	}
	else {
		return 0;
	} //simple!
}

int front(QueueNode **headPPtr) {
	if (*headPPtr == NULL) {
		return -1;
	}
	else {
		return (*headPPtr)->data;
	}
}

int back(QueueNode **tailPPtr) {
	if (*tailPPtr == NULL) {
		return -1;
	}
	else {
		return (*tailPPtr)->data;
	}
}

int main() {
	QueueNode *topPtr = NULL;
	QueueNode *tailPtr = NULL;

	int how_many = 0;
	char buffer[15];
	char Push[5] = "push";
	char Pop[4] = "pop";
	char Size[5] = "size";
	char Empty[6] = "empty";
	char Front[6] = "front";
	char Back[5] = "back";

	scanf("%d", &how_many);
	getchar();
	for (int i = 0; i < how_many; i++) {
		gets(buffer);
		if (strcmp(buffer, Size) == 0) {
			printf("%d\n", size(topPtr, tailPtr));
		}
		else if (strcmp(buffer, Empty) == 0) {
			printf("%d\n", empty(&topPtr, &tailPtr));
		}
		else if (strcmp(buffer, Front) == 0) {
			printf("%d\n", front(&topPtr));
		}
		else if (strcmp(buffer, Back) == 0) {
			printf("%d\n", back(&tailPtr));
		}
		else if (strcmp(buffer, Pop) == 0) {
			printf("%d\n", dequeue(&topPtr, &tailPtr));
		}
		else {
			char *ptr = strtok(buffer, " ");
			ptr = strtok(NULL, " ");
			enqueue(&topPtr, &tailPtr, atoi(ptr));
		}
	}
	return 0;
}