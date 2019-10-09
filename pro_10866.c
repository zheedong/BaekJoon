#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning (disable:4996)

struct Node {
	int data;
	struct Node *nextPtr;
};

typedef struct Node DequeNode;

void push_front(DequeNode **topPPtr, DequeNode **tailPPtr, int X) { //정수 X를 덱의 앞에 넣는다.
	DequeNode *newPtr = NULL;
	newPtr = (int *)malloc(sizeof(DequeNode));

	if (newPtr != NULL) { //1-1) 메모리 할당 성공
		newPtr->data = X;

		if (*topPPtr == NULL) { //2-1) Deque이 비어있을 때
			newPtr->nextPtr = NULL;
			*topPPtr = newPtr;
			*tailPPtr = newPtr;
		}
		else { //2-2) Deque이 비어있지 않을 때
			newPtr->nextPtr = *topPPtr;
			*topPPtr = newPtr;
		}
	}
	else { //1-2) 메모리 할당 실패
		printf("ERROR. Memory allocation FAIL.\n");
		exit(1);
	}
}

void push_back(DequeNode **topPPtr, DequeNode **tailPPtr, int X) { //정수 X를 덱의 뒤에 넣는다.
	DequeNode *newPtr = NULL;
	newPtr = (int *)malloc(sizeof(DequeNode));

	if (newPtr != NULL) { //1-1) 메모리 할당 성공
		newPtr->data = X;

		if (*topPPtr == NULL) { //2-1) Deque이 비어있을 때
			newPtr->nextPtr = NULL;
			*topPPtr = newPtr;
			*tailPPtr = newPtr;
		}
		else { //2-2) Deque이 비어있지 않을 때
			newPtr->nextPtr = NULL;
			(*tailPPtr)->nextPtr = newPtr;
		}
	}
	else { //1-2) 메모리 할당 실패
		printf("ERROR. Memory allocation FAIL.\n");
		exit(1);
	}
}

int pop_front(DequeNode **topPPtr, DequeNode **tailPPtr) { //덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다.만약, 덱에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
	int pop_value = -1;
	DequeNode *tempPtr = NULL;

	if (empty(*topPPtr) == 0) { //1-1)Deque이 비어 있지 않을 때
		tempPtr = *topPPtr;
		pop_value = (*topPPtr)->data;
		*topPPtr = (*topPPtr)->nextPtr;
		free(tempPtr);

		if (*topPPtr == NULL) //2)Deque이 비어진 경우
			*tailPPtr = NULL;
	}

	return pop_value;
}

int pop_back(DequeNode **topPPtr, DequeNode **tailPPtr) { //덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다.만약, 덱에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
	int pop_value = -1;
	DequeNode *tempPtr = NULL;

	if (empty(*topPPtr) == 0){ //1)Deque가 비지 않았을 때
		pop_value = (*tailPPtr)->data;
		tempPtr = *tailPPtr;
		*tailPPtr = ;
	}

	return pop_value;
}

int size() { //덱에 들어있는 정수의 개수를 출력한다.
}

int empty(DequeNode *topPtr) { //덱이 비어있으면 1을, 아니면 0을 출력한다.
	if (topPtr == NULL) {
		return 1;
	}
	else {
		return 0;
	}
}

int front() { //덱의 가장 앞에 있는 정수를 출력한다.만약 덱에 들어있는 정수가 없는 경우에는 - 1을 출력한다.
}

int back() { //덱의 가장 뒤에 있는 정수를 출력한다.만약 덱에 들어있는 정수가 없는 경우에는 - 1을 출력한다.

}

int main(){
	DequeNode *topPtr = NULL;
	DequeNode *tailPtr = NULL;


}
