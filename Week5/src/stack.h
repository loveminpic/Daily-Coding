#include <stdio.h>
#include <stdlib.h>

typedef struct Stack {
    int *data;
    int top;
    int max;
}Stack;

Stack *newstack(int capa);
int is_empty(Stack *arr);
int is_full(Stack *arr);
void push(Stack *arr, int data);
int pop(Stack *arr);
void free_stack(Stack *arr) ;