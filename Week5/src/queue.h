#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
}Node;

typedef struct Queue {
    Node *front;
    Node *back;
    int count;
}Queue;

Queue *q_create();
void q_push(Queue *que, int data);
int q_pop(Queue *que);
int q_is_empty(Queue *que);
