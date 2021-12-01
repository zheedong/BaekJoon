#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning (disable:4996)

struct Node {
	int data;
	struct Node *nextPtr;
};

typedef struct Node DequeNode;

void push_front(DequeNode **topPPtr, DequeNode **tailPPtr, int X) { //���� X�� ���� �տ� �ִ´�.
	DequeNode *newPtr = NULL;
	newPtr = (int *)malloc(sizeof(DequeNode));

	if (newPtr != NULL) { //1-1) �޸� �Ҵ� ����
		newPtr->data = X;

		if (*topPPtr == NULL) { //2-1) Deque�� ������� ��
			newPtr->nextPtr = NULL;
			*topPPtr = newPtr;
			*tailPPtr = newPtr;
		}
		else { //2-2) Deque�� ������� ���� ��
			newPtr->nextPtr = *topPPtr;
			*topPPtr = newPtr;
		}
	}
	else { //1-2) �޸� �Ҵ� ����
		printf("ERROR. Memory allocation FAIL.\n");
		exit(1);
	}
}

void push_back(DequeNode **topPPtr, DequeNode **tailPPtr, int X) { //���� X�� ���� �ڿ� �ִ´�.
	DequeNode *newPtr = NULL;
	newPtr = (int *)malloc(sizeof(DequeNode));

	if (newPtr != NULL) { //1-1) �޸� �Ҵ� ����
		newPtr->data = X;

		if (*topPPtr == NULL) { //2-1) Deque�� ������� ��
			newPtr->nextPtr = NULL;
			*topPPtr = newPtr;
			*tailPPtr = newPtr;
		}
		else { //2-2) Deque�� ������� ���� ��
			newPtr->nextPtr = NULL;
			(*tailPPtr)->nextPtr = newPtr;
		}
	}
	else { //1-2) �޸� �Ҵ� ����
		printf("ERROR. Memory allocation FAIL.\n");
		exit(1);
	}
}

int pop_front(DequeNode **topPPtr, DequeNode **tailPPtr) { //���� ���� �տ� �ִ� ���� ����, �� ���� ����Ѵ�.����, ���� ����ִ� ������ ���� ��쿡�� - 1�� ����Ѵ�.
	int pop_value = -1;
	DequeNode *tempPtr = NULL;

	if (empty(*topPPtr) == 0) { //1-1)Deque�� ��� ���� ���� ��
		tempPtr = *topPPtr;
		pop_value = (*topPPtr)->data;
		*topPPtr = (*topPPtr)->nextPtr;
		free(tempPtr);

		if (*topPPtr == NULL) //2)Deque�� ����� ���
			*tailPPtr = NULL;
	}

	return pop_value;
}

int pop_back(DequeNode **topPPtr, DequeNode **tailPPtr) { //���� ���� �ڿ� �ִ� ���� ����, �� ���� ����Ѵ�.����, ���� ����ִ� ������ ���� ��쿡�� - 1�� ����Ѵ�.
	int pop_value = -1;
	DequeNode *tempPtr = NULL;

	if (empty(*topPPtr) == 0){ //1)Deque�� ���� �ʾ��� ��
		pop_value = (*tailPPtr)->data;
		tempPtr = *tailPPtr;
		*tailPPtr = ;
	}

	return pop_value;
}

int size() { //���� ����ִ� ������ ������ ����Ѵ�.
}

int empty(DequeNode *topPtr) { //���� ��������� 1��, �ƴϸ� 0�� ����Ѵ�.
	if (topPtr == NULL) {
		return 1;
	}
	else {
		return 0;
	}
}

int front() { //���� ���� �տ� �ִ� ������ ����Ѵ�.���� ���� ����ִ� ������ ���� ��쿡�� - 1�� ����Ѵ�.
}

int back() { //���� ���� �ڿ� �ִ� ������ ����Ѵ�.���� ���� ����ִ� ������ ���� ��쿡�� - 1�� ����Ѵ�.

}

int main(){
	DequeNode *topPtr = NULL;
	DequeNode *tailPtr = NULL;


}
