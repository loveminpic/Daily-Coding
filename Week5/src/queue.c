#include <stdio.h>
#include <stdlib.h>
#include "queue.h"

Queue *q_create(){
    Queue *que = (Queue*)malloc(sizeof(Queue));
    que->front = NULL;
    que->back = NULL;
    que->count = 0;
    return que;
}

void q_push(Queue *que, int data){
    Node *newone =  (Node*)malloc(sizeof(Node));
    newone->data = data;
    newone->next = NULL;
    if(q_is_empty(que)){
        que->front = newone;
    }else{
        que->back->next = newone;
    }
    que->back = newone;
    que->count++;
}

int q_pop(Queue *que){
    if(q_is_empty(que)) {
        printf("this queue is empty!");
        return 0; 
    }
    Node *tempNode = que->front;
    int temp = tempNode->data;
    que->front = que->front->next;
    que->count--;
    free(tempNode);
    return temp;
}

int q_is_empty(Queue *que){
    if(que->count == 0) {
        return 1;
    }
    return 0;
}
